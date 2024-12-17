
import db_tables_classes as db_model
from faker import Faker
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

fk = Faker()

## Users and employees
# To do:

def generate_email_from_name(first_name: str, last_name: str):
    return first_name.lower() + last_name.lower() + "@" + fk.domain_name()
def generate_user(id):
    name, last_name = fk.first_name(), fk.last_name()
    tmp = db_model.User(id, generate_email_from_name(name, last_name), name, last_name, random.randint(0, CITIES_AMOUNT), random.randint(0, COUNTRIES_AMOUNT), random.randint(100000000, 999999999), fk.street_name(), fk.building_number(), fk.date_of_birth(minimum_age=16, maximum_age=80))

    return tmp

def generate_users_table():
    tmp = [generate_user(i) for i in range(USERS_LIMIT)]

    return tmp

def generate_role_id():
    return 0

def generate_employee(id, role):
    tmp = db_model.Employee(id,  fk.first_name(), fk.last_name(), fk.date_of_birth(minimum_age=18, maximum_age=60), fk.date_this_decade() ,fk.phone_number(), fk.email(), role ,random.randint(0, CITIES_AMOUNT), random.randint(0, COUNTRIES_AMOUNT))

    

    return tmp

def generate_employees_table():
    teachers = [generate_employee(i, 1) for i in range(EMPLOYEES_LIMIT)]
    translators = [generate_employee(i+len(teachers), 2) for i in range(EMPLOYEES_LIMIT*0,5)]
    translators_table = [db_model.Translator(i, i+len(teachers)) for i in range(EMPLOYEES_LIMIT*0,5)]
    translators_language_used = []
    ceo = generate_employee(len(teachers) + len(translators), 0)
    all_employees = teachers + translators
    all_employees.append(ceo)
    return all_employees, translators_table, translators_language_used

## Webinars
# To do: Better descriptions (maybe from chatgpt)
# Better start date 
# Assigning teachers

def generate_webinar(id):
    start_date = fk.date_this_decade()
    return db_model.Webinar(id, fk.catch_phrase(), "Lorem ipsum", 0, random.randint(0, 500) ,start_date, fk.url(), start_date)
def generate_webinars():
    webinars = []
    for i in range(WEBINARS_AMOUNT):
        webinars.append(generate_webinar(i))
    return webinars


## Courses
def generate_meeting(id, course_id, course_start_date, previous_meeting_date, type_number):
    # add dates so they won't overlap
    meeting_type_number = 0
    if(type_number != 3):
        meeting_type_number = type_number
    else:
        meeting_type_number = random.randint(0,2)


    meeting = db_model.CourseModuleMeetings(course_id, id, fk.date_between_dates(date_start=previous_meeting_date), dval.meeting_types[meeting_type_number] , random.randint(0, LANGUAGES_AMOUNt), None, random.randint(0, EMPLOYEES_LIMIT),
                                           str(random.randint(2,10)), 10, meeting_type_number, "Name")
    stationary = None
    sync_async = None

    if meeting_type_number == 0:
        stationary = db_model.CourseModuleMeetingStationary(id, course_id, 0, 0)
    elif meeting_type_number == 1:
        sync_async = db_model.CourseSyncAsyncMeeting(id, course_id, 0, "something", fk.url(), fk.url())
    else:
        sync_async = db_model.CourseSyncAsyncMeeting(id, course_id, 0, "something", fk.url(), "")

    presence = []

    return meeting, stationary , sync_async, presence

def generate_module(id, course_id, course_start_date):

    type_number = random.randint(0, 3)

    type_string = dval.module_types[type_number]

    


    module = db_model.CourseModules(id, 0, type_string, course_id)

    module_meetings = []
    stationary_meetings = []
    sync_async_meetings = []
    meetings_atendance_list = []

    meetings_amount = random.randint(1, COURSE_MODULE_MEETINGS_LIMIT)
    last_meeting_date = course_start_date
    for i in range(meetings_amount + 1):
        tmp_meeting, tmp_stationary, tmp_sync_async, tmp_attendance = generate_meeting(i, course_id,
        course_start_date, last_meeting_date, type_number)

        module_meetings.append(tmp_meeting)
        if(tmp_stationary):
            stationary_meetings.append(tmp_stationary)
        if(tmp_sync_async):
            sync_async_meetings.append(tmp_sync_async)
        meetings_atendance_list += tmp_attendance

        last_meeting_date = tmp_meeting.meeting_date

        module_meetings.append(tmp_meeting)
    
    return module, module_meetings, stationary_meetings, sync_async_meetings, meetings_atendance_list


def generate_course(id):
    modules = []
    meetings = []
    enrolled_students = []
    stationary_meetings = []
    sync_async_meetings = []
    meetings_atendance_list = []

    start_date = fk.date_this_century()

    course = db_model.Course(id, fk.catch_phrase(), "Opis", start_date, random.randint(1, COURSE_STUDENTS_LIMIT), random.random()*100, random.randint(0,USERS_LIMIT), start_date)

    module_amount = random.randint(1, COURSE_MODULES_LIMIT)

    for i in range(module_amount+1):
        module, tmp_meetings, tmp_stationary_meetings, tmp_sync_async_meetings, tmp_meeting_attendance_list = generate_module(i, id, course.start_date)
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
        tmp_course, tmp_modules, tmp_meetings, tmp_enrolled_students, tmp_stationary_meetings, tmp_sync_async_meetings, tmp_meetings_attendance_list = generate_course(i)

        modules_all += tmp_modules
        meetings_all += tmp_meetings
        enrolled_students_all += tmp_enrolled_students 
        sync_async_meeting_all += tmp_sync_async_meetings
        meetings_atendace_list_all += tmp_meetings_attendance_list
        stationary_meetings += tmp_stationary_meetings
        
        courses.append(tmp_course)
    i = 0
    for meeting in meetings_all:
        meeting.meeting_id = i
        i += 1

    i = 0

    for met in sync_async_meeting_all:
        met.meeting_id = i
        i += 1

    return courses, modules_all, meetings_all, enrolled_students_all, sync_async_meeting_all, meetings_atendace_list_all, stationary_meetings
    


def main():
    users = generate_users_table()
    print("INSERT INTO Users (user_id, email, first_name, last_name, city_id, country_id, street, phone, house_number, birth_date) VALUES")
    for user in users:
        print("(" + str(user) + "),")

    # employees, translators, translators_languages = generate_employees_table()
    # for employee in employees:
    #     print(str(employee) + " " + dval.employee_roles[employee.role_id])

    courses, course_modules, course_meetings, course_enrolled_students, course_sync_async_meetings, course_attendance_list, course_stationary_meetings = generate_courses_table()
    
    # for module in course_modules:
    #     print(module)

    # for course in courses:
    #     print(course)

    # for meeting in course_meetings:
    #     print(meeting)
    
    # for met in course_sync_async_meetings:
    #     print(met)
    
    # for statio in course_stationary_meetings:
    #     print(statio)

    # webinars = generate_webinars()

    # for webinar in webinars:
    #     print(webinar)
if __name__ == "__main__":
    main()