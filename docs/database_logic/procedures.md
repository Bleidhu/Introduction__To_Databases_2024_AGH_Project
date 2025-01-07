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