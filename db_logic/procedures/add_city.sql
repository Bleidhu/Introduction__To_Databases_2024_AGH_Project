-- Create a stored procedure to add a new city
CREATE PROCEDURE add_city
    @CityName NVARCHAR(30) -- Parameter for the city name
AS
BEGIN
    IF @CityName IS NULL OR LTRIM(RTRIM(@CityName)) = ''
    BEGIN
        THROW 50005, 'City name cannot be empty', 16;
    END

    BEGIN
        INSERT INTO Cities (city_name)
        VALUES (@CityName);
    END
END;
go

