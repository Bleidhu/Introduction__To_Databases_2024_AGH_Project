-- sprawdza czy student ma zaliczone wszystkie przedmioty z danego semestru,
-- frekwencje na poziomie 80% oraz 100% na praktykach
create function check_if_user_pass_studies(@studies_id int, @user_id int)
    returns bit as
begin
    declare @total_attendance float;
    declare @intership_absence int;
    declare @exam_grade float;
    declare @enrolled bit;

--  jesli nie jest zapisany na dany przedmiot to nie zalicza
    select @enrolled = count(*) from studies_enrolled_list
    where studies_id = @studies_id
      and user_id = @user_id;

    if @enrolled = 0
        return 0;

--  jesli nie ma 80% frekwencji to nie zalicza
    select @total_attendance = dbo.get_user_attendance_percentage(@studies_id, @user_id);

    if @total_attendance < 80
        return 0;

--  jesli ma nieobecnosci na praktykach to nie zalicza
    select @intership_absence = count(*) from Intership_meeting_attendance_list
    where studies_id = @studies_id
      and user_id = @user_id
      and was_present = 0;

    if @intership_absence > 0
        return 0;

--  jesli ma niezaliczony egzamin to nie zalicza
    select @exam_grade = grade from Exams
    where studies_id = @studies_id
      and user_id = @user_id;

    if  @exam_grade is null or @exam_grade < 3
        return 0;



--  w przeciwnym wypadku zalicza
    return 1;

end

