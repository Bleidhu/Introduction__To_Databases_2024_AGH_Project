
import db_tables_classes as db_model
from faker import Faker
import random
import dummy_values as dval
USERS_LIMIT = 10
EMPLOYEES_LIMIT = 10
COURSES_LIMIT = 10
COURSE_MODULES_LIMIT = 10
COURSE_MODULE_MEETINGS_LIMIT = 10
COURSE_STUDENTS_LIMIT = 10
CITIES_AMOUNT = len(dval.cities)
COUNTRIES_AMOUNT = len(dval.countries)
LANGUAGES_AMOUNt = len(dval.languages)

fk = Faker()

def generate_user(id):
    tmp = db_model.User(id, fk.email(), fk.first_name(), fk.last_name(), random.randint(0, CITIES_AMOUNT), random.randint(0, COUNTRIES_AMOUNT))

    return tmp

def generate_users_table():
    tmp = [generate_user(i) for i in range(USERS_LIMIT)]

    return tmp

def generate_role_id():
    return 0

def generate_employee(id):
    tmp = db_model.Employee(id,  fk.first_name(), fk.last_name(), fk.date_of_birth(minimum_age=18, maximum_age=60), fk.date_this_decade() ,fk.phone_number(), fk.email(), generate_role_id(),random.randint(0, CITIES_AMOUNT), random.randint(0, COUNTRIES_AMOUNT))

    

    return tmp

def generate_employees_table():
    tmp = [generate_employee(i) for i in range(EMPLOYEES_LIMIT)]
    #translators =  look for translators and append them here
    return tmp

def generate_meeting(id, course_id, course_start_date, previous_meeting_date):
    # add dates so they won't overlap
    meeting = db_model.CourseModuleMeeting(course_id, id, fk.date(), "Stationary", random.randint(0, LANGUAGES_AMOUNt), None, random.randint(0, EMPLOYEES_LIMIT),
                                           "90min", 10)
    
    return meeting

def generate_module(id, module_meetings_size, course_start_date):
    module = db_model.CourseModule(id, 0, "Stationary")

    module_meetings = []

    meetings_amount = random.randint(1, COURSE_MODULE_MEETINGS_LIMIT)
    last_meeting_date = course_start_date
    for i in range(meetings_amount + 1):
        meeting = generate_meeting(i+module_meetings_size, course_start_date, last_meeting_date)
        last_meeting_date = meeting.meeting_date
        module_meetings.append(meeting)
    
    return module, module_meetings


def generate_course(id, modules_table_size, module_meetings_table_size):
    modules = []
    meetings = []
    enrolled_students = []
    stationary_meetings = []
    sync_async_meetings = []
    meetings_atendance_list = []

    course = db_model.Course(id, fk.catch_phrase(), "Opis", fk.date_this_century(), random.randint(1, COURSE_STUDENTS_LIMIT), random.random()*100, random.randint(0,EMPLOYEES_LIMIT))

    module_amount = random.randint(1, COURSE_MODULES_LIMIT)

    for i in range(module_amount+1):
        module, tmp_meetings = generate_module(i+modules_table_size, module_meetings_table_size, course.start_date)
        modules.append(module)
        meetings += tmp_meetings

    return course, modules, meetings

    


def main():
    users = generate_users_table()
    for user in users:
        print(user)

    employees = generate_employees_table()

if __name__ == "__main__":
    main()