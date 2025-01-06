import db_tables_classes as db_model
from faker import Faker
import datetime
import random
import dummy_values as dval
import employees_generation as emp_gen
import webinars_generation as w_gen
import utility_functions as uf
from typing import List, Tuple
import course_names as cn
fk = Faker()

## Courses
# To do - make sure translators are not multiplied (two meetings one date)
# make better module names
def generate_courses(webinars, employees, translators: List[db_model.Translator], translators_languages: List[db_model.TranslatorsLanguagesUsed]) -> Tuple[List[db_model.Course], List[db_model.CourseModules], List[db_model.CourseModuleMeetings]]:
    COURSES_LIMIT = 4
    COURSE_MODULES_LIMIT = 4
    COURSE_MODULE_MEETINGS_LIMIT = 10
    COURSE_STUDENTS_LIMIT = 10

    COURSES_START_DATE = datetime.datetime(2022, 10, 10)
    COURSES_INTERVAL = datetime.timedelta(14)

    CITIES_AMOUNT = len(dval.cities)
    COUNTRIES_AMOUNT = len(dval.countries)
    LANGUAGES_AMOUNt = len(dval.languages)
    courses = []
    course_modules = []
    corse_enrolled_students = []
    course_module_meetings = []
    course_module_meeting_attendance_list = []
    corse_module_meetings_stationary = []
    course_sync_async_meetings = []
    
    last_course_date = COURSES_START_DATE
    last_meeting_date = COURSES_START_DATE
    
    def generate_course():
        price = random.randint(50, 400)
        nonlocal last_course_date
        start_date = fk.date_between(start_date=last_course_date, end_date=last_course_date + COURSES_INTERVAL)
        tmp_course = db_model.Course(len(courses), 
                                     cn.course_names[len(courses)][0], 
                                     cn.course_names[len(courses)][1], 
                                     start_date.isoformat(), 
                                     COURSE_STUDENTS_LIMIT, price,
                                     course_coordinator_id=random.choice(uf.get_employees_hired_after_date(employees, start_date)).employee_id,
                                     visible_from=start_date.isoformat())
        nonlocal last_meeting_date
        last_meeting_date = start_date
        last_course_date += random.randint(2, 4)*COURSES_INTERVAL
        courses.append(tmp_course)
        generate_course_modules(courses[-1].course_id)
        

    def generate_course_module(course_id):
        module_type = random.randint(0, len(dval.module_types) - 1)
        tmp_module = db_model.CourseModules(len(course_modules), module_type, cn.course_names[course_id][2][len(course_modules)%6][0], course_id)
        course_modules.append(tmp_module)

        generate_course_module_meetings(course_id, module_type, tmp_module.module_id)


    ## fix date to be realistic
    def generate_course_module_meeting(course_id, module_type, module_id):
        nonlocal last_meeting_date
        meeting_type = module_type

        if(module_type == 3):
            meeting_type = random.randint(0, len(dval.meeting_types) - 1)

        meeting_date = fk.date_between_dates(date_start=last_meeting_date, date_end=last_meeting_date+datetime.timedelta(1)*random.randint(2,4))
        last_meeting_date = meeting_date + datetime.timedelta(1)
        
        language_id = 0
        translators_id = None
        if(random.randint(0, 1) == 0):
            language_id = 0
        else:
            language_id = random.randint(1, LANGUAGES_AMOUNt)
        
            translators_of_lang = list(filter(lambda x: x.language_id  == language_id, translators_languages))
            translators_id = translators_of_lang[random.randint(0,len(translators_of_lang) - 1)].translator_id

        lecturer_id = random.choice(uf.get_employees_not_working_on_date(uf.get_employees_hired_after_date(employees, meeting_date), date=meeting_date.isoformat(), webinars_meetings=webinars, course_meetings_table=course_module_meetings)).employee_id
        duration = random.randint(1,4) * 45
        students_limit = 10

        if(meeting_type == 0):
            stationary_meeting = db_model.CourseModuleMeetingStationary(len(corse_module_meetings_stationary), course_id, len(course_module_meetings)-1, 0)
            corse_module_meetings_stationary.append(stationary_meeting)
        elif(meeting_type==1):
            sync_meeting = db_model.CourseSyncAsyncMeeting(len(course_sync_async_meetings), course_id, len(course_module_meetings)-1, None, fk.url(), None)
            course_sync_async_meetings.append(sync_meeting)
        else:
            sync_meeting = db_model.CourseSyncAsyncMeeting(len(course_sync_async_meetings), course_id, len(course_module_meetings)-1, None, None, fk.url())
            course_sync_async_meetings.append(sync_meeting)

        tmp_module_meeting = db_model.CourseModuleMeetings(course_id, 
                                                           len(course_module_meetings), 
                                                           meeting_date, language_id, 
                                                           translators_id, lecturer_id, 
                                                           duration, 
                                                           students_limit, 
                                                           module_id, 
                                                           meeting_type, 
                                                           cn.course_names[course_id][2][module_id%6][1][len(course_module_meetings)%10])
        course_module_meetings.append(tmp_module_meeting)
    
    def generate_course_modules(course_id):
        modules_amount = random.randint(1, COURSE_MODULES_LIMIT)

        for i in range(modules_amount):
            generate_course_module(course_id)


    def generate_course_module_meetings(course_id, module_type, module_id):
        module_meetings_amount = random.randint(1, COURSE_MODULE_MEETINGS_LIMIT)
        for i in range(module_meetings_amount):
            generate_course_module_meeting(course_id, module_type, module_id)
        
    # def generate_course_attendance_list(users):
    #     course : db_model.Course
    #     for  course in courses:
    #         students_limit = course.students_limit

    #         amount_of_students = students_limit - random.randint(1,10)

    #         students_participating = random.sample(users, amount_of_students)

    #         for s in students_participating:
                

    for i in range(COURSES_LIMIT):
        generate_course()

    
    return courses, course_modules, course_module_meetings, corse_module_meetings_stationary, course_sync_async_meetings

def main():
    # users = generate_users_table()
    # print("INSERT INTO Users (user_id, email, first_name, last_name, city_id, country_id, street, phone, house_number, birth_date) VALUES")
    # for user in users:
    #     print("(" + str(user) + "),")

    # employees, translators, translators_languages = emp_gen.generate_employees_table()
    # print("INSERT INTO Employees (employee_id, first_name, last_name, hire_date, birth_date, phone, email, role_id, city_id, country_id) VALUES")
    # for employee in employees:
    #     print("(" + str(employee) + "),")

    # courses, c_mods, c_meetings = generate_courses(translators_languages)

    # for c in c_meetings:
    #     print(c)

    employees, translators, translators_languages = emp_gen.generate_employees_table()
    webinars = w_gen.webinars_generator(employees)
    courses, course_modules, course_module_meetings, stationary_meetings, sync_async_meetings = generate_courses(webinars, employees, translators, translators_languages)

    for course in courses:
        print(course)
        modules = list(filter(lambda x: (x.course_id == course.course_id), course_modules)) 
        for m in modules:
            print("   " + str(m))
            meetings = list(filter(lambda x: (x.module_id == m.module_id and x.course_id == course.course_id ), course_module_meetings)) 
            for m2 in meetings:
                print("        " + str(m2))


if __name__ == "__main__":
    main()
