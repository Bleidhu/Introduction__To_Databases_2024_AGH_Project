CREATE PROCEDURE add_event_type
    @event_name NVARCHAR(30)
AS
BEGIN
    BEGIN
        INSERT INTO Event_types (event_name)
        VALUES (@event_name);

    END
END;
go

