## Widoki w bazie danych

### Wypisanie użytkowników, którzy ukończyli dane studia z wynikiem pozytywnym
```sql
create view dbo.check_if_user_passed as
    select user_id, cast(1 as bit) as pass
    from Users u
    where not exists(select 1
                     from Intership_meeting_attendance_list ia
                     where u.user_id = ia.user_id
                       and was_present = 0)
      and ((select SUM(IIF(was_present = 1, 1, 0)) from Studies_meeting_attendance_list sa)
        / (select count(was_present) from Studies_meeting_attendance_list sa)) >= 0.8
      and (select grade from Exams e where e.user_id = u.user_id) >= 3.0
    union
    select user_id, cast(0 as bit) as pass
    from Users u
    where user_id not in (select user_id
                          from Users u
                          where not exists(select 1
                                           from Intership_meeting_attendance_list ia
                                           where u.user_id = ia.user_id
                                             and was_present = 0)
                            and ((select SUM(IIF(was_present = 1, 1, 0)) from Studies_meeting_attendance_list sa)
                              / (select count(was_present) from Studies_meeting_attendance_list sa)) >= 0.8
                            and (select grade from Exams e where e.user_id = u.user_id) >= 3.0)
go


```


### Liczba zamówień dla poszczególnych użytkowników
```sql 
create view dbo.number_of_orders_by_user as
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
```

### Użytkownicy zapisani na dany kurs

```sql
create view dbo.courses_enrolled_list as
    select course_id, user_id
    from Order_course oc
             inner join Order_details od on oc.order_detail_id = od.order_detail_id
             inner join Orders o on od.order_id = o.order_id
    where o.is_paid = 1
       or (getdate() < max_paid_date)
go

```

### Użytkownicy zapisani na dane studia

```sql 
create view dbo.studies_enrolled_list as
    select studies_id, user_id
    from Order_studies os
             inner join Order_details od on os.order_detail_id = od.order_detail_id
             inner join Orders o on od.order_id = o.order_id
    where o.is_paid = 1
       or (getdate() < max_paid_date)
go
```

### Użytkownicy zapisani na dany webinar

```sql 
create view dbo.webinar_enrolled_list as
    select webinar_id, user_id
    from Order_webinars ow
             inner join Order_details od on ow.order_detail_id = od.order_detail_id
             inner join Orders o on od.order_id = o.order_id
    where o.is_paid = 1
       or (getdate() < max_paid_date)
go

```


