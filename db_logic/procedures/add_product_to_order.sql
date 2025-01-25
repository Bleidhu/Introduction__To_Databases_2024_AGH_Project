-- dodanie produktu do ISTNIEJACEGO zamówienia
create procedure add_product_to_order @order_id int,
                                      @product_id int,
                                      @product_type_id int
as
begin
    declare @is_order_exists bit;
    declare @is_product_exists bit;
    declare @product_type varchar(50);
    declare @product_price decimal(10, 2);
    declare @order_detail_id int;

    begin TRY
        begin transaction;
        -- Sprawdzenie, czy zamówienie istnieje
        select @is_order_exists = case
                                      when exists (select 1
                                                   from dbo.orders
                                                   where order_id = @order_id) then 1
                                      else 0 end;

        if @is_order_exists = 0
            begin
                throw 50001, 'Zamówienie o podanym ID nie istnieje.', 1;
            end

--     sprawdzenie typu produktu
        select @product_type = event_name
        from Event_types
        where type_id = @product_type_id;

        if @product_type is null
            begin
                throw 50002, 'Nieprawidłowy typ produktu.', 1;
            end

        -- Sprawdzenie, czy produkt istnieje
        select @is_product_exists = case
                                        when @product_type = 'Webinar' then
                                            IIF(exists (select 1
                                                        from dbo.webinars
                                                        where webinar_id = @product_id), 1, 0)
                                        when @product_type = 'Course' then
                                            IIF(exists (select 1
                                                        from dbo.courses
                                                        where course_id = @product_id), 1, 0)
                                        when @product_type = 'Studies' then
                                            IIF(exists (select 1
                                                        from dbo.studies
                                                        where studies_id = @product_id), 1, 0)
                                        when @product_type = 'Study_Module' then
                                            IIF(exists (select 1
                                                        from dbo.Studies_Module
                                                        where studies_module_id = @product_id), 1, 0)
                                        else 0
            end


        --  jeśli produkt nie istnieje
        if @is_product_exists = 0
            begin
                throw 50003, 'Produkt o podanym ID nie istnieje.', 1;
            end

        --     pobranie ceny produktu
        select @product_price = case
                                    when @product_type = 'Webinar' then
                                            (select price from webinars where webinar_id = @product_id)
                                    when @product_type = 'Course' then
                                            (select price from courses where course_id = @product_id)
                                    when @product_type = 'Studies' then
                                            (select price from studies where studies_id = @product_id)
                                    when @product_type = 'Study_Module' then
                                        (select price_for_module
                                         from Studies_Module
                                         where studies_module_id = @product_id)
                                    else 0
            end

--            dodanie produktu do order_details
        insert into Order_details (order_id, type_id, price)
        values (@order_id, @product_type_id, @product_price);
        select @order_detail_id = SCOPE_IDENTITY();

--           dodanie zakupu do odpowiedniej tabeli
        if @product_type = 'Webinar'
            begin
                --                     id z order_details i id webinaru
                insert into Order_webinars (order_detail_id, webinar_id)
                values (@order_detail_id, @product_id);
            end

--            jesli to kurs i dodatkowo czy są wolne miejsca
        else if @product_type = 'Course'
            begin
                if dbo.check_course_places_left(@product_id) > 0
                    begin
                        insert into Order_course (order_detail_id, course_id)
                        values (@order_detail_id, @product_id);
                    end
                else
                    begin
                        throw 50004, 'Brak miejsc na kurs.', 1;
                    end
            end

        else if @product_type = 'Studies'
            begin
                if dbo.check_studies_places_left(@product_id) > 0
                    begin
                        insert into Order_studies (order_detail_id, studies_id)
                        values (@order_detail_id, @product_id);
                    end
                else
                    begin
                        throw 50005, 'Brak miejsc na studia.', 1;
                    end
            end


--             dla modułów bez limitu miejsc
        else if @product_type = 'Study_Module'
            begin
                insert into Order_module_studies (order_detail_id, module_id)
                values (@order_detail_id, @product_id);
            end
        commit transaction;

        SELECT * FROM Order_details WHERE order_id = @order_id;
    end TRY
    begin CATCH
        if @@TRANCOUNT > 0
            rollback transaction;
        throw;
    end CATCH
end