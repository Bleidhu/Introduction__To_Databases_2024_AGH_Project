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
import datetime
fk = Faker()

def generate_orders(courses, course_meetings, users, studies, study_meetings, study_internships):
    course_enrolled = []
    study_enrolled = []
    orders = []
    order_details = []
    order_webinars = []
    order_course = []
    order_module_studies = []
    order_studies = []


    def generate_webinars_orders():
        pass
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

    def generate_orders_from_course_enrolled(course_enrolled, courses: List[db_model.Course]):
        for i, enrolled_users in enumerate(course_enrolled):
            current_course = courses[i]
            course_start_date = datetime.datetime.fromisoformat(current_course.start_date)
            course_pay_before_Date = course_start_date + datetime.timedelta(14)

            for user_id in enrolled_users:
                tmp_order = db_model.Order(len(orders), user_id=user_id, is_paid=1, max_paid_date=course_pay_before_Date)
                tmp_order_detail = db_model.OrderDetail(len(order_details), tmp_order.order_id, 1, courses[i].price)
                tmp_order_course = db_model.OrderCourse(tmp_order_detail.order_detail_id, i)

                orders.append(tmp_order)
                order_details.append(tmp_order_detail)
                order_course.append(tmp_order_course)


    def generate_course_meetings_attendance_list_of_enrolled_students():
        pass

    def generate_enrolled_lists_for_studies(courses: List[db_model.Course], 
                                            course_meetings: List[db_model.CourseModuleMeetings], 
                                            users: List[db_model.User], studies: List[db_model.Study], study_meetings: List[db_model.StudyModuleMeeting], study_internship: List[db_model.InternshipMeeting]):
        for s_id, study in enumerate(studies):
            study_enrolled.append([])
            current_study_meetings: List[db_model.StudyModuleMeeting] = list(filter(lambda m: m.studies_id == study.studies_id, study_meetings))
            current_study_internships: List[db_model.InternshipMeeting] = list(filter(lambda m: m.studies_id == study.studies_id, study_internship))
            # imo we should take into account how many concflict each user has with courses meetings and if its over some treshold don't add him
            users_by_collisions = []
            for user in  users:
                users_course_ids = []
                user_study_ids = []
                for i, course_list in enumerate(course_enrolled):
                    if user.user_id in course_list:
                        users_course_ids.append(i)
                for i, study_list in enumerate(study_enrolled):
                    if user.user_id in study_list:
                        user_study_ids.append(i)
                
                user_collisions = 0
                for other_meeting in filter(lambda x: x.course_id in users_course_ids , course_meetings):
                    for s in current_study_meetings:
                        if other_meeting.meeting_date == s.meeting_date:
                            user_collisions += 1
                    for i in current_study_internships:
                        if other_meeting.meeting_date == i.meeting_date:
                            user_collisions += 1
                for other_meeting in filter(lambda x: x in user_study_ids , study_meetings):
                    for s in current_study_meetings:
                        if other_meeting.meeting_date == s.meeting_date:
                            user_collisions += 1
                    for i in current_study_internships:
                        if other_meeting.meeting_date == i.meeting_date:
                            user_collisions += 1
                users_by_collisions.append((user_collisions, user.user_id))
            random.shuffle(users_by_collisions)
            users_by_collisions.sort(key=lambda x: x[0])

            # edit this so not every course is fully booked
            for i in range(study.students_limit): 
                study_enrolled[s_id].append(users_by_collisions[i][1])

    def generate_orders_from_studies_enrolled(studies_enrolled, studies):
        for i, enrolled_users in enumerate(studies_enrolled):
            current_study = studies[i]
            study_start_date = datetime.datetime.fromisoformat(current_study.start_date)
            study_pay_before_Date = study_start_date + datetime.timedelta(14)

            for user_id in enrolled_users:
                tmp_order = db_model.Order(len(orders), user_id=user_id, is_paid=1, max_paid_date=study_pay_before_Date)
                tmp_order_detail = db_model.OrderDetail(len(order_details), tmp_order.order_id, 2, studies[i].price)
                tmp_order_study = db_model.OrderStudy(tmp_order_detail.order_detail_id, i)

                orders.append(tmp_order)
                order_details.append(tmp_order_detail)
                order_studies.append(tmp_order_study)


    def generate_study_meetings_attendance_list_of_enrolled_students():
        pass


    generate_enrolled_lists_for_courses(courses, course_meetings, users)
    generate_enrolled_lists_for_studies(courses, course_meetings, users, studies, study_meetings, study_internships)
    generate_orders_from_course_enrolled(course_enrolled, courses)
    generate_orders_from_studies_enrolled(study_enrolled, studies)

    return orders, order_details, order_course, order_studies

def main():
    users = u_gen.generate_users_table()
    employees, translators, translators_languages = emp_gen.generate_employees_table()
    webinars = w_gen.webinars_generator(employees)
    courses, course_modules, course_module_meetings, stationary_meetings, sync_async_meetings = c_gen.generate_courses(webinars, employees, translators, translators_languages)

    studies, study_modules, study_module_meetings, study_internships,  study_stationary_meetings, study_sync_async_meetings = s_gen.generate_studies(webinars, course_module_meetings, employees, translators, translators_languages)
    # generate_enrolled_lists_for_courses(courses, course_module_meetings, users)

    # print(course_enrolled)

    # generate_orders_from_course_enrolled(course_enrolled, courses)

    # generate_enrolled_lists_for_studies(courses, course_module_meetings, users, studies, study_module_meetings, study_internships)

    # generate_orders_from_studies_enrolled(study_enrolled, studies)

    # print(study_enrolled)

    # for o in orders:
    #     print(o)
    #     detail = list(filter(lambda x: x.order_id == o.order_id, order_details))
    #     for d in detail:
    #         print("    " + str(d))

    generate_orders(users)

if __name__ == "__main__":
    main()
