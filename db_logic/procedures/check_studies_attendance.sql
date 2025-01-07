CREATE PROCEDURE check_studies_attendance @user_id INT,
                                          @studies_id INT,
                                          @meeting_id INT
AS
BEGIN
    DECLARE @is_enrolled BIT;

    -- Sprawdzenie, czy użytkownik jest zapisany na studia
    SELECT @is_enrolled = CASE
                              WHEN EXISTS (SELECT 1
                                           FROM dbo.studies_enrolled_list
                                           WHERE user_id = @user_id
                                             AND studies_id = @studies_id) THEN 1
                              ELSE 0 END;

    IF @is_enrolled = 1
        BEGIN
            insert into Studies_meeting_attendance_list (user_id, studies_id, meeting_id, was_present)
            values (@user_id, @studies_id, @meeting_id, 1);
        END
    ELSE
        BEGIN
            insert into Studies_makeup_meeting_attendance_list (user_id, studies_id, meeting_id)
            values (@user_id, @studies_id, @meeting_id);
        END

END;