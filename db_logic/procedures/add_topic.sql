create procedure add_topic(
    @topic_name nvarchar(30),
    @topic_description nvarchar(30)
)
as
begin
    if not exists (
        select 1
        from dbo.topics_list
        where topic_name = @topic_name
    )
    begin
        insert into dbo.topics_list (topic_name, topic_description)
        values (@topic_name, @topic_description);
    end
END;
go

