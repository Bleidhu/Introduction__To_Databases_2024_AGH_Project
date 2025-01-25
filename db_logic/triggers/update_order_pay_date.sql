-- DROP TRIGGER IF EXISTS update_order_pay_date;

-- po dodaniu zamówienia sprawdza czy data zamówienia jest wcześniejsza niż data ostatniego opłaconego produktu
create trigger update_order_pay_date
    on Order_details
    after insert
    as
begin
    declare @order_id int;
    declare @product_type_id int;
    declare @product_type varchar(50);
    declare @product_id int;
    declare @order_detail_id int;
    declare @start_date date;

    declare inserted_cursor cursor for
        select order_id, type_id, order_detail_id
        from inserted;

    open inserted_cursor;
    fetch next from inserted_cursor into @order_id, @product_type_id, @order_detail_id;

    while @@FETCH_STATUS = 0
        begin
            select @product_type = case
                                       when @product_type_id = 1 then 'Webinar'
                                       when @product_type_id = 2 then 'Course'
                                       when @product_type_id = 3 then 'Studies'
                                       when @product_type_id = 4 then 'Study_Module'
                                       else 'Unknown'
                end;

            if @product_type = 'Course'
                begin
                    select @product_id = course_id
                    from Order_course
                    where order_detail_id = @order_detail_id;

                    select @start_date = start_date
                    from Courses
                    where course_id = @product_id;
                end
            else if @product_type = 'Studies'
                begin
                    select @product_id = studies_id
                    from Order_studies
                    where order_detail_id = @order_detail_id;

                    select @start_date = start_date
                    from Studies
                    where studies_id = @product_id;
                end
            else if @product_type = 'Webinar'
                begin
                    select @product_id = webinar_id
                    from Order_webinars
                    where order_detail_id = @order_detail_id;

                    select @start_date = start_date
                    from Webinars
                    where webinar_id = @product_id;
                end
            else if @product_type = 'Study_Module'
                begin
                    select @product_id = module_id
                    from Order_module_studies
                    where order_detail_id = @order_detail_id;

                    select @start_date = min(meeting_date)
                    from Studies_module_meetings
                    where module_id = @product_id;
                end
            else
                begin
                    fetch next from inserted_cursor into @order_id, @product_type_id, @order_detail_id;
                    continue;
                end

            update Orders
            set max_paid_date = dateadd(day, -3, @start_date)
            where order_id = @order_id
              and max_paid_date < dateadd(day, -3, @start_date);

            fetch next from inserted_cursor into @order_id, @product_type_id, @order_detail_id;
        end

    close inserted_cursor;
    deallocate inserted_cursor;
end