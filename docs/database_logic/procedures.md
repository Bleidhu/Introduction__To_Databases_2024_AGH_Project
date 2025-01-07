## Procedury w bazie danych

### Dodawanie nowego zamówienia

```sql
-- tworzenie typu tabeli dla OrderDetailsTableType

CREATE TYPE OrderDetailsTableType AS TABLE
    (
    type_id INT,
    price MONEY
    );

-- ----------------------------------------------


CREATE PROCEDURE add_new_order @user_id INT,
    @is_paid BIT,
    @max_paid_date DATETIME,
    @paid_date DATETIME,
    @order_details OrderDetailsTableType READONLY
AS
BEGIN
    DECLARE
@order_id INT;

INSERT INTO Orders (user_id, is_paid, max_paid_date, paid_date)
VALUES (@user_id, @is_paid, @max_paid_date, @paid_date);

-- ID dodanego zamówienia
SET
@order_id = SCOPE_IDENTITY();

    -- Dodanie szczegółów zamówienia do tabeli Order_details
INSERT INTO Order_details (order_id, type_id)
SELECT @order_id, type_id
FROM @order_details;

-- Dodanie szczegółów zamówienia do odpowiednich tabel

INSERT INTO Order_webinars (order_detail_id, webinar_id, price)
SELECT od.order_detail_id, od.order_detail_id, odt.price
FROM Order_details od
         JOIN @order_details odt ON od.type_id = odt.type_id
WHERE od.order_id = @order_id
  AND od.type_id = 1;

INSERT INTO Order_course (order_detail_id, course_id, price)
SELECT od.order_detail_id, od.order_detail_id, odt.price
FROM Order_details od
         JOIN @order_details odt ON od.type_id = odt.type_id
WHERE od.order_id = @order_id
  AND od.type_id = 2;

INSERT INTO Order_studies (order_detail_id, studies_id, price)
SELECT od.order_detail_id, od.order_detail_id, odt.price
FROM Order_details od
         JOIN @order_details odt ON od.type_id = odt.type_id
WHERE od.order_id = @order_id
  AND od.type_id = 3;

INSERT INTO Order_module_studies (order_detail_id, module_id, price)
SELECT od.order_detail_id, od.order_detail_id, odt.price
FROM Order_details od
         JOIN @order_details odt ON od.type_id = odt.type_id
WHERE od.order_id = @order_id
  AND od.type_id = 4;
END;

```

### Sprawdzanie listy obecności dla kursu

```sql
CREATE PROCEDURE check_course_attendance @user_id INT,
                                         @course_id INT,
                                         @meeting_id INT
AS
BEGIN
    DECLARE @is_enrolled BIT;

    -- Sprawdzenie, czy użytkownik jest zapisany na kurs
    SELECT @is_enrolled = CASE
                              WHEN EXISTS (SELECT 1
                                           FROM dbo.courses_enrolled_list
                                           WHERE user_id = @user_id
                                             AND course_id = @course_id) THEN 1
                              ELSE 0 END;

    IF @is_enrolled = 1
        BEGIN
            insert into Course_meeting_attendance_list (user_id, course_id, meeting_id, was_present)
            values (@user_id, @course_id, @meeting_id, 1);
        END


END;
```

### Odnajdywanie studentów, którzy nie byli obecni na spotkaniu

```sql
CREATE PROCEDURE check_for_students_that_missed_meeting @studies_id INT,
                                                        @meeting_id INT
AS
BEGIN
    set nocount on;

--     dla wszystkich uzytkowników zapisanych na studia @studies_id, którzy nie byli obecni na spotkaniu @meeting_id dodaj ich brak obecnosci do listy
    insert into Studies_meeting_attendance_list (user_id, studies_id, meeting_id, was_present)
    select el.user_id, @studies_id, @meeting_id, 0
    from studies_enrolled_list el
    where el.studies_id = @studies_id
      and el.user_id not in (select user_id
                             from Studies_meeting_attendance_list
                             where studies_id = @studies_id
                               and meeting_id = @meeting_id);


END;
```

### Sprawdzanie listy obecności dla studiów

