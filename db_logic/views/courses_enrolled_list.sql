create view dbo.courses_enrolled_list as
select course_id, user_id
from Order_course oc
         inner join Order_details od on oc.order_detail_id = od.order_detail_id
         inner join Orders o on od.order_id = o.order_id
where o.is_paid = 1
   or (getdate() < max_paid_date)
    go

