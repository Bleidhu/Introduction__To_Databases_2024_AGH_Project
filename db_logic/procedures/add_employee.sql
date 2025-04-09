CREATE PROCEDURE add_employee(
    @FirstName NVARCHAR(30),
    @LastName NVARCHAR(30),
    @HireDate DATE,
    @BirthDate DATE,
    @Phone NVARCHAR(9),
    @Email NVARCHAR(50),
    @RoleID INT,
    @CityID INT,
    @CountryID INT
)
AS
BEGIN
      INSERT INTO Employees (
         first_name,
         last_name,
         hire_date,
         birth_date,
         phone,
         email,
         role_id,
         city_id,
         country_id
      )
      VALUES (
         @FirstName,
         @LastName,
         @HireDate,
         @BirthDate,
         @Phone,
         @Email,
         @RoleID,
         @CityID,
         @CountryID
      );
   END;
go

