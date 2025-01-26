-- Sprawdza średnią ocenę w egzaminie dla danego przedmiotu, I guess
create function get_average_grade_in_exam(@studies_id int)
    returns float
as
begin
    declare @average float;
    select @average = avg(grade) from Exams where studies_id = @studies_id;
    return @average;
end
go
