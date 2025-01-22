CREATE PROCEDURE delete_user
    @user_id INT
AS
BEGIN
    SET NOCOUNT ON;

    IF NOT EXISTS (SELECT 1 FROM Users WHERE user_id = @user_id)
    BEGIN
        PRINT 'Uzytkownik nie znaleziony';
        RETURN;
    END

    DELETE FROM Users
    WHERE user_id = @user_id;

    PRINT 'Uzytkownik usuniety';
END
go

