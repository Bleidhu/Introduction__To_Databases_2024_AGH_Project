class City:
    def __init__(self, city_id: int, city_name: str):
        self.city_id = city_id
        self.city_name = city_name

    def __str__(self):
        return f"{self.city_id}, {self.city_name}"


class Country:
    def __init__(self, country_id: int, country_name: str):
        self.country_id = country_id
        self.country_name = country_name

    def __str__(self):
        return f"{self.country_id}, {self.country_name}"


class CourseEnrolledStudent:
    def __init__(self, course_id: int, user_id: int, is_paid: bool, order_id: int):
        self.course_id = course_id
        self.user_id = user_id
        self.is_paid = is_paid
        self.order_id = order_id

    def __str__(self):
        return f"{self.course_id}, {self.user_id}, {self.is_paid}, {self.order_id}"


class CourseMeetingAttendance:
    def __init__(self, user_id: int, course_id: int, meeting_id: int, was_present: bool):
        self.user_id = user_id
        self.course_id = course_id
        self.meeting_id = meeting_id
        self.was_present = was_present

    def __str__(self):
        return f"{self.user_id}, {self.course_id}, {self.meeting_id}, {self.was_present}"


class CourseModule:
    def __init__(self, course_id: int, meeting_id: int, module_type: str):
        self.course_id = course_id
        self.meeting_id = meeting_id
        self.module_type = module_type

    def __str__(self):
        return f"{self.course_id}, {self.meeting_id}, {self.module_type}"


class CourseModuleMeetingStationary:
    def __init__(self, id: int, course_id: int, meeting_id: int, classroom: int):
        self.id = id
        self.course_id = course_id
        self.meeting_id = meeting_id
        self.classroom = classroom

    def __str__(self):
        return f"{self.id}, {self.course_id}, {self.meeting_id}, {self.classroom}"


class CourseModuleMeeting:
    def __init__(self, course_id: int, meeting_id: int, meeting_date: str, meeting_type: str, 
                 language_id: str, translator_id: int, lecturer_id: int, duration: str, place_limit: int):
        self.course_id = course_id
        self.meeting_id = meeting_id
        self.meeting_date = meeting_date
        self.meeting_type = meeting_type
        self.language_id = language_id
        self.translator_id = translator_id
        self.lecturer_id = lecturer_id
        self.duration = duration
        self.place_limit = place_limit

    def __str__(self):
        return f"{self.course_id}, {self.meeting_id}, {self.meeting_date}, {self.meeting_type}, {self.language_id}, {self.translator_id}, {self.lecturer_id}, {self.duration}, {self.place_limit}"


class CourseSyncAsyncMeeting:
    def __init__(self, id: int, course_id: int, meeting_id: int, access_to: str, video_link: str, stream_link: str = None):
        self.id = id
        self.course_id = course_id
        self.meeting_id = meeting_id
        self.access_to = access_to
        self.video_link = video_link
        self.stream_link = stream_link

    def __str__(self):
        return f"{self.id}, {self.course_id}, {self.meeting_id}, {self.access_to}, {self.video_link}, {self.stream_link}"


class Course:
    def __init__(self, course_id: int, course_name: str, course_description: str, start_date: str, 
                 students_limit: int, price: float, course_coordinator_id: int):
        self.course_id = course_id
        self.course_name = course_name
        self.course_description = course_description
        self.start_date = start_date
        self.students_limit = students_limit
        self.price = price
        self.course_coordinator_id = course_coordinator_id

    def __str__(self):
        return f"{self.course_id}, {self.course_name}, {self.course_description}, {self.start_date}, {self.students_limit}, {self.price}, {self.course_coordinator_id}"


class EmployeeRole:
    def __init__(self, role_id: int, employee_id: int, role_name: str):
        self.role_id = role_id
        self.employee_id = employee_id
        self.role_name = role_name

    def __str__(self):
        return f"{self.role_id}, {self.employee_id}, {self.role_name}"


