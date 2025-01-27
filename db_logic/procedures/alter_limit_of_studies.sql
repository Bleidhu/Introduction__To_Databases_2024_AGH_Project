CREATE PROCEDURE alter_limit_of_studies
    @studies_id INT,
    @new_limit INT
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @current_enrolled_students INT;

    SELECT @current_enrolled_students = COUNT(*)
    FROM Order_studies
    WHERE studies_id = @studies_id;


    IF @new_limit < @current_enrolled_students
    BEGIN
        THROW 50003, 'There are more current enrolled students than the new limit.', 16;
    END
    ELSE
    BEGIN
        UPDATE Studies_module_meetings
        SET place_limit = @new_limit
        WHERE studies_id = @studies_id;
    END
END;