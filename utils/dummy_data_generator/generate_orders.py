import db_tables_classes as db_model
from faker import Faker
import datetime
import random
import employees_generation as emp_gen
import webinars_generation as w_gen
from typing import List
import users_generation as u_gen
import courses_generation as c_gen
import studies_generator as s_gen
import datetime
fk = Faker()

def generate_orders(courses, course_meetings, users, studies, study_meetings, study_internships, webinars):
    course_enrolled = []
    study_enrolled = []
    orders = []
    order_details = []
    order_webinars = []
    order_course = []
    order_module_studies = []
    order_studies = []
    course_meetings_attendance_list = []
    study_meetings_attendance_list = []
    study_internships_attendance_list = []
    egzams_grades = []

    def generate_webinars_orders():
        for w_id, webinar in enumerate(webinars):
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
                    if(webinar.start_date == other_meeting.meeting_date):
                        user_collisions += 1
                for other_meeting in filter(lambda x: x in user_study_ids , study_meetings):
                   if(webinar.webinar_date == other_meeting.meeting_date):
                        user_collisions += 1
                users_by_collisions.append((user_collisions, user.user_id))
            random.shuffle(users_by_collisions)
            users_by_collisions.sort(key=lambda x: x[0])

            # edit this so not every course is fully booked
            for i in range(random.randint(5,50)) :
                orders.append(db_model.Order(len(orders)+1, user_id=users_by_collisions[i][1], is_paid=1, max_paid_date=webinar.start_date))
                order_details.append(db_model.OrderDetail(len(order_details)+1, len(orders), 1, 0))
                order_webinars.append(db_model.OrderWebinar(len(order_details), w_id))

    
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
            course_start_date = (current_course.start_date)
            course_pay_before_Date = course_start_date + datetime.timedelta(14)

            for user_id in enrolled_users:
                tmp_order = db_model.Order(len(orders)+1, user_id=user_id, is_paid=1, max_paid_date=course_pay_before_Date)
                tmp_order_detail = db_model.OrderDetail(len(order_details)+1, tmp_order.order_id, 2, courses[i].price)
                tmp_order_course = db_model.OrderCourse(tmp_order_detail.order_detail_id, i+1)

                orders.append(tmp_order)
                order_details.append(tmp_order_detail)
                order_course.append(tmp_order_course)


    def generate_course_meetings_attendance_list_of_enrolled_students():
        for i, enrolled_users in enumerate(course_enrolled):
            current_course = courses[i]

            m:db_model.CourseModuleMeetings
            for m in filter(lambda x: x.course_id == current_course.course_id  ,course_meetings):
                for user in enrolled_users:
                    course_meetings_attendance_list.append(db_model.CourseMeetingAttendanceList(user, current_course.course_id, m.meeting_id, 1))

    def generate_study_meetings_attendance_list_of_enrolled_students():
        for i, enrolled_users in enumerate(study_enrolled):
            current_Study = studies[i]

            m:db_model.StudyModuleMeeting
            for m in filter(lambda x: x.studies_id == current_Study.studies_id  , study_meetings):
                for user in enrolled_users:
                    study_meetings_attendance_list.append(db_model.StudyMeetingAttendanceList(user, current_Study.studies_id, m.meeting_id, 1, 0))

    def generate_internship_attendance_list_of_enrolled_students():
        for i, enrolled_users in enumerate(study_enrolled):
            current_Study = studies[i]

            m:db_model.InternshipMeetingAttendanceList
            for m in filter(lambda x: x.studies_id == current_Study.studies_id  , study_internships):
                for user in enrolled_users:
                    study_internships_attendance_list.append(db_model.InternshipMeetingAttendanceList(m.inter_meeting_id, current_Study.studies_id, user, 1))

    def generate_egzams_grades_of_enrolled_students():
        for i, enrolled_users in enumerate(study_enrolled):
            current_Study = studies[i]

            m:db_model.Egzam   
            for user in enrolled_users:
                grade = random.randint(0,100)
                if(grade < 10):
                    grade = 2
                elif(grade < 50):
                    grade = 3
                elif(grade < 90):
                    grade = 4
                else:
                    grade = 5
                egzams_grades.append(db_model.Exam(current_Study.studies_id, user, grade))

    def generate_missed_classes():
        for attendance in course_meetings_attendance_list:
            if random.randint(0, 100) < 10:
                attendance.was_present = 0
        for attendance in study_meetings_attendance_list:
            if random.randint(0, 100) < 10:
                attendance.was_present = 0
                    

    def generate_signgle_module_orders_studies():
        for study in studies:
            for m in  list(filter(lambda x: x.studies_id == study.studies_id, study_meetings)):
                for u in list(filter(lambda x: x.user_id not in study_enrolled[study.studies_id - 1], users)):
                    if(random.randint(0,1000) < 10):
                        orders.append(db_model.Order(len(orders)+1, user_id=u.user_id, is_paid=1, max_paid_date=m.meeting_date))
                        order_details.append(db_model.OrderDetail(len(order_details)+1, len(orders), 4, study.price))
                        order_module_studies.append(db_model.OrderModuleStudy(len(order_details), study.studies_id))



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
            study_start_date = (current_study.start_date)
            study_pay_before_Date = study_start_date + datetime.timedelta(14)

            for user_id in enrolled_users:
                tmp_order = db_model.Order(len(orders)+1, user_id=user_id, is_paid=1, max_paid_date=study_pay_before_Date)
                tmp_order_detail = db_model.OrderDetail(len(order_details)+1, tmp_order.order_id, 3, studies[i].price)
                tmp_order_study = db_model.OrderStudy(tmp_order_detail.order_detail_id, i+1)

                orders.append(tmp_order)
                order_details.append(tmp_order_detail)
                order_studies.append(tmp_order_study)


   

    generate_enrolled_lists_for_courses(courses, course_meetings, users)
    generate_enrolled_lists_for_studies(courses, course_meetings, users, studies, study_meetings, study_internships)
    generate_orders_from_course_enrolled(course_enrolled, courses)
    generate_orders_from_studies_enrolled(study_enrolled, studies)
    generate_webinars_orders()
    generate_signgle_module_orders_studies()
    generate_course_meetings_attendance_list_of_enrolled_students()
    generate_study_meetings_attendance_list_of_enrolled_students()
    generate_internship_attendance_list_of_enrolled_students()
    generate_missed_classes()
    generate_egzams_grades_of_enrolled_students()

    return orders, order_details, order_course, order_studies, course_meetings_attendance_list, study_meetings_attendance_list, study_internships_attendance_list, egzams_grades, order_webinars, order_module_studies

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