```sql
CREATE PROCEDURE check_studies_attendance @user_id INT,
                                          @studies_id INT,
                                          @meeting_id INT
AS
BEGIN
    DECLARE @is_enrolled BIT;

    -- Sprawdzenie, czy użytkownik jest zapisany na studia
    SELECT @is_enrolled = CASE
                              WHEN EXISTS (SELECT 1
                                           FROM dbo.studies_enrolled_list
                                           WHERE user_id = @user_id
                                             AND studies_id = @studies_id) THEN 1
                              ELSE 0 END;

    IF @is_enrolled = 1
        BEGIN
            insert into Studies_meeting_attendance_list (user_id, studies_id, meeting_id, was_present)
            values (@user_id, @studies_id, @meeting_id, 1);
        END
    ELSE
        BEGIN
            insert into Studies_makeup_meeting_attendance_list (user_id, studies_id, meeting_id)
            values (@user_id, @studies_id, @meeting_id);
        END

END;
```

### Sprawdzanie łącznej wartości zamówień

```sql
create procedure get_total_order_cost @order_id int
as
begin
    declare @total_cost float
    select @total_cost = sum(price) from Order_details where order_id = @order_id
    return @total_cost
end
```

### Ustawianie obecności dla studenta
```sql
CREATE PROCEDURE set_attendance_for_student_that_makeup_meeting @studies_id INT,
                                                                @meeting_id INT,
                                                                @user_id INT
AS
BEGIN
    declare @makeup_meeting_id INT;
    declare @topic_id INT;

    select @topic_id = topic_id from Studies_module_meetings where meeting_id = @meeting_id and studies_id = @studies_id;

    select top 1 @makeup_meeting_id = makeup_list_id from Studies_makeup_meeting_attendance_list smmal
                                                              join Studies_module_meetings smm on smmal.meeting_id = smm.meeting_id and smmal.studies_id = smm.studies_id
    where topic_id = @topic_id and user_id = @user_id and smmal.used = 0;

    if @makeup_meeting_id is not null
        begin
            update Studies_makeup_meeting_attendance_list set used = 1 where makeup_list_id = @makeup_meeting_id;
            update Studies_meeting_attendance_list set did_makeup = 1 where meeting_id = @meeting_id and studies_id = @studies_id and user_id = @user_id;
        end




END;
```

### Dodanie nowego tematu 
``` sql
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
end;
```

### Dodanie nowego użytkownika

```sql 
CREATE PROCEDURE add_user
    @Email NVARCHAR(50),
    @FirstName NVARCHAR(30),
    @LastName NVARCHAR(30),
    @CityID INT,
    @CountryID INT,
    @Phone NVARCHAR(9),
    @Street NVARCHAR(30),
    @HouseNumber INT,
    @BirthDate DATE
AS
BEGIN
        IF DATEDIFF(YEAR, @BirthDate, GETDATE()) >= 100
        BEGIN
            THROW 50003, 'User must be less than 100 years old.', 16;
        END

        IF PATINDEX('%[^0-9]%', @Phone) > 0 OR LEN(@Phone) <> 9
        BEGIN
            THROW 50004,'Phone number must be exactly 9 numeric characters.', 16;
        END

        INSERT INTO Users (
            email, first_name, last_name, city_id, country_id, phone, street, house_number, birth_date
        )
        VALUES (
            @Email, @FirstName, @LastName, @CityID, @CountryID, @Phone, @Street, @HouseNumber, @BirthDate
        );
END;

```

### Dodanie nowego miasta

``` sql
CREATE PROCEDURE add_city
    @CityName NVARCHAR(30) 
AS
BEGIN
                            -- obciecie lewych i prawych spacji
    IF @CityName IS NULL OR LTRIM(RTRIM(@CityName)) = ''
    BEGIN
        THROW 50005, 'City name cannot be empty', 16;
    END

    BEGIN
        INSERT INTO Cities (city_name)
        VALUES (@CityName);
    END
END;
GO
``` 

### Dodanie nowego pracownika

```sql 
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

```

### Dodanie nowego typu wydarzenia

```sql 
CREATE PROCEDURE add_event_type
    @event_name NVARCHAR(30)
AS
BEGIN
    BEGIN
        INSERT INTO Event_types (event_name)
        VALUES (@event_name);

    END
END;
```

### Sprawdzenie czy użytkownik jest zapisany na kurs

