-- jeśli użytkownik jest zapisany na podane studia ustaw ze byl obecny

CREATE PROCEDURE check_course_attendance @user_id INT,
                                         @course_id INT,
                                         @meeting_id INT
AS
BEGIN
    DECLARE @is_enrolled BIT;

    -- Sprawdzenie, czy użytkownik jest zapisany na kurs
    SELECT @is_enrolled = CASE
                              WHEN EXISTS (SELECT 1
                                           FROM dbo.courses_enrolled_list
                                           WHERE user_id = @user_id
                                             AND course_id = @course_id) THEN 1
                              ELSE 0 END;

    IF @is_enrolled = 1
        BEGIN
            insert into Course_meeting_attendance_list (user_id, course_id, meeting_id, was_present)
            values (@user_id, @course_id, @meeting_id, 1);
        END


END;