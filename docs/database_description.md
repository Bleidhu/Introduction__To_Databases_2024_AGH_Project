# Tabele w bazie danych

## Webinar

### Webinar_info
- webinar_id
- user_id  
- teacher_id
- price
- purchased_date

### Webinar_details
- webinar_id
- recording_link

## Course

### Courses
- course_id
- course_name
- course_description
- start_date
- students_limit
- price
- course_coordinator_id


### Course_enrolled_students
- course_id
- user_id
- is_paid

### Course_module
- course_id
- module_id
- module_type 

### Course_module_meetings
- meeting_id
- course_id
- module_id
- meeting_date
- meeting_type
- language_id
- translator_id
- lecturer_id
- duration
- place_limit

### Course_meeting_attendance_list
- user_id
- meeting_id
- meeting_id


### Course_sync_async_meeting
- id
- meeting_id
- accessTo
- video_link
- stream_link

### Course_module_meeting_stationary
- id
- meeting_id
- classroom


## Studies

### Studies_module_meetings
- meeting_id
- studies_id
- module_id
- meeting_date
- meeting_type
- language_id
- translator_id
- lecturer_id
- duration
- place_limit
- price_for_free_listener

### Internship_meeting_attendance_list
- inter_meeting_id
- user_id
- was_present

### Internship_meetings
- inter_meeting_id
- studies_id
- intership_id
- meetind_date

### Studies_meeting_attendance_list
- user_id
- meeting_id
- was_present


### Studies
- studies_id
- studies_name
- studies_description
- start_date
- students_limit
- price
- studies_coordinator_id


### Studies_module_meeting_stationary
- id
- meeting_id
- classroom

### Studies_enrolled_students
- studies_id
- user_id
- is_paid

### Studies_sync_async_meeting
- id
- meeting_id
- accessTo
- video_link
- stream_link

### Studies_module
- module_id
- studies_id
- module_type


## Orders and Payment


### Order_webinars
- order_detail_id
- webinar_id

### Order_details
- order_detail_id
- order_id
- type_id
- pay_date
- price

### Orders
- order_id
- user_id
- is_paid

### Event_types
- type_id
- event_name

### Order_course
- order_detail_id
- course_id

### Order_studies
- order_detail_id
- studies_id

### Order_meeting_studies
- order_detail_id
- studies_id
- meeting_id


## People

### Users
- user_id
- email
- first_name
- last_name
- city_id
- country_id
- phone
- street
- house_number 

### Employees
- employee_id
- first_name
- last_name
- hire_date
- birth_date
- phone
- email
- role_id
- city_id
- country_id

### Cities
- city_id
- city_name

### Countries
- country_id
- country_name

### Employee_Roles
- role_id
- employee_id
- role_name

### Translators
- translator_id
- employee_id

### Translators_languages_used
- id
- translator_id
- language_id

### Languages
- language_id
- language_name
