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
import courses_generation as c_gen
import studies_generator as s_gen
fk = Faker()

def generate_attendance_lists_for_courses(courses: List[db_model.CourseModules], course_meetings: List[db_model.CourseModuleMeetings]):
    # imo we should take into account how many concflict each user has with courses meetings and if its over some treshold don't add him
    users_course_ids = 
    pass



def main():
    employees, translators, translators_languages = emp_gen.generate_employees_table()
    webinars = w_gen.webinars_generator(employees)
    courses, course_modules, course_module_meetings, stationary_meetings, sync_async_meetings = c_gen.generate_courses(webinars, employees, translators, translators_languages)

    studies, study_modules, study_module_meetings, study_internships,  study_stationary_meetings, study_sync_async_meetings = s_gen.generate_studies(webinars, course_module_meetings, employees, translators, translators_languages)
    

    

if __name__ == "__main__":
    main()
