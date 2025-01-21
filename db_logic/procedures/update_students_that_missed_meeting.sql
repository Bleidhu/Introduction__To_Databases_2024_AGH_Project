-- dla wszystkich użytkowników, którzy nie maja zaznaczonej obencości na zajęciach ustaw, że byli na nich nieobecni

CREATE PROCEDURE update_students_that_missed_meeting @studies_id INT,
                                                        @meeting_id INT
AS
BEGIN
    set nocount on;

--     dla wszystkich uzytkowników zapisanych na studia @studies_id, którzy nie byli obecni na spotkaniu @meeting_id dodaj ich brak obecnosci do listy
    insert into Studies_meeting_attendance_list (user_id, studies_id, meeting_id, was_present)
    select el.user_id, @studies_id, @meeting_id, 0
    from studies_enrolled_list el
    where el.studies_id = @studies_id
      and el.user_id not in (select user_id
                             from Studies_meeting_attendance_list
                             where studies_id = @studies_id
                               and meeting_id = @meeting_id);


END;