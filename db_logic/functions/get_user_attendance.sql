CREATE FUNCTION get_user_attendance_percentage
(
    @studies_id INT,
    @user_id INT
)
    RETURNS FLOAT
AS
BEGIN
    DECLARE @total_meetings INT;
    DECLARE @present_meetings INT;

    SELECT @total_meetings = COUNT(*)
    FROM Studies_module_meetings
    WHERE studies_id = @studies_id;

    SELECT @present_meetings = COUNT(*)
    FROM Studies_meeting_attendance_list
    WHERE studies_id = @studies_id
      AND user_id = @user_id
      AND (was_present = 1 OR did_makeup = 1);

    -- Jeśli brak spotkań, zwróć 0 (unikamy dzielenia przez 0)
    IF @total_meetings = 0
        RETURN 0;

    -- Zwróć procent obecności
    RETURN CAST(@present_meetings AS FLOAT) / CAST(@total_meetings AS FLOAT) * 100;
END;
