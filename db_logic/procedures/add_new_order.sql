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
