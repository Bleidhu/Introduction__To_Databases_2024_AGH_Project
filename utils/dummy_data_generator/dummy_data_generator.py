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

import employees_generation as employees_gen

fk = Faker()

def main():
    # users = generate_users_table()
    # print("INSERT INTO Users (user_id, email, first_name, last_name, city_id, country_id, street, phone, house_number, birth_date) VALUES")
    # for user in users:
    #     print("(" + str(user) + "),")

    employees, translators, translators_languages = employees_gen.generate_employees_table()
    print("INSERT INTO Employees (employee_id, first_name, last_name, hire_date, birth_date, phone, email, role_id, city_id, country_id) VALUES")
    for employee in employees:
        print("(" + str(employee) + "),")

    # courses, course_modules, course_meetings, course_enrolled_students, course_sync_async_meetings, course_attendance_list, course_stationary_meetings = generate_courses_table()

    # courses, c_modules, c_metings_modules = generate_courses()

    # for course in courses:
    #     print(course)
    # for module in c_modules:
    #     print(module)
    # for meeting in c_metings_modules:
    #     print(meeting)

if __name__ == "__main__":
    main()
