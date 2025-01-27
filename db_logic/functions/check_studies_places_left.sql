-- sprawdza ile zostało wolnych miejsc na na studiach
create function check_studies_places_left(@studies_id int)
    returns int as
begin
    declare @limit int;
    declare @result int;
select @limit = students_limit from Studies where studies_id = @studies_id;
select @result = @limit - (select count(*) from studies_enrolled_list sel where studies_id = @studies_id);
return @result;
end