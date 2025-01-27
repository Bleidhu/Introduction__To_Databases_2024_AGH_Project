create procedure add_exams (@studies_id int, @user_id int, @grade int)
as begin
    if exists ( select 1 from dbo.studies_enrolled_list
                         where dbo.studies_enrolled_list.studies_id = @studies_id
                                                        and dbo.studies_enrolled_list.user_id = @user_id
    )
        begin
        insert into Exams (studies_id, user_id, grade) values (@studies_id,@user_id,@grade);
        print 'Values added!';
        end
    else
        throw 50020, 'There is not such student that is enrolled in this course', 1;
end
go

