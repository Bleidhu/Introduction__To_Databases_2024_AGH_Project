## Funkcje w bazie danych

### Obliczanie średniej oceny dla użytkownika
```sql
create function get_user_average_grade(@user_id int)
    returns float
as
begin
    declare @average float;
select @average = avg(grade) from Exams where user_id = @user_id;
return @average;
end;
```

### Generowanie planu zajęć dla użytkownika
```sql
CREATE FUNCTION get_user_schedule(@user_id INT)
    RETURNS TABLE
    AS
        RETURN(SELECT 'Course'        AS EventType,
                      cm.meeting_name AS EventName,
                      cm.meeting_date AS EventDate,
                      cm.duration     AS Duration,
                      cm.place_limit  AS PlaceLimit,
                      c.course_name   AS Name
               FROM Course_meeting_attendance_list cma
                        JOIN
                    Course_module_meetings cm ON cma.meeting_id = cm.meeting_id AND cma.course_id = cm.course_id
                        JOIN
                    Courses c ON cm.course_id = c.course_id
               WHERE cma.user_id = @user_id

               UNION ALL

               SELECT 'Study'          AS EventType,
                      smm.meeting_name AS EventName,
                      smm.meeting_date AS EventDate,
                      smm.duration     AS Duration,
                      smm.place_limit  AS PlaceLimit,
                      s.studies_name   AS Name
               FROM Studies_meeting_attendance_list sma
                        JOIN
                    Studies_module_meetings smm ON sma.meeting_id = smm.meeting_id AND sma.studies_id = smm.studies_id
                        JOIN
                    Studies s ON smm.studies_id = s.studies_id
               WHERE sma.user_id = @user_id

        );
```

### Czy użytkownik uczestniczył w zajęciach o danym temacie

```sql 
create function was_user_present_in_a_topic ( @topic_id int, @user_id int)
returns bit
begin
    declare @result bit = 0;

    if @user_id in (select user_id from dbo.Studies_meeting_attendance_list
        inner join dbo.Studies_module_meetings on
            dbo.Studies_module_meetings.meeting_id = dbo.Studies_meeting_attendance_list.meeting_id and
            dbo.Studies_module_meetings.studies_id = dbo.Studies_meeting_attendance_list.studies_id
        where topic_id = @topic_id
    ) or (
        @user_id in (select user_id from dbo.Studies_makeup_meeting_attendance_list
            inner join dbo.Studies_module_meetings on
            dbo.Studies_module_meetings.meeting_id = dbo.Studies_makeup_meeting_attendance_list.meeting_id and
            dbo.Studies_module_meetings.studies_id = dbo.Studies_makeup_meeting_attendance_list.studies_id
            where topic_id = @topic_id
        ))
    begin
        set @result = 1;
    end

    return @result
end
go


```