class Employee:
    def __init__(self, employee_id: int, first_name: str, last_name: str, hire_date: str, birth_date: str, 
                 phone: int, email: str, role_id: int, city_id: int, country_id: int):
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
    def __init__(self, type_id: int, event_name: str):
        self.type_id = type_id
        self.event_name = event_name

    def __str__(self):
        return f"{self.type_id}, {self.event_name}"


class InternshipMeetingAttendance:
    def __init__(self, inter_meeting_id: int, user_id: int, was_present: bool):
        self.inter_meeting_id = inter_meeting_id
        self.user_id = user_id
        self.was_present = was_present

    def __str__(self):
        return f"{self.inter_meeting_id}, {self.user_id}, {self.was_present}"


class InternshipMeeting:
    def __init__(self, inter_meeting_id: int, studies_id: int, internship_id: int, meeting_date: str):
        self.inter_meeting_id = inter_meeting_id
        self.studies_id = studies_id
        self.internship_id = internship_id
        self.meeting_date = meeting_date

    def __str__(self):
        return f"{self.inter_meeting_id}, {self.studies_id}, {self.internship_id}, {self.meeting_date}"


class Language:
    def __init__(self, language_id: str, language_name: str):
        self.language_id = language_id
        self.language_name = language_name

    def __str__(self):
        return f"{self.language_id}, {self.language_name}"


class OrderCourse:
    def __init__(self, order_detail_id: int, course_id: int):
        self.order_detail_id = order_detail_id
        self.course_id = course_id

    def __str__(self):
        return f"{self.order_detail_id}, {self.course_id}"


class OrderDetail:
    def __init__(self, order_detail_id: int, order_id: int, type_id: int):
        self.order_detail_id = order_detail_id
        self.order_id = order_id
        self.type_id = type_id

    def __str__(self):
        return f"{self.order_detail_id}, {self.order_id}, {self.type_id}"


class OrderMeetingStudy:
    def __init__(self, order_detail_id: int, studies_id: int, meeting_id: int):
        self.order_detail_id = order_detail_id
        self.studies_id = studies_id
        self.meeting_id = meeting_id

    def __str__(self):
        return f"{self.order_detail_id}, {self.studies_id}, {self.meeting_id}"


class OrderStudy:
    def __init__(self, order_detail_id: int, studies_id: int):
        self.order_detail_id = order_detail_id
        self.studies_id = studies_id

    def __str__(self):
        return f"{self.order_detail_id}, {self.studies_id}"


class OrderWebinar:
    def __init__(self, order_detail_id: int, webinar_id: int):
        self.order_detail_id = order_detail_id
        self.webinar_id = webinar_id

    def __str__(self):
        return f"{self.order_detail_id}, {self.webinar_id}"


class Order:
    def __init__(self, order_id: int, user_id: int, is_paid: bool, price: float):
        self.order_id = order_id
        self.user_id = user_id
        self.is_paid = is_paid
        self.price = price

    def __str__(self):
        return f"{self.order_id}, {self.user_id}, {self.is_paid}, {self.price}"


class Study:
    def __init__(self, studies_id: int, studies_name: str, studies_description: str, start_date: str, 
                 students_limit: int, price: float, studies_coordinator_id: int):
        self.studies_id = studies_id
        self.studies_name = studies_name
        self.studies_description = studies_description
        self.start_date = start_date
        self.students_limit = students_limit
        self.price = price
        self.studies_coordinator_id = studies_coordinator_id

    def __str__(self):
        return f"{self.studies_id}, {self.studies_name}, {self.studies_description}, {self.start_date}, {self.students_limit}, {self.price}, {self.studies_coordinator_id}"


class StudyEnrolledStudent:
    def __init__(self, studies_id: int, user_id: int, only_meeting: bool, order_id: int):
        self.studies_id = studies_id
        self.user_id = user_id
        self.only_meeting = only_meeting
        self.order_id = order_id

    def __str__(self):
        return f"{self.studies_id}, {self.user_id}, {self.only_meeting}, {self.order_id}"


