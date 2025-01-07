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
import users_generation as u_gen
import courses_generation as c_gen
import studies_generator as s_gen
fk = Faker()
course_enrolled = []
orders = []
order_details = []
order_webinars = []
order_course = []
order_module_studies = []
order_studies = []
def generate_enrolled_lists_for_courses(courses: List[db_model.Course], 
                                          course_meetings: List[db_model.CourseModuleMeetings], 
                                          users: List[db_model.User]):
    for c_name, course in enumerate(courses):
        course_enrolled.append([])
        current_course_meetings: List[db_model.CourseModuleMeetings] = list(filter(lambda m: m.course_id == course.course_id, course_meetings))
        # imo we should take into account how many concflict each user has with courses meetings and if its over some treshold don't add him
        users_by_collisions = []
        for user in  users:
            users_course_ids = []
            for i, course_list in enumerate(course_enrolled):
                if user.user_id in course_list:
                    users_course_ids.append(i)
            user_collisions = 0
            for other_meeting in filter(lambda x: x.course_id in users_course_ids , course_meetings):
                for c in current_course_meetings:
                    if other_meeting.meeting_date == c.meeting_date:
                        user_collisions += 1
            users_by_collisions.append((user_collisions, user.user_id))
        random.shuffle(users_by_collisions)
        users_by_collisions.sort(key=lambda x: x[0])

        # edit this so not every course is fully booked
        for i in range(course.students_limit): 
            course_enrolled[c_name].append(users_by_collisions[i][1])

def generate_orders_from_course_enrolled(course_enrolled)


def main():
    users = u_gen.generate_users_table()
    employees, translators, translators_languages = emp_gen.generate_employees_table()
    webinars = w_gen.webinars_generator(employees)
    courses, course_modules, course_module_meetings, stationary_meetings, sync_async_meetings = c_gen.generate_courses(webinars, employees, translators, translators_languages)

    studies, study_modules, study_module_meetings, study_internships,  study_stationary_meetings, study_sync_async_meetings = s_gen.generate_studies(webinars, course_module_meetings, employees, translators, translators_languages)
    generate_enrolled_lists_for_courses(courses, course_module_meetings, users)

    print(course_enrolled)

    

if __name__ == "__main__":
    main()
