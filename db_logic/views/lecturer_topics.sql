select Employees.employee_id, concat(Employees.first_name, ' ', Employees.last_name) as full_name, topic_name
    from Employees
             inner join Studies_module_meetings on
        Employees.employee_id = Studies_module_meetings.lecturer_id
             inner join topics_list on
        Studies_module_meetings.topic_id = topics_list.topic_id