class StudyMeetingAttendance:
    def __init__(self, user_id: int, studies_id: int, meeting_id: int, was_present: bool):
        self.user_id = user_id
        self.studies_id = studies_id
        self.meeting_id = meeting_id
        self.was_present = was_present

    def __str__(self):
        return f"{self.user_id}, {self.studies_id}, {self.meeting_id}, {self.was_present}"


class StudyModule:
    def __init__(self, studies_id: int, meeting_id: int, module_type: str):
        self.studies_id = studies_id
        self.meeting_id = meeting_id
        self.module_type = module_type

    def __str__(self):
        return f"{self.studies_id}, {self.meeting_id}, {self.module_type}"


class StudyModuleMeetingStationary:
    def __init__(self, id: int, studies_id: int, meeting_id: int, classroom: int):
        self.id = id
        self.studies_id = studies_id
        self.meeting_id = meeting_id
        self.classroom = classroom

    def __str__(self):
        return f"{self.id}, {self.studies_id}, {self.meeting_id}, {self.classroom}"


class StudyModuleMeeting:
    def __init__(self, meeting_id: int, studies_id: int, meeting_date: str, meeting_type: str, 
                 language_id: str, translator_id: int, lecturer_id: int, duration: str, 
                 place_limit: int, price_for_free_listener: float):
        self.meeting_id = meeting_id
        self.studies_id = studies_id
        self.meeting_date = meeting_date
        self.meeting_type = meeting_type
        self.language_id = language_id
        self.translator_id = translator_id
        self.lecturer_id = lecturer_id
        self.duration = duration
        self.place_limit = place_limit
        self.price_for_free_listener = price_for_free_listener

    def __str__(self):
        return f"{self.meeting_id}, {self.studies_id}, {self.meeting_date}, {self.meeting_type}, {self.language_id}, {self.translator_id}, {self.lecturer_id}, {self.duration}, {self.place_limit}, {self.price_for_free_listener}"


class StudySyncAsyncMeeting:
    def __init__(self, id: int, studies_id: int, meeting_id: int, access_to: str, video_link: str, 
                 stream_link: str):
        self.id = id
        self.studies_id = studies_id
        self.meeting_id = meeting_id
        self.access_to = access_to
        self.video_link = video_link
        self.stream_link = stream_link

    def __str__(self):
        return f"{self.id}, {self.studies_id}, {self.meeting_id}, {self.access_to}, {self.video_link}, {self.stream_link}"


class Translator:
    def __init__(self, translator_id: int, employee_id: int):
        self.translator_id = translator_id
        self.employee_id = employee_id

    def __str__(self):
        return f"{self.translator_id}, {self.employee_id}"


class TranslatorLanguageUsed:
    def __init__(self, id: int, translator_id: int, language_id: str):
        self.id = id
        self.translator_id = translator_id
        self.language_id = language_id

    def __str__(self):
        return f"{self.id}, {self.translator_id}, {self.language_id}"


class User:
    def __init__(self, user_id: int, email: str, first_name: str, last_name: str, city_id: int, 
                 country_id: int):
        self.user_id = user_id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.city_id = city_id
        self.country_id = country_id

    def __str__(self):
        return f"{self.user_id}, {self.email}, {self.first_name}, {self.last_name}, {self.city_id}, {self.country_id}"


class Webinar:
    def __init__(self, webinar_id: int, course_id: int, studies_id: int, language_id: str, 
                 duration: str, presenter_id: int):
        self.webinar_id = webinar_id
        self.course_id = course_id
        self.studies_id = studies_id
        self.language_id = language_id
        self.duration = duration
        self.presenter_id = presenter_id

    def __str__(self):
        return f"{self.webinar_id}, {self.course_id}, {self.studies_id}, {self.language_id}, {self.duration}, {self.presenter_id}"
