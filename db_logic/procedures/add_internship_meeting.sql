create procedure add_internship_meeting
( @studies_id int, @meeting_date datetime )
as begin

    if exists ( select 1 from Studies where studies_id = @studies_id)
    begin
    insert into Intership_meetings (studies_id, meetind_date)
    values (@studies_id, @meeting_date);
    print 'Values added';
    end
    else
    begin
        throw 50020, 'Value could not be added',16;
    end
end
go

