CREATE PROCEDURE alter_limit_of_courses
    @course_id INT,
    @new_limit INT
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @current_enrolled_students INT;

    SELECT @current_enrolled_students = COUNT(*)
    FROM Order_course
    WHERE course_id = @course_id;

    IF @new_limit < @current_enrolled_students
    BEGIN
        THROW 50018, 'There are more current enrolled students than the new limit.', 16;
    END
    ELSE
    BEGIN
        UPDATE Course_module_meetings
        SET place_limit = @new_limit
        WHERE course_id = @course_id;
    END
END;