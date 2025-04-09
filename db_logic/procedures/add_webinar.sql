CREATE PROCEDURE add_webinar
    @name nvarchar(30),
    @description nvarchar(300),
    @teacher_id int,
    @price money,
    @can_buy_from date,
    @recording_link nvarchar(30),
    @start_date date
AS
BEGIN

    IF @price < 0
    BEGIN
        THROW 50010, 'Cena musi być dodatnia', 16;
        RETURN;
    END

    INSERT INTO Webinars (name, description, teacher_id, price, can_buy_from, recording_link, start_date)
    VALUES (@name, @description, @teacher_id, @price, @can_buy_from, @recording_link, @start_date);

    PRINT 'Webinar został dodany';
END;
go

