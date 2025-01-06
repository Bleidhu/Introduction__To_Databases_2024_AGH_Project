from db_tables_classes import *
from typing import List
def get_employees_not_working_on_date(employees: List[Employee],date, course_meetings_table: List[CourseModuleMeetings]=[], 
                                      webinars_meetings: List[Webinar]=[], studies_meetings: List[StudyModuleMeeting]=[]) -> List[Employee]:

    emp = []
    for e in employees:
        check = True

        if(any(e.employee_id == meeting.lecturer_id and meeting.meeting_date == date for meeting in course_meetings_table)):
            check = False
        if(any(e.employee_id == meeting.teacher_id and meeting.start_date == date for meeting in webinars_meetings)):
            check = False
        if(any(e.employee_id == meeting.lecturer_id and meeting.meeting_date == date for meeting in studies_meetings)):
            check = False
        
        if(check):
             emp.append(e)
    return emp
    
def get_employees_hired_after_date(employees: List[Employee], date) -> List[Employee]:
    emp = []
    for e in employees:

        if(e.hire_date < date):
             emp.append(e)
    return emp

# def get_rooms_of_given_size(size, rooms):
#     rooms = list(filter())
# def get_rooms_free_date(date, course_meetings_tabble: List[CourseModuleMeetings]=[], studies_meetings: List[StudyModuleMeeting]=[]):
