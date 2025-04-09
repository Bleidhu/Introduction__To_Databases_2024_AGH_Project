-- jesli uzytkownik ma jakies odrobione zajecia z tym samym tematem co przesłane to ustaw ze odrobil zajecia
-- oraz odrobienia oznacz jako "zuzyte"

CREATE PROCEDURE set_attendance_for_student_that_makeup_meeting @studies_id INT,
                                                                @meeting_id INT,
                                                                @user_id INT
AS
BEGIN
    declare @makeup_meeting_id INT;
    declare @topic_id INT;

    select @topic_id = topic_id
    from Studies_module_meetings
    where meeting_id = @meeting_id
      and studies_id = @studies_id;

    select top 1 @makeup_meeting_id = makeup_list_id
    from Studies_makeup_meeting_attendance_list smmal
             join Studies_module_meetings smm on smmal.meeting_id = smm.meeting_id and smmal.studies_id = smm.studies_id
    where topic_id = @topic_id
      and user_id = @user_id
      and smmal.used = 0;

    if @makeup_meeting_id is not null
        begin
            update Studies_makeup_meeting_attendance_list set used = 1 where makeup_list_id = @makeup_meeting_id;

            update Studies_meeting_attendance_list
            set did_makeup = 1
            where meeting_id = @meeting_id
              and studies_id = @studies_id
              and user_id = @user_id;
            return 0;
        end
    else
        begin
--             jednak zwracanie succes/failure bo wykorzystujemy w check_user_attendance
            return 1;
--             raiserror ('Student did not make up the meeting', 16, 1);

        end


END;


