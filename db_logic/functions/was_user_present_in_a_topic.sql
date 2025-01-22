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

