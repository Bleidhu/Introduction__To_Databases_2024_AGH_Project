create procedure create_study(
    @study_id int output ,
    @studies_name nvarchar(30),
    @studies_description nvarchar(300),
    @start_date date,
    @students_limit int,
    @price money,
    @studies_coordinator_id int,
    @visible_from date
) as
    begin
        if @students_limit <= 0
            throw 50000, 'Students limit has to be positive',11;
        else if @price < 0
            throw 50001, 'Price cannot be negative',16;

        if not exists(select 1 from dbo.Employees where employee_id = @studies_coordinator_id)
            throw 50002, 'Coordinator ID does not exist', 11;

        insert into dbo.Studies (studies_name, studies_description, start_date, students_limit, price, studies_coordinator_id, visible_from)
        values (@studies_name,@studies_description,@start_date,
                @students_limit, @price, @studies_coordinator_id, @visible_from)
    end;
go

