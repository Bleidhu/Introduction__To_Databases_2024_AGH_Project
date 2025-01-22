CREATE PROCEDURE delete_study
    @study_id INT
AS
BEGIN
    SET NOCOUNT ON;

    -- Check if the study exists
    IF NOT EXISTS (SELECT 1 FROM Studies WHERE studies_id = @study_id)
    BEGIN
        PRINT 'Nie znaleziono studiow';
        RETURN;
    END

    -- Delete the study
    DELETE FROM Studies
    WHERE studies_id = @study_id;

    PRINT 'Studia usuniete';
END
go