``` sql
CREATE PROCEDURE check_course_attendance
    @user_id INT,
    @course_id INT,
    @meeting_id INT
AS
BEGIN
    DECLARE @is_enrolled BIT;

    -- Sprawdzenie, czy użytkownik jest zapisany na kurs
    SELECT @is_enrolled = CASE WHEN EXISTS (
        SELECT 1
        FROM dbo.courses_enrolled_list
        WHERE user_id = @user_id AND course_id = @course_id
    ) THEN 1 ELSE 0 END;

    IF @is_enrolled = 1
        BEGIN
            insert into Course_meeting_attendance_list (user_id, course_id, meeting_id, was_present)
            values (@user_id, @course_id, @meeting_id, 1);
        END
    ELSE
        BEGIN
            PRINT 'Użytkownik nie jest zapisany na kurs!';
        END
END;
go
```


### Dodanie nowego zamówienia

```sql 
CREATE PROCEDURE add_new_order
    @user_id INT,
    @is_paid BIT,
    @max_paid_date DATETIME,
    @paid_date DATETIME,
    @order_details OrderDetailsTableType READONLY
AS
BEGIN
    DECLARE @order_id INT;

    INSERT INTO Orders (user_id, is_paid, max_paid_date, paid_date)
    VALUES (@user_id, @is_paid, @max_paid_date, @paid_date);

    -- ID dodanego zamówienia
    SET @order_id = SCOPE_IDENTITY();

    -- Dodanie szczegółów zamówienia do tabeli Order_details
    INSERT INTO Order_details (order_id, type_id)
    SELECT @order_id, type_id
    FROM @order_details;

    -- Dodanie szczegółów zamówienia do odpowiednich tabel

    INSERT INTO Order_webinars (order_detail_id, webinar_id, price)
    SELECT od.order_detail_id, od.order_detail_id, odt.price
    FROM Order_details od
             JOIN @order_details odt ON od.type_id = odt.type_id
    WHERE od.order_id = @order_id
      AND od.type_id = 1;

    INSERT INTO Order_course (order_detail_id, course_id, price)
    SELECT od.order_detail_id, od.order_detail_id, odt.price
    FROM Order_details od
             JOIN @order_details odt ON od.type_id = odt.type_id
    WHERE od.order_id = @order_id
      AND od.type_id = 2;

    INSERT INTO Order_studies (order_detail_id, studies_id, price)
    SELECT od.order_detail_id, od.order_detail_id, odt.price
    FROM Order_details od
             JOIN @order_details odt ON od.type_id = odt.type_id
    WHERE od.order_id = @order_id
      AND od.type_id = 3;

    INSERT INTO Order_module_studies (order_detail_id, module_id, price)
    SELECT od.order_detail_id, od.order_detail_id, odt.price
    FROM Order_details od
             JOIN @order_details odt ON od.type_id = odt.type_id
    WHERE od.order_id = @order_id
      AND od.type_id = 4;
END;
go


```

### Usuniecie studiów o danym indeksie
```sql 
CREATE PROCEDURE delete_study
    @study_id INT
AS
BEGIN
    SET NOCOUNT ON;

    IF NOT EXISTS (SELECT 1 FROM Studies WHERE studies_id = @study_id)
    BEGIN
        PRINT 'Nie znaleziono studiow';
        RETURN;
    END

    DELETE FROM Studies
    WHERE studies_id = @study_id;

    PRINT 'Studia usuniete';
END

```

### Usuniecie użytkownika o danym indeksie
```sql 
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

``` 

### Dodanie webinaru 

```sql 
CREATE PROCEDURE add_webinar
    @name nvarchar(30),
    @description nvarchar(300),
    @teacher_id int,
    @price money,
    @can_buy_from date,
    @recording_link nvarchar(30),
    @start_date date
AS
BEGIN
    
    IF @price < 0
    BEGIN
        THROW 50010, 'Cena musi być dodatnia', 16;
        RETURN;
    END

    INSERT INTO Webinars (name, description, teacher_id, price, can_buy_from, recording_link, start_date)
    VALUES (@name, @description, @teacher_id, @price, @can_buy_from, @recording_link, @start_date);

    PRINT 'Webinar został dodany';
END;

``` 