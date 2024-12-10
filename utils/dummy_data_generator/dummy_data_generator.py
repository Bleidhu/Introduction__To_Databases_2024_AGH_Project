
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

def generate_email_from_name(first_name: str, last_name: str):
    return first_name.lower() + last_name.lower() + "@" + fk.domain_name()
def generate_user(id):
    name, last_name = fk.first_name(), fk.last_name()
    tmp = db_model.User(id, generate_email_from_name(name, last_name), name, last_name, random.randint(0, CITIES_AMOUNT), random.randint(0, COUNTRIES_AMOUNT))

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
    meeting = db_model.CourseModuleMeeting(course_id, id, fk.date_between_dates(date_start=previous_meeting_date), "Stationary", random.randint(0, LANGUAGES_AMOUNt), None, random.randint(0, EMPLOYEES_LIMIT),
                                           str(random.randint(2,10)), 10)
    
    return meeting

def generate_module(id, module_meetings_size, course_start_date, stationary_meetings_size, sync_async_meetings_size, meetings_atendance_list_size):
    module = db_model.CourseModule(id, 0, "Stationary")

    module_meetings = []
    stationary_meetings = []
    sync_async_meetings = []
    meetings_atendance_list = []

    meetings_amount = random.randint(1, COURSE_MODULE_MEETINGS_LIMIT)
    last_meeting_date = course_start_date
    for i in range(meetings_amount + 1):
        tmp_meeting , tmp_module_meetings, tmp_stationary, tmp_sync_async, tmp_attendance = generate_meeting(i+module_meetings_size, 
        course_start_date, last_meeting_date, module_meetings_size + len(module_meetings), stationary_meetings_size + len(stationary_meetings),
        sync_async_meetings_size + len(sync_async_meetings), meetings_atendance_list_size + len(meetings_atendance_list))
        last_meeting_date = tmp_meeting.meeting_date
        module_meetings.append(tmp_meeting)
    
    return module, module_meetings


def generate_course(id, modules_table_size, module_meetings_table_size, enrolled_students_size, stationary_meetings_size, sync_async_meetings_size):
    modules = []
    meetings = []
    enrolled_students = []
    stationary_meetings = []
    sync_async_meetings = []
    meetings_atendance_list = []

    course = db_model.Course(id, fk.catch_phrase(), "Opis", fk.date_this_century(), random.randint(1, COURSE_STUDENTS_LIMIT), random.random()*100, random.randint(0,EMPLOYEES_LIMIT))

    module_amount = random.randint(1, COURSE_MODULES_LIMIT)

    for i in range(module_amount+1):
        module, tmp_meetings, tmp_meeting_attendance_list, tmp_stationary_meetings, tmp_sync_async_meetings, tmp_meeting_attendance_list = generate_module(i+modules_table_size, 
        module_meetings_table_size, course.start_date, enrolled_students_size + len(enrolled_students)
        , stationary_meetings_size + len(stationary_meetings), sync_async_meetings_size + len(sync_async_meetings))
        modules.append(module)
        meetings += tmp_meetings
        stationary_meetings += tmp_stationary_meetings
        sync_async_meetings += tmp_sync_async_meetings
        stationary_meetings += tmp_stationary_meetings
        meetings_atendance_list += tmp_meeting_attendance_list

    return course, modules, meetings, enrolled_students, stationary_meetings, sync_async_meetings, meetings_atendance_list

def generate_courses_table():
    modules_all = []
    meetings_all = []
    enrolled_students_all = []
    sync_async_meeting_all = []
    meetings_atendace_list_all = []
    stationary_meetings = []

    courses = []
    for i in range(COURSES_LIMIT):
        tmp_course, tmp_modules, tmp_meetings, tmp_enrolled_students, tmp_stationary_meetings, tmp_sync_async_meetings, tmp_meetings_attendance_list = generate_course(i, len(modules_all), len(meetings_all), len(enrolled_students_all), len(stationary_meetings), len(sync_async_meeting_all))

        modules_all += tmp_modules
        meetings_all += tmp_meetings
        enrolled_students_all += tmp_enrolled_students 
        sync_async_meeting_all += tmp_sync_async_meetings
        meetings_atendace_list_all += tmp_meetings_attendance_list
        
        courses.append(tmp_course)
    


def main():
    users = generate_users_table()
    print("INSERT INTO Users (user_id, email, first_name, last_name, city_id, country_id, phone, street, house_number)")
    for user in users:
        print("(" + str(user) + ")")

    employees = generate_employees_table()
    for employee in employees:
        print(employee)
    

if __name__ == "__main__":
    main()