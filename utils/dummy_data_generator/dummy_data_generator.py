import db_tables_classes as db_model
from faker import Faker
import datetime
import random
import dummy_values as dval
USERS_LIMIT = 100
EMPLOYEES_LIMIT = 10
COURSES_LIMIT = 10
COURSE_MODULES_LIMIT = 10
COURSE_MODULE_MEETINGS_LIMIT = 10
COURSE_STUDENTS_LIMIT = 10
CITIES_AMOUNT = len(dval.cities)
COUNTRIES_AMOUNT = len(dval.countries)
LANGUAGES_AMOUNt = len(dval.languages)
WEBINARS_AMOUNT = 10

import employees_generation as e_gen
import users_generation as u_gen
import webinars_generation as w_gen
import courses_generation as c_gen
import studies_generator as s_gen
import generate_orders as o_gen

import utility_functions as uf
import csv

fk = Faker()

def main():
    # users = generate_users_table()
    # print("INSERT INTO Users (user_id, email, first_name, last_name, city_id, country_id, street, phone, house_number, birth_date) VALUES")
    # for user in users:
    #     print("(" + str(user) + "),")

    # employees, translators, translators_languages = employees_gen.generate_employees_table()
    # print("INSERT INTO Employees (employee_id, first_name, last_name, hire_date, birth_date, phone, email, role_id, city_id, country_id) VALUES")
    # for employee in employees:
    #     print("(" + str(employee) + "),")
    
    

    # courses, course_modules, course_meetings, course_enrolled_students, course_sync_async_meetings, course_attendance_list, course_stationary_meetings = generate_courses_table()

    # courses, c_modules, c_metings_modules = generate_courses()

    # for course in courses:
    #     print(course)
    # for module in c_modules:
    #     print(module)
    # for meeting in c_metings_modules:
    #     print(meeting)
    # uf.object_table_table_to_csv(dval.cities, "./dummy_data/cities.csv")
    # uf.object_table_table_to_csv(dval.countries, "./dummy_data/countries.csv")
    # uf.object_table_table_to_csv(dval.languages, "./dummy_data/languages.csv")
    # uf.object_table_table_to_csv(dval.module_types, "./dummy_data/module_types.csv")
    # uf.object_table_table_to_csv(dval.meeting_types, "./dummy_data/meeting_types.csv")
    needs_to_be_generated = {'defaults': True,
                            'users': False, 
                             'employees': False, 
                             'webinars': False,
                             'courses': False,
                             'studies': True,
                             'orders': True}
    if(needs_to_be_generated.get('defaults')):
        uf.dict_to_csv(dval.cities, "./dummy_data/cities.csv")
        uf.dict_to_csv(dval.countries, "./dummy_data/countries.csv")
        uf.dict_to_csv(dval.languages, "./dummy_data/languages.csv")
        uf.dict_to_csv(dval.module_types, "./dummy_data/module_types.csv")
        uf.dict_to_csv(dval.meeting_types, "./dummy_data/meeting_types.csv")
        uf.dict_to_csv(dval.employee_roles, "./dummy_data/roles.csv")
        uf.dict_to_csv(dval.topics, "./dummy_data/topics.csv")
    users = []
    if(needs_to_be_generated.get('users')):
        users = u_gen.generate_users_table()
        uf.object_table_table_to_csv(users, "./dummy_data/users.csv")
    else:
        users = []
        with open("./dummy_data/users.csv", mode='r') as file:
            reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
            for row in reader:
                # Create an object from the row data
                person = db_model.User(int(row['user_id']), row['email'], row['first_name'], row['last_name'],
                                       int(row['city_id']), int(row['country_id']), row['phone'], row['street'], row['house_number'], row['birth_date'])
                users.append(person)
    employees = []
    translators = []
    translators_languages = []
    if(needs_to_be_generated.get('employees')):
        employees, translators, translators_languages = e_gen.generate_employees_table()
        uf.object_table_table_to_csv(employees, "./dummy_data/employees.csv")
        uf.object_table_table_to_csv(translators, "./dummy_data/translators.csv")
        uf.object_table_table_to_csv(translators_languages, "./dummy_data/translators_languages.csv")
    else:
        with open("./dummy_data/employees.csv", mode='r') as file:
            reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
            for row in reader:
                # Create an object from the row data
                person = db_model.Employee(int(row['employee_id']), row['first_name'], row['last_name'], 
                                           datetime.date.fromisoformat(row['hire_date']), row['birth_date'], row['phone'], row['email'],
                                       int(row['role_id']), int(row['city_id']), int(row['country_id']))
                employees.append(person)
        with open("./dummy_data/translators.csv", mode='r') as file:
            reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
            for row in reader:
                # Create an object from the row data
                person = db_model.Translator(int(row['translator_id']), int(row['employee_id']))
                translators.append(person)
        with open("./dummy_data/translators_languages.csv", mode='r') as file:
            reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
            for row in reader:
                # Create an object from the row data
                person = db_model.TranslatorsLanguagesUsed(int(row['id']),int(row['translator_id']), int(row['language_id']))
                translators_languages.append(person)
    webinars = []
    if(needs_to_be_generated.get('employees')):
        webinars = w_gen.webinars_generator(employees)
        uf.object_table_table_to_csv(webinars, "./dummy_data/webinars.csv")
    else:
        with open("./dummy_data/webinars.csv", mode='r') as file:
            reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
            for row in reader:
                # Create an object from the row data
                webinar = db_model.Webinar(int(row['webinar_id']), row['name'], row['description'], int(row['teacher_id']), 
                                           int(row['price']), 
                                           row['can_buy_from'], 
                                           row['recording_link'],
                                       row['start_date'])
                webinars.append(webinar)
    courses = []
    course_modules = []
    course_module_meetings = []
    stationary_meetings = []
    sync_async_meetings = []
    if(needs_to_be_generated.get('studies')):
        courses, course_modules, course_module_meetings, stationary_meetings, sync_async_meetings = c_gen.generate_courses(webinars, employees, translators, translators_languages)
        uf.object_table_table_to_csv(courses, "./dummy_data/courses.csv")
        uf.object_table_table_to_csv(course_modules, "./dummy_data/course_modules.csv")
        uf.object_table_table_to_csv(course_module_meetings, "./dummy_data/course_module_meetings.csv")
        uf.object_table_table_to_csv(stationary_meetings, "./dummy_data/stationary_meetings.csv")
        uf.object_table_table_to_csv(sync_async_meetings, "./dummy_data/sync_async_meetings.csv")
    else:
        with open("./dummy_data/courses.csv", mode='r') as file:
            reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
            for row in reader:
                # Create an object from the row data
                course = db_model.Course(int(row['course_id']), row['course_name'], row['course_description'], 
                                        datetime.date.fromisoformat(row['start_date']), int(row['students_limit']), int(row['price']), int(row['course_coordinator_id']),
                                    datetime.date.fromisoformat(row['visible_from']))
                courses.append(course)
        with open("./dummy_data/course_modules.csv", mode='r') as file:
            reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
            for row in reader:
                # Create an object from the row data
                module = db_model.CourseModules(int(row['module_id']), int(row['module_type_id']), row['module_name'], int(row['course_id']))
                course_modules.append(module)
        with open("./dummy_data/course_module_meetings.csv", mode='r') as file:
            reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
            for row in reader:
                # Create an object from the row data
                meeting = db_model.CourseModuleMeetings(int(row['course_id']), int(row['meeting_id']), row['meeting_date'], int(row['language_id']), int(row['translator_id']) if row['translator_id'] != '' else None, int(row['lecturer_id']), int(row['duration']), int(row['place_limit']), int(row['module_id']), int(row['meeting_type_id']), row['meeting_name'] )
                course_module_meetings.append(meeting)
        with open("./dummy_data/stationary_meetings.csv", mode='r') as file:
            reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
            for row in reader:
                # Create an object from the row data
                meeting = db_model.CourseStationaryMeeting(int(row['id']), int(row['course_id']), int(row['meeting_id']), int(row['classrom']) )
                stationary_meetings.append(meeting)
        with open("./dummy_data/sync_async_meetings.csv", mode='r') as file:
            reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
            for row in reader:
                # Create an object from the row data
                meeting = db_model.CourseSyncAsyncMeeting(int(row['id']), int(row['course_id']), int(row['meeting_id']), row['acces_to'], row['video_link'], row['stream_link'])
                sync_async_meetings.append(meeting)
   
    studies = []
    study_modules = []
    study_module_meetings = []
    study_internships = []
    study_stationary_meetings = []
    study_sync_async_meetings = []
    if(needs_to_be_generated.get('studies')):
            studies, study_modules, study_module_meetings, study_internships,  study_stationary_meetings, study_sync_async_meetings = s_gen.generate_studies(webinars, course_module_meetings, employees, translators, translators_languages)
            uf.object_table_table_to_csv(studies, "./dummy_data/studies.csv")
            uf.object_table_table_to_csv(study_modules, "./dummy_data/study_modules.csv")
            uf.object_table_table_to_csv(study_module_meetings, "./dummy_data/study_module_meetings.csv")
            uf.object_table_table_to_csv(study_internships, "./dummy_data/study_internships.csv")
            uf.object_table_table_to_csv(study_stationary_meetings, "./dummy_data/study_stationary_meetings.csv")
            uf.object_table_table_to_csv(study_sync_async_meetings, "./dummy_data/study_sync_async_meetings.csv")
    else:
        with open("./dummy_data/studies.csv", mode='r') as file:
            reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
            for row in reader:
                # Create an object from the row data
                study = db_model.Study(int(row['study_id']), row['studies_name'], row['studies_descritpion'], datetime.date.fromisoformat(row['start_date']), int(row['students_limit']), int(row['price']), int(row['studies_coordinator_id']), datetime.date.fromisoformat(row['visible_from']))
                studies.append(study)
        with open("./dummy_data/stude_modules.csv", mode='r') as file:
            reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
            for row in reader:
                # Create an object from the row data
                module = db_model.StudyModule(int(row['studies_module_id']), int(row['module_type_id']), row['module_name'], int(row['studies_id']), int(row['price_for_module']))
                study_modules.append(module)
        with open("./dummy_data/study_module_meetings.csv", mode='r') as file:
            reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
            for row in reader:
                # Create an object from the row data
                meeting = db_model.StudyModuleMeeting(int(row['meeting_id']), int(row['studies_id']), row['meeting_date'], int(row['language_id']), int(row['translator_id']), int(row['lecturer_id']), int(row['duration']), int(row['place_limit']), int(row['module_id']), int(row['topic_id']), row['meeting_name'], int(row['meeting_type_id']))
                study_module_meetings.append(meeting)
        with open("./dummy_data/study_stationary_meetings.csv", mode='r') as file:
            reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
            for row in reader:
                # Create an object from the row data
                meeting = db_model.CourseStationaryMeeting(int(row['id']), int(row['studies_id']), int(row['meeting_id']), int(row['classrom']) )
                study_stationary_meetings.append(meeting)
        with open("./dummy_data/study_sync_async_meetings.csv", mode='r') as file:
            reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
            for row in reader:
                # Create an object from the row data
                meeting = db_model.StudySyncAsyncMeeting(int(row['id']), int(row['studies_id']), int(row['meeting_id']), datetime.date.fromisoformat(row['acces_to']), row['video_link'], row['stream_link'])
                study_sync_async_meetings.append(meeting)
        with open("./dummy_data/study_internships.csv", mode='r') as file:
            reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
            for row in reader:
                # Create an object from the row data
                internship = db_model.InternshipMeeting(int(row['studies_id']), int(row['inter_meeting_id']), datetime.date.fromisoformat(row['meeting_date']))
                study_internships.append(internship)

    
    
    orders = []
    orders_details = []
    orders_courses = []
    orders_studies = []
    course_attendace = []
    study_attendance = []
    internship_attendance = []
    if(needs_to_be_generated.get('orders')):
            orders, orders_details, orders_courses, orders_studies, course_attendace =  o_gen.generate_orders(courses, course_module_meetings, users, studies, study_module_meetings, study_internships)
            uf.object_table_table_to_csv(orders, "./dummy_data/orders.csv")
            uf.object_table_table_to_csv(orders_details, "./dummy_data/orders_details.csv")
            uf.object_table_table_to_csv(orders_courses, "./dummy_data/orders_courses.csv")
            uf.object_table_table_to_csv(orders_studies, "./dummy_data/orders_studies.csv")
            uf.object_table_table_to_csv(course_attendace, "./dummy_data/course_attendance.csv")
    else:
        with open("./dummy_data/orders.csv", mode='r') as file:
            reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
            for row in reader:
                # Create an object from the row data
                order = db_model.Order(int(row['order_id']), int(row['user_id']), bool(row['is_paid']), datetime.date.fromisoformat(row['max_paid_date']))
                orders.append(order)
        with open("./dummy_data/orders_details.csv", mode='r') as file:
            reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
            for row in reader:
                # Create an object from the row data
                detail = db_model.OrderDetail(int(row['order_detail_id']), int(row['order_id']), int(row['type_id']), int(row['price']))
                orders_details.append(detail)
        with open("./dummy_data/orders_courses.csv", mode='r') as file:
            reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
            for row in reader:
                # Create an object from the row data
                order = db_model.OrderCourse(int(row['order_detail_id']), int(row['course_id']))
                orders_courses.append(order)
        with open("./dummy_data/orders_studies.csv", mode='r') as file:
            reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
            for row in reader:
                # Create an object from the row data
                order = db_model.OrderStudy(int(row['order_detail_id']), int(row['studies_id']))
                orders_studies.append(order)
        
if __name__ == "__main__":
    main()
