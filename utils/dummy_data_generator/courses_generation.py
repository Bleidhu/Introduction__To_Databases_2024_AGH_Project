import db_tables_classes as db_model
from faker import Faker
import datetime
import random
import dummy_values as dval
COURSES_LIMIT = 10
COURSE_MODULES_LIMIT = 10
COURSE_MODULE_MEETINGS_LIMIT = 10
COURSE_STUDENTS_LIMIT = 10
CITIES_AMOUNT = len(dval.cities)
COUNTRIES_AMOUNT = len(dval.countries)
LANGUAGES_AMOUNt = len(dval.languages)
import employees_generation as emp_gen
fk = Faker()

## Courses
def generate_courses(translators):
    courses = []
    course_modules = []
    corse_enrolled_students = []
    course_module_meetings = []
    course_module_meeting_attendance_list = []
    corse_module_meetings_stationary = []
    course_sync_async_meetings = []
    last_date = None
    def generate_course():
        start_date = fk.date_between(start_date=datetime.datetime(2010, 4, 12), end_date=datetime.datetime(2024, 10, 10))
        tmp_course = db_model.Course(len(courses), 
                                     fk.catch_phrase(), 
                                     "Lorem Ipsum", 
                                     start_date, 
                                     COURSE_STUDENTS_LIMIT, 0,
                                     course_coordinator_id=0,
                                     visible_from=start_date)
        nonlocal last_date
        last_date = start_date
        courses.append(tmp_course)
        generate_course_modules(courses[-1].course_id)
        

    def generate_course_module(course_id):
        module_type = random.randint(0, len(dval.module_types) - 1)
        tmp_module = db_model.CourseModules(len(course_modules), module_type, fk.catch_phrase(), course_id)
        course_modules.append(tmp_module)

        generate_course_module_meetings(course_id, module_type, tmp_module.module_id)


    ## fix date to be realistic
    def generate_course_module_meeting(course_id, module_type, module_id):
        nonlocal last_date
        meeting_date = fk.date_between_dates(date_start=last_date)
        last_date = meeting_date
        
        language_id = 0
        translators_id = None
        if(random.randint(0, 1) == 0):
            language_id = 0
        else:
            language_id = random.randint(1, LANGUAGES_AMOUNt)
            translators_of_lang = list(filter(lambda x: x.language_id == language_id, translators))
            translators_id = translators_of_lang[random.randint(0,len(translators_of_lang) - 1)].translator_id

        meeting_type = 0

        lecturer_id = 0
        duration = 90
        students_limit = 10

        tmp_module_meeting = db_model.CourseModuleMeetings(course_id, 
                                                           len(course_module_meetings), 
                                                           meeting_date, language_id, 
                                                           translators_id, lecturer_id, 
                                                           duration, 
                                                           students_limit, 
                                                           module_id, 
                                                           meeting_type, 
                                                           "tmp")
        course_module_meetings.append(tmp_module_meeting)
    
    def generate_course_modules(course_id):
        modules_amount = random.randint(1, COURSE_MODULES_LIMIT)

        for i in range(modules_amount):
            generate_course_module(course_id)


    def generate_course_module_meetings(course_id, module_type, module_id):
        module_meetings_amount = random.randint(1, COURSE_MODULE_MEETINGS_LIMIT)
        for i in range(module_meetings_amount):
            generate_course_module_meeting(course_id, module_type, module_id)
        
    
    for i in range(COURSES_LIMIT):
        generate_course()

    return courses, course_modules, course_module_meetings

def main():
    # users = generate_users_table()
    # print("INSERT INTO Users (user_id, email, first_name, last_name, city_id, country_id, street, phone, house_number, birth_date) VALUES")
    # for user in users:
    #     print("(" + str(user) + "),")

    employees, translators, translators_languages = emp_gen.generate_employees_table()
    print("INSERT INTO Employees (employee_id, first_name, last_name, hire_date, birth_date, phone, email, role_id, city_id, country_id) VALUES")
    for employee in employees:
        print("(" + str(employee) + "),")

    courses, c_mods, c_meetings = generate_courses(translators_languages)

    for c in c_meetings:
        print(c)

if __name__ == "__main__":
    main()
