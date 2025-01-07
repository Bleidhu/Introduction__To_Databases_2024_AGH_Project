create function get_user_average_grade(@user_id int)
    returns float
as
begin
    declare @average float;
select @average = avg(grade) from Exams where user_id = @user_id;
return @average;
end;