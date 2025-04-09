-- sprawdza ile zostało wolnych miejsc na na kursie
create function check_course_places_left(@course_id int)
    returns int as
begin
    declare @limit int;
    declare @result int;
select @limit = students_limit from Courses where course_id = @course_id;
select @result = @limit - (select count(*) from courses_enrolled_list where course_id = @course_id);
return @result;
end