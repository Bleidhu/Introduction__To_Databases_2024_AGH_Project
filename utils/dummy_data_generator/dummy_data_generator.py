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

    users = u_gen.generate_users_table()
    uf.object_table_table_to_csv(users, "./dummy_data/users.csv")
    employees, translators, translators_languages = e_gen.generate_employees_table()
    uf.object_table_table_to_csv(employees, "./dummy_data/employees.csv")
    uf.object_table_table_to_csv(translators, "./dummy_data/translators.csv")
    uf.object_table_table_to_csv(translators_languages, "./dummy_data/translators_languages.csv")
    webinars = w_gen.webinars_generator(employees)
    uf.object_table_table_to_csv(webinars, "./dummy_data/webinars.csv")
    courses, course_modules, course_module_meetings, stationary_meetings, sync_async_meetings = c_gen.generate_courses(webinars, employees, translators, translators_languages)
    uf.object_table_table_to_csv(courses, "./dummy_data/courses.csv")
    uf.object_table_table_to_csv(course_modules, "./dummy_data/course_modules.csv")
    uf.object_table_table_to_csv(course_module_meetings, "./dummy_data/course_module_meetings.csv")
    uf.object_table_table_to_csv(stationary_meetings, "./dummy_data/stationary_meetings.csv")
    uf.object_table_table_to_csv(sync_async_meetings, "./dummy_data/sync_async_meetings.csv")
    studies, study_modules, study_module_meetings, study_internships,  study_stationary_meetings, study_sync_async_meetings = s_gen.generate_studies(webinars, course_module_meetings, employees, translators, translators_languages)
    uf.object_table_table_to_csv(studies, "./dummy_data/studies.csv")
    uf.object_table_table_to_csv(study_modules, "./dummy_data/study_modules.csv")
    uf.object_table_table_to_csv(study_module_meetings, "./dummy_data/study_module_meetings.csv")
    uf.object_table_table_to_csv(study_internships, "./dummy_data/study_internships.csv")
    uf.object_table_table_to_csv(study_stationary_meetings, "./dummy_data/study_stationary_meetings.csv")
    uf.object_table_table_to_csv(study_sync_async_meetings, "./dummy_data/study_sync_async_meetings.csv")
    
    orders, orders_details, orders_courses, orders_studies =  o_gen.generate_orders(courses, course_module_meetings, users, studies, study_module_meetings, study_internships)
    uf.object_table_table_to_csv(orders, "./dummy_data/orders.csv")
    uf.object_table_table_to_csv(orders_details, "./dummy_data/orders_details.csv")
    uf.object_table_table_to_csv(orders_courses, "./dummy_data/orders_courses.csv")
    uf.object_table_table_to_csv(orders_studies, "./dummy_data/orders_studies.csv")
if __name__ == "__main__":
    main()
