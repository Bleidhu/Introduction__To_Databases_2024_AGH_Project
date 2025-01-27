create function get_learning_progress_of_a_student(@user_id int)
    returns table
        as
        return (
            select @user_id, topid_id from
            (
            select topic_id from Studies_meeting_attendance_list
                inner join Studies_module_meetings on
                Studies_module_meetings.studies_id = Studies_meeting_attendance_list.studies_id
            where user_id = @user_id and was_present = 1
            union
            select topic_id from Studies_makeup_attendance_list
                inner join Studies_module_meetings on
                Studies_module_meetings.studies_id = Studies_makeup_attendance_list.studies_id
            where user_id = @user_id
            ) as covered_topics inner join topics_list on
            topics_list.topic_id = covered_topics.topic_id
        );
--
-- try
--     begin transaction
--     end
-- catch
--     rollback
--     throw
