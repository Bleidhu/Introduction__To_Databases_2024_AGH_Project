-- sprawdza % obecnosci studenta na zajeciach

create procedure get_user_attendance_procedure  @studies_id int, @user_id int, @result float output
as
begin
    declare @meeting_id int;
    declare @was_present bit;
    declare @did_makeup bit;
    declare @total_meetings int = 0;
    declare @present_meetings int = 0;

    declare @status int;

    declare attendance_cursor cursor for
        select meeting_id, was_present, did_makeup
        from Studies_meeting_attendance_list
        where studies_id = @studies_id
          and user_id = @user_id;

--     dla kazdego rekordu w attendance_list sprawdz czy student byl obecny, jesli nie to sprawdz czy odrobil zajecia
    open attendance_cursor;
    fetch next from attendance_cursor into @meeting_id, @was_present, @did_makeup;
    while @@fetch_status = 0
        begin
            if @was_present = 1
                set @present_meetings = @present_meetings + 1;
            else
                if @did_makeup = 1
                    set @present_meetings = @present_meetings + 1;
                else
                    begin
                        --   jesli student nie byl obecny i nie odrobil zajec to sprawdz czy ma odrobione zajecia
                        exec @status = set_attendance_for_student_that_makeup_meeting
                                    @studies_id,
                                    @meeting_id,
                                       @user_id;
                        if @status = 0
                            begin
                                set @present_meetings = @present_meetings + 1;
                            end

                    end
            set @total_meetings = @total_meetings + 1;
            fetch next from attendance_cursor into @meeting_id, @was_present, @did_makeup;
        end
    close attendance_cursor;
    deallocate attendance_cursor;

    if @total_meetings = 0
        set @result = 0;
    else
        set @result = @present_meetings / @total_meetings;
end