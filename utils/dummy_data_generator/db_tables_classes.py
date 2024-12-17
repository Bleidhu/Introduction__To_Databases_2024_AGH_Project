class City:
    def __init__(self, city_id, city_name):
        self.city_id = city_id
        self.city_name = city_name

    def __str__(self):
        return f"{self.city_id}, {self.city_name}"


class Country:
    def __init__(self, country_id, country_name):
        self.country_id = country_id
        self.country_name = country_name

    def __str__(self):
        return f"{self.country_id}, {self.country_name}"


class CourseMeetingAttendanceList:
    def __init__(self, user_id, course_id, meeting_id, was_present):
        self.user_id = user_id
        self.course_id = course_id
        self.meeting_id = meeting_id
        self.was_present = was_present

    def __str__(self):
        return f"{self.user_id}, {self.course_id}, {self.meeting_id}, {self.was_present}"


class CourseModuleMeetingStationary:
    def __init__(self, id, course_id, meeting_id, classroom):
        self.id = id
        self.course_id = course_id
        self.meeting_id = meeting_id
        self.classroom = classroom

    def __str__(self):
        return f"{self.id}, {self.course_id}, {self.meeting_id}, {self.classroom}"


class CourseModuleMeetings:
    def __init__(self, course_id, meeting_id, meeting_date, language_id, translator_id, lecturer_id, duration, place_limit, module_id, meeting_type_id, meeting_name):
        self.course_id = course_id
        self.meeting_id = meeting_id
        self.meeting_date = meeting_date
        self.language_id = language_id
        self.translator_id = translator_id
        self.lecturer_id = lecturer_id
        self.duration = duration
        self.place_limit = place_limit
        self.module_id = module_id
        self.meeting_type_id = meeting_type_id
        self.meeting_name = meeting_name

    def __str__(self):
        return f"{self.course_id}, {self.meeting_id}, {self.meeting_date}, {self.language_id}, {self.translator_id}, {self.lecturer_id}, {self.duration}, {self.place_limit}, {self.module_id}, {self.meeting_type_id}, {self.meeting_name}"


class CourseModules:
    def __init__(self, module_id, module_type_id, module_name, course_id):
        self.module_id = module_id
        self.module_type_id = module_type_id
        self.module_name = module_name
        self.course_id = course_id

    def __str__(self):
        return f"{self.module_id}, {self.module_type_id}, {self.module_name}, {self.course_id}"


class CourseSyncAsyncMeeting:
    def __init__(self, id, course_id, meeting_id, accessTo, video_link, stream_link):
        self.id = id
        self.course_id = course_id
        self.meeting_id = meeting_id
        self.accessTo = accessTo
        self.video_link = video_link
        self.stream_link = stream_link

    def __str__(self):
        return f"{self.id}, {self.course_id}, {self.meeting_id}, {self.accessTo}, {self.video_link}, {self.stream_link}"


class Course:
    def __init__(self, course_id, course_name, course_description, start_date, students_limit, price, course_coordinator_id, visible_from):
        self.course_id = course_id
        self.course_name = course_name
        self.course_description = course_description
        self.start_date = start_date
        self.students_limit = students_limit
        self.price = price
        self.course_coordinator_id = course_coordinator_id
        self.visible_from = visible_from

    def __str__(self):
        return f"{self.course_id}, {self.course_name}, {self.course_description}, {self.start_date}, {self.students_limit}, {self.price}, {self.course_coordinator_id}, {self.visible_from}"


class EmployeeRole:
    def __init__(self, role_id, employee_id, role_name):
        self.role_id = role_id
        self.employee_id = employee_id
        self.role_name = role_name

    def __str__(self):
        return f"{self.role_id}, {self.employee_id}, {self.role_name}"


class Employee:
    def __init__(self, employee_id, first_name, last_name, hire_date, birth_date, phone, email, role_id, city_id, country_id):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.phone = phone
        self.email = email
        self.role_id = role_id
        self.city_id = city_id
        self.country_id = country_id

    def __str__(self):
        return f"{self.employee_id}, {self.first_name}, {self.last_name}, {self.hire_date}, {self.birth_date}, {self.phone}, {self.email}, {self.role_id}, {self.city_id}, {self.country_id}"


class EventType:
    def __init__(self, type_id, event_name):
        self.type_id = type_id
        self.event_name = event_name

    def __str__(self):
        return f"{self.type_id}, {self.event_name}"


class Exam:
    def __init__(self, studies_id, user_id, grade):
        self.studies_id = studies_id
        self.user_id = user_id
        self.grade = grade

    def __str__(self):
        return f"{self.studies_id}, {self.user_id}, {self.grade}"


class InternshipMeetingAttendanceList:
    def __init__(self, inter_meeting_id, user_id, was_present):
        self.inter_meeting_id = inter_meeting_id
        self.user_id = user_id
        self.was_present = was_present

    def __str__(self):
        return f"{self.inter_meeting_id}, {self.user_id}, {self.was_present}"


class InternshipMeeting:
    def __init__(self, inter_meeting_id, studies_id, internship_id, meeting_date):
        self.inter_meeting_id = inter_meeting_id
        self.studies_id = studies_id
        self.internship_id = internship_id
        self.meeting_date = meeting_date

    def __str__(self):
        return f"{self.inter_meeting_id}, {self.studies_id}, {self.internship_id}, {self.meeting_date}"


class Language:
    def __init__(self, language_id, language_name):
        self.language_id = language_id
        self.language_name = language_name

    def __str__(self):
        return f"{self.language_id}, {self.language_name}"


class OrderCourse:
    def __init__(self, order_detail_id, course_id):
        self.order_detail_id = order_detail_id
        self.course_id = course_id

    def __str__(self):
        return f"{self.order_detail_id}, {self.course_id}"


class OrderDetail:
    def __init__(self, order_detail_id, order_id, type_id):
        self.order_detail_id = order_detail_id
        self.order_id = order_id
        self.type_id = type_id

    def __str__(self):
        return f"{self.order_detail_id}, {self.order_id}, {self.type_id}"


class OrderModuleStudy:
    def __init__(self, order_detail_id, module_id):
        self.order_detail_id = order_detail_id
        self.module_id = module_id

    def __str__(self):
        return f"{self.order_detail_id}, {self.module_id}"


class OrderStudy:
    def __init__(self, order_detail_id, studies_id):
        self.order_detail_id = order_detail_id
        self.studies_id = studies_id

    def __str__(self):
        return f"{self.order_detail_id}, {self.studies_id}"


class OrderWebinar:
    def __init__(self, order_detail_id, webinar_id):
        self.order_detail_id = order_detail_id
        self.webinar_id = webinar_id

    def __str__(self):
        return f"{self.order_detail_id}, {self.webinar_id}"


class Order:
    def __init__(self, order_id, user_id, is_paid, price, max_paid_date):
        self.order_id = order_id
        self.user_id = user_id
        self.is_paid = is_paid
        self.price = price
        self.max_paid_date = max_paid_date

    def __str__(self):
        return f"{self.order_id}, {self.user_id}, {self.is_paid}, {self.price}, {self.max_paid_date}"


class Study:
    def __init__(self, studies_id, studies_name, studies_description, start_date, students_limit, price, studies_coordinator_id, visible_from):
        self.studies_id = studies_id
        self.studies_name = studies_name
        self.studies_description = studies_description
        self.start_date = start_date
        self.students_limit = students_limit
        self.price = price
        self.studies_coordinator_id = studies_coordinator_id
        self.visible_from = visible_from

    def __str__(self):
        return f"{self.studies_id}, {self.studies_name}, {self.studies_description}, {self.start_date}, {self.students_limit}, {self.price}, {self.studies_coordinator_id}, {self.visible_from}"


class StudyModule:
    def __init__(self, module_id, module_type_id, module_name, studies_id, price_for_free_listeners):
        self.module_id = module_id
        self.module_type_id = module_type_id
        self.module_name = module_name
        self.studies_id = studies_id
        self.price_for_free_listeners = price_for_free_listeners

    def __str__(self):
        return f"{self.module_id}, {self.module_type_id}, {self.module_name}, {self.studies_id}, {self.price_for_free_listeners}"


class StudyMakeupMeetingAttendanceList:
    def __init__(self, makeup_list_id, user_id, studies_id, meeting_id, topic_id):
        self.makeup_list_id = makeup_list_id
        self.user_id = user_id
        self.studies_id = studies_id
        self.meeting_id = meeting_id
        self.topic_id = topic_id

    def __str__(self):
        return f"{self.makeup_list_id}, {self.user_id}, {self.studies_id}, {self.meeting_id}, {self.topic_id}"


class StudyMeetingAttendanceList:
    def __init__(self, user_id, studies_id, meeting_id, was_present, topic_id):
        self.user_id = user_id
        self.studies_id = studies_id
        self.meeting_id = meeting_id
        self.was_present = was_present
        self.topic_id = topic_id

    def __str__(self):
        return f"{self.user_id}, {self.studies_id}, {self.meeting_id}, {self.was_present}, {self.topic_id}"


class StudyModuleMeetingStationary:
    def __init__(self, id, studies_id, meeting_id, classroom):
        self.id = id
        self.studies_id = studies_id
        self.meeting_id = meeting_id
        self.classroom = classroom

    def __str__(self):
        return f"{self.id}, {self.studies_id}, {self.meeting_id}, {self.classroom}"


class StudyModuleMeeting:
    def __init__(self, meeting_id, studies_id, meeting_date, language_id, translator_id, lecturer_id, duration, place_limit, module_id, topic_id, meeting_name):
        self.meeting_id = meeting_id
        self.studies_id = studies_id
        self.meeting_date = meeting_date
        self.language_id = language_id
        self.translator_id = translator_id
        self.lecturer_id = lecturer_id
        self.duration = duration
        self.place_limit = place_limit
        self.module_id = module_id
        self.topic_id = topic_id
        self.meeting_name = meeting_name

    def __str__(self):
        return f"{self.meeting_id}, {self.studies_id}, {self.meeting_date}, {self.language_id}, {self.translator_id}, {self.lecturer_id}, {self.duration}, {self.place_limit}, {self.module_id}, {self.topic_id}, {self.meeting_name}"


class StudyModule:
    def __init__(self, module_id, module_type_id, module_name, studies_id, price_for_free_listeners):
        self.module_id = module_id
        self.module_type_id = module_type_id
        self.module_name = module_name
        self.studies_id = studies_id
        self.price_for_free_listeners = price_for_free_listeners

    def __str__(self):
        return f"{self.module_id}, {self.module_type_id}, {self.module_name}, {self.studies_id}, {self.price_for_free_listeners}"


class StudyType:
    def __init__(self, study_type_id, study_type_name):
        self.study_type_id = study_type_id
        self.study_type_name = study_type_name

    def __str__(self):
        return f"{self.study_type_id}, {self.study_type_name}"


class User:
    def __init__(self, user_id, user_name, email, phone, city_id, country_id):
        self.user_id = user_id
        self.user_name = user_name
        self.email = email
        self.phone = phone
        self.city_id = city_id
        self.country_id = country_id

    def __str__(self):
        return f"{self.user_id}, {self.user_name}, {self.email}, {self.phone}, {self.city_id}, {self.country_id}"


class Webinar:
    def __init__(self, webinar_id, webinar_name, webinar_description, teacher_id, price, can_buy_from, recording_link, start_date):
        self.webinar_id = webinar_id
        self.webinar_name = webinar_name
        self.webinar_description = webinar_description
        self.teacher_id = teacher_id
        self.price = price
        self.can_buy_from = can_buy_from
        self.recording_link = recording_link
        self.start_date = start_date

    def __str__(self):
        return f"{self.webinar_id}, {self.webinar_name}, {self.webinar_description}, {self.teacher_id}, {self.price}, {self.can_buy_from}, {self.recording_link}, {self.start_date}"
    
    
class Translator:
    def __init__(self, translator_id, employee_id):
        self.translator_id = translator_id
        self.employee_id = employee_id

    def __str__(self):
        return f"{self.translator_id}, {self.first_name}, {self.last_name}, {self.email}, {self.phone}, {self.language_id}"