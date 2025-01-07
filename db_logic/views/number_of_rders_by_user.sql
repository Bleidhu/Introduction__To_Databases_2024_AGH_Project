alter view dbo.number_of_orders_by_user as
    with what_user_ordered as (select Orders.user_id,
                                      Order_details.order_detail_id
                               from Orders
                                        inner join
                                    Order_details
                                    on
                                        Orders.order_id = Order_details.order_id),
         order_webinars_ as (select what_user_ordered.user_id,
                                    count(Order_webinars.webinar_id) as c
                             from what_user_ordered
                                      inner join
                                  Order_webinars
                                  on
                                      Order_webinars.order_detail_id = what_user_ordered.order_detail_id
                             group by what_user_ordered.user_id),
         order_studies_ as (select what_user_ordered.user_id,
                                   count(Order_studies.studies_id) as c
                            from what_user_ordered
                                     inner join
                                 dbo.Order_studies
                                 on
                                     Order_studies.order_detail_id = what_user_ordered.order_detail_id
                            group by what_user_ordered.user_id),
         order_modules_ as (select what_user_ordered.user_id,
                                   count(Order_module_studies.module_id) as c
                            from what_user_ordered
                                     inner join
                                 dbo.Order_module_studies
                                 on
                                     Order_module_studies.order_detail_id = what_user_ordered.order_detail_id
                            group by what_user_ordered.user_id),
         order_course_ as (select what_user_ordered.user_id,
                                  count(Order_course.course_id) as c
                           from what_user_ordered
                                    inner join
                                dbo.Order_course
                                on
                                    Order_course.order_detail_id = what_user_ordered.order_detail_id
                           group by what_user_ordered.user_id)
select t.user_id, sum(t.c) as order_count
from (select *
      from order_studies_
      union
      select *
      from order_modules_
      union
      select *
      from order_webinars_
      union
      select *
      from order_course_) as t
group by t.user_id
    go

