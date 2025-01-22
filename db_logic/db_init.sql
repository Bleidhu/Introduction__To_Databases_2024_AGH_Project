-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2025-01-08 13:11:49.547

-- tables
-- Table: Cities
CREATE TABLE Cities (
                        city_id int  NOT NULL IDENTITY(1, 1),
                        city_name nvarchar(30)  NOT NULL,
                        CONSTRAINT Cities_pk PRIMARY KEY  (city_id)
);

-- Table: Countries
CREATE TABLE Countries (
                           country_id int  NOT NULL IDENTITY(1, 1),
                           country_name nvarchar(30)  NOT NULL,
                           CONSTRAINT Countries_pk PRIMARY KEY  (country_id)
);

-- Table: Course_meeting_attendance_list
CREATE TABLE Course_meeting_attendance_list (
                                                user_id int  NOT NULL,
                                                course_id int  NOT NULL,
                                                meeting_id int  NOT NULL,
                                                was_present bit  NOT NULL,
                                                CONSTRAINT Course_meeting_attendance_list_pk PRIMARY KEY  (user_id,meeting_id,course_id)
);

-- Table: Course_module_meetings
CREATE TABLE Course_module_meetings (
                                        course_id int  NOT NULL,
                                        meeting_id int  NOT NULL,
                                        meeting_date datetime  NOT NULL,
                                        language_id int  NOT NULL,
                                        translator_id int  NOT NULL,
                                        lecturer_id int  NOT NULL,
                                        duration time  NOT NULL,
                                        place_limit int  NOT NULL,
                                        module_id int  NOT NULL,
                                        meeting_type_id int  NOT NULL,
                                        meeting_name nvarchar(30)  NOT NULL,
                                        CONSTRAINT place_limit CHECK (place_limit >= 0),
                                        CONSTRAINT Course_module_meetings_pk PRIMARY KEY  (meeting_id,course_id)
);

-- Table: Course_modules
CREATE TABLE Course_modules (
                                course_module_id int  NOT NULL IDENTITY(1, 1),
                                module_type_id int  NOT NULL,
                                module_name nvarchar(30)  NOT NULL,
                                course_id int  NOT NULL,
                                CONSTRAINT course_module_id PRIMARY KEY  (course_module_id)
);

-- Table: Course_stationary_meeting
CREATE TABLE Course_stationary_meeting (
                                           id int  NOT NULL IDENTITY(1, 1),
                                           course_id int  NOT NULL,
                                           meeting_id int  NOT NULL,
                                           classroom nvarchar(10)  NOT NULL,
                                           CONSTRAINT Course_stationary_meeting_pk PRIMARY KEY  (id)
);

-- Table: Course_sync_async_meeting
CREATE TABLE Course_sync_async_meeting (
                                           id int  NOT NULL IDENTITY(1, 1),
                                           course_id int  NOT NULL,
                                           meeting_id int  NOT NULL,
                                           access_to datetime  NOT NULL,
                                           video_link nvarchar(30)  NOT NULL,
                                           stream_link nvarchar(30)  NULL,
                                           CONSTRAINT Course_sync_async_meeting_pk PRIMARY KEY  (id)
);

-- Table: Courses
CREATE TABLE Courses (
                         course_id int  NOT NULL IDENTITY(1, 1),
                         course_name nvarchar(30)  NOT NULL,
                         course_description nvarchar(300)  NOT NULL,
                         start_date date  NOT NULL,
                         students_limit int  NOT NULL,
                         price money  NOT NULL,
                         course_coordinator_id int  NOT NULL,
                         visible_from date  NOT NULL,
                         CONSTRAINT courses_price_check CHECK (price >= 0),
                         CONSTRAINT Courses_pk PRIMARY KEY  (course_id)
);

-- Table: Employee_Roles
CREATE TABLE Employee_Roles (
                                role_id int  NOT NULL IDENTITY(1, 1),
                                role_name nvarchar(30)  NOT NULL,
                                CONSTRAINT Employee_Roles_pk PRIMARY KEY  (role_id)
);

-- Table: Employees
CREATE TABLE Employees (
                           employee_id int  NOT NULL IDENTITY(1, 1),
                           first_name nvarchar(30)  NOT NULL,
                           last_name nvarchar(30)  NOT NULL,
                           hire_date date  NOT NULL,
                           birth_date date  NOT NULL,
                           phone nvarchar(9)  NOT NULL CHECK ((PATINDEX('%[^0-9]%', phone) = 0 AND LEN(phone) = 9)),
                           email nvarchar(50)  NOT NULL,
                           role_id int  NOT NULL,
                           city_id int  NOT NULL,
                           country_id int  NOT NULL,
                           CONSTRAINT employee_birth_date_check CHECK (year(getdate())-year(birth_date)<100),
                           CONSTRAINT Employees_pk PRIMARY KEY  (employee_id)
);

-- Table: Event_types
CREATE TABLE Event_types (
                             type_id int  NOT NULL IDENTITY(1, 1),
                             event_name nvarchar(30)  NOT NULL,
                             CONSTRAINT Event_types_pk PRIMARY KEY  (type_id)
);

-- Table: Exams
CREATE TABLE Exams (
                       studies_id int  NOT NULL,
                       user_id int  NOT NULL,
                       grade numeric(2,1)  NOT NULL,
                       CONSTRAINT grade_check CHECK (grade in (2.0, 3.0, 3.5, 4.0, 4.5, 5.0)),
                       CONSTRAINT Exams_pk PRIMARY KEY  (studies_id,user_id)
);

-- Table: Intership_meeting_attendance_list
CREATE TABLE Intership_meeting_attendance_list (
                                                   inter_meeting_id int  NOT NULL,
                                                   studies_id int  NOT NULL,
                                                   user_id int  NOT NULL,
                                                   was_present bit  NOT NULL,
                                                   CONSTRAINT Intership_meeting_attendance_list_pk PRIMARY KEY  (inter_meeting_id,user_id,studies_id)
);

-- Table: Intership_meetings
CREATE TABLE Intership_meetings (
                                    studies_id int  NOT NULL,
                                    inter_meeting_id int  NOT NULL IDENTITY(1, 1),
                                    meetind_date datetime  NOT NULL,
                                    CONSTRAINT Intership_meetings_pk PRIMARY KEY  (inter_meeting_id,studies_id)
);

-- Table: Languages
CREATE TABLE Languages (
                           language_id int  NOT NULL IDENTITY(1, 1),
                           language_name nvarchar(30)  NOT NULL,
                           CONSTRAINT Languages_pk PRIMARY KEY  (language_id)
);

-- Table: Order_course
CREATE TABLE Order_course (
                              order_detail_id int  NOT NULL,
                              course_id int  NOT NULL,
                              CONSTRAINT Order_course_pk PRIMARY KEY  (order_detail_id)
);

-- Table: Order_details
CREATE TABLE Order_details (
                               order_detail_id int  NOT NULL IDENTITY(1, 1),
                               order_id int  NOT NULL,
                               type_id int  NOT NULL,
                               price money  NOT NULL,
                               CONSTRAINT order_details_price_check CHECK (price >= 0),
                               CONSTRAINT Order_details_pk PRIMARY KEY  (order_detail_id)
);

-- Table: Order_module_studies
CREATE TABLE Order_module_studies (
                                      order_detail_id int  NOT NULL,
                                      module_id int  NOT NULL,
                                      CONSTRAINT Order_module_studies_pk PRIMARY KEY  (order_detail_id)
);

-- Table: Order_studies
CREATE TABLE Order_studies (
                               order_detail_id int  NOT NULL,
                               studies_id int  NOT NULL,
                               CONSTRAINT Order_studies_pk PRIMARY KEY  (order_detail_id)
);

-- Table: Order_webinars
CREATE TABLE Order_webinars (
                                order_detail_id int  NOT NULL,
                                webinar_id int  NOT NULL,
                                CONSTRAINT Order_webinars_pk PRIMARY KEY  (order_detail_id)
);

-- Table: Orders
CREATE TABLE Orders (
                        order_id int  NOT NULL IDENTITY(1, 1),
                        user_id int  NOT NULL,
                        is_paid bit  NOT NULL,
                        max_paid_date datetime  NOT NULL,
                        CONSTRAINT Orders_pk PRIMARY KEY  (order_id)
);

-- Table: Studies
CREATE TABLE Studies (
                         studies_id int  NOT NULL IDENTITY(1, 1),
                         studies_name nvarchar(30)  NOT NULL,
                         studies_description nvarchar(300)  NOT NULL,
                         start_date date  NOT NULL,
                         students_limit int  NOT NULL,
                         price money  NOT NULL,
                         studies_coordinator_id int  NOT NULL,
                         visible_from date  NOT NULL,
                         CONSTRAINT studies_price_check CHECK (price >= 0),
                         CONSTRAINT Studies_pk PRIMARY KEY  (studies_id)
);

-- Table: Studies_Module
CREATE TABLE Studies_Module (
                                studies_module_id int  NOT NULL IDENTITY(1, 1),
                                module_type_id int  NOT NULL,
                                module_name nvarchar(30)  NOT NULL,
                                studies_id int  NOT NULL,
                                price_for_module money  NOT NULL,
                                CONSTRAINT price_check CHECK (price_for_module >= 0),
                                CONSTRAINT studies_module_id PRIMARY KEY  (studies_module_id)
);

-- Table: Studies_makeup_meeting_attendance_list
CREATE TABLE Studies_makeup_meeting_attendance_list (
                                                        makeup_list_id int  NOT NULL IDENTITY(1, 1),
                                                        user_id int  NOT NULL,
                                                        studies_id int  NOT NULL,
                                                        meeting_id int  NOT NULL,
                                                        used bit  NOT NULL DEFAULT 0,
                                                        CONSTRAINT Studies_makeup_meeting_attendance_list_pk PRIMARY KEY  (makeup_list_id)
);

-- Table: Studies_meeting_attendance_list
CREATE TABLE Studies_meeting_attendance_list (
                                                 user_id int  NOT NULL,
                                                 studies_id int  NOT NULL,
                                                 meeting_id int  NOT NULL,
                                                 was_present bit  NOT NULL,
                                                 did_makeup bit  NOT NULL DEFAULT 0,
                                                 CONSTRAINT Studies_meeting_attendance_list_pk PRIMARY KEY  (user_id,studies_id,meeting_id)
);

-- Table: Studies_module_meetings
CREATE TABLE Studies_module_meetings (
                                         meeting_id int  NOT NULL,
                                         studies_id int  NOT NULL,
                                         meeting_date datetime  NOT NULL,
                                         language_id int  NOT NULL,
                                         translator_id int  NULL,
                                         lecturer_id int  NOT NULL,
                                         duration time  NOT NULL,
                                         place_limit int  NOT NULL,
                                         module_id int  NOT NULL,
                                         topic_id int  NOT NULL,
                                         meeting_name nvarchar(30)  NOT NULL,
                                         meeting_type_id int  NOT NULL,
                                         CONSTRAINT Studies_module_meetings_pk PRIMARY KEY  (meeting_id,studies_id)
);

-- Table: Studies_stationary_meeting
CREATE TABLE Studies_stationary_meeting (
                                            id int  NOT NULL IDENTITY(1, 1),
                                            studies_id int  NOT NULL,
                                            meeting_id int  NOT NULL,
                                            classroom nvarchar(6)  NOT NULL,
                                            CONSTRAINT Studies_stationary_meeting_pk PRIMARY KEY  (id)
);

-- Table: Studies_sync_async_meeting
CREATE TABLE Studies_sync_async_meeting (
                                            id int  NOT NULL IDENTITY(1, 1),
                                            studies_id int  NOT NULL,
                                            meeting_id int  NOT NULL,
                                            access_to datetime  NOT NULL,
                                            video_link nvarchar(30)  NOT NULL,
                                            stream_link nvarchar(30)  NULL,
                                            CONSTRAINT Studies_sync_async_meeting_pk PRIMARY KEY  (id)
);

-- Table: Translators
CREATE TABLE Translators (
                             translator_id int  NOT NULL IDENTITY(1, 1),
                             employee_id int  NOT NULL,
                             CONSTRAINT Translators_pk PRIMARY KEY  (translator_id)
);

-- Table: Translators_languages_used
CREATE TABLE Translators_languages_used (
                                            id int  NOT NULL IDENTITY(1, 1),
                                            translator_id int  NOT NULL,
                                            language_id int  NOT NULL,
                                            CONSTRAINT Translators_languages_used_pk PRIMARY KEY  (id)
);

-- Table: Users
CREATE TABLE Users (
                       user_id int  NOT NULL IDENTITY(1, 1),
                       email nvarchar(50)  NOT NULL,
                       first_name nvarchar(30)  NOT NULL,
                       last_name nvarchar(30)  NOT NULL,
                       city_id int  NOT NULL,
                       country_id int  NOT NULL,
                       phone nvarchar(9)  NOT NULL CHECK (PATINDEX('%[^0-9]%', phone) = 0 AND LEN(phone) = 9),
                       street nvarchar(30)  NOT NULL,
                       house_number int  NOT NULL,
                       birth_date date  NOT NULL,
                       CONSTRAINT users_birth_date_check CHECK (datediff(year,birth_date,getdate()) < 100),
                       CONSTRAINT Users_pk PRIMARY KEY  (user_id)
);

-- Table: Webinars
CREATE TABLE Webinars (
                          webinar_id int  NOT NULL IDENTITY(1, 1),
                          name nvarchar(30)  NOT NULL,
                          description nvarchar(300)  NOT NULL,
                          teacher_id int  NOT NULL,
                          price money  NOT NULL,
                          can_buy_from date  NOT NULL,
                          recording_link nvarchar(30)  NOT NULL,
                          start_date date  NOT NULL,
                          CONSTRAINT webinar_price_check CHECK (price >= 0),
                          CONSTRAINT Webinars_pk PRIMARY KEY  (webinar_id)
);

-- Table: meeting_type
CREATE TABLE meeting_type (
                              meeting_type_id int  NOT NULL IDENTITY(1, 1),
                              meeting_name nvarchar(30)  NOT NULL,
                              CONSTRAINT meeting_type_pk PRIMARY KEY  (meeting_type_id)
);

-- Table: module_type
CREATE TABLE module_type (
                             module_type_id int  NOT NULL IDENTITY(1, 1),
                             module_name nvarchar(30)  NOT NULL,
                             CONSTRAINT module_type_pk PRIMARY KEY  (module_type_id)
);

-- Table: topics_list
CREATE TABLE topics_list (
                             topic_id int  NOT NULL IDENTITY(1, 1),
                             topic_name nvarchar(30)  NOT NULL,
                             topic_description nvarchar(300)  NOT NULL,
                             CONSTRAINT topics_list_pk PRIMARY KEY  (topic_id)
);

-- foreign keys
-- Reference: Cities_Users (table: Users)
ALTER TABLE Users ADD CONSTRAINT Cities_Users
    FOREIGN KEY (city_id)
        REFERENCES Cities (city_id);

-- Reference: Countries_Users (table: Users)
ALTER TABLE Users ADD CONSTRAINT Countries_Users
    FOREIGN KEY (country_id)
        REFERENCES Countries (country_id);

-- Reference: Course_meeting_attendance_list_Course_module_meetings (table: Course_meeting_attendance_list)
ALTER TABLE Course_meeting_attendance_list ADD CONSTRAINT Course_meeting_attendance_list_Course_module_meetings
    FOREIGN KEY (meeting_id,course_id)
        REFERENCES Course_module_meetings (meeting_id,course_id);

-- Reference: Course_meeting_attendance_list_Users (table: Course_meeting_attendance_list)
ALTER TABLE Course_meeting_attendance_list ADD CONSTRAINT Course_meeting_attendance_list_Users
    FOREIGN KEY (user_id)
        REFERENCES Users (user_id);

-- Reference: Course_module_Course_module_meetings (table: Course_module_meetings)
ALTER TABLE Course_module_meetings ADD CONSTRAINT Course_module_Course_module_meetings
    FOREIGN KEY (module_id)
        REFERENCES module_type (module_type_id);

-- Reference: Course_module_meetings_Course_module_meeting_stationary (table: Course_stationary_meeting)
ALTER TABLE Course_stationary_meeting ADD CONSTRAINT Course_module_meetings_Course_module_meeting_stationary
    FOREIGN KEY (meeting_id,course_id)
        REFERENCES Course_module_meetings (meeting_id,course_id);

-- Reference: Course_module_meetings_Course_modules (table: Course_module_meetings)
ALTER TABLE Course_module_meetings ADD CONSTRAINT Course_module_meetings_Course_modules
    FOREIGN KEY (module_id)
        REFERENCES Course_modules (course_module_id);

-- Reference: Course_module_meetings_Employees (table: Course_module_meetings)
ALTER TABLE Course_module_meetings ADD CONSTRAINT Course_module_meetings_Employees
    FOREIGN KEY (lecturer_id)
        REFERENCES Employees (employee_id);

-- Reference: Course_module_meetings_Languages (table: Course_module_meetings)
ALTER TABLE Course_module_meetings ADD CONSTRAINT Course_module_meetings_Languages
    FOREIGN KEY (language_id)
        REFERENCES Languages (language_id);

-- Reference: Course_modules_module_type (table: Course_modules)
ALTER TABLE Course_modules ADD CONSTRAINT Course_modules_module_type
    FOREIGN KEY (module_type_id)
        REFERENCES module_type (module_type_id);

-- Reference: Course_video_access_Course_module_meetings (table: Course_sync_async_meeting)
ALTER TABLE Course_sync_async_meeting ADD CONSTRAINT Course_video_access_Course_module_meetings
    FOREIGN KEY (meeting_id,course_id)
        REFERENCES Course_module_meetings (meeting_id,course_id);

-- Reference: Courses_Course_modules (table: Course_modules)
ALTER TABLE Course_modules ADD CONSTRAINT Courses_Course_modules
    FOREIGN KEY (course_id)
        REFERENCES Courses (course_id);

-- Reference: Courses_Employees (table: Courses)
ALTER TABLE Courses ADD CONSTRAINT Courses_Employees
    FOREIGN KEY (course_coordinator_id)
        REFERENCES Employees (employee_id);

-- Reference: Employees_Cities (table: Employees)
ALTER TABLE Employees ADD CONSTRAINT Employees_Cities
    FOREIGN KEY (city_id)
        REFERENCES Cities (city_id);

-- Reference: Employees_Countries (table: Employees)
ALTER TABLE Employees ADD CONSTRAINT Employees_Countries
    FOREIGN KEY (country_id)
        REFERENCES Countries (country_id);

-- Reference: Employees_Employee_Roles (table: Employees)
ALTER TABLE Employees ADD CONSTRAINT Employees_Employee_Roles
    FOREIGN KEY (role_id)
        REFERENCES Employee_Roles (role_id);

-- Reference: Exams_Studies (table: Exams)
ALTER TABLE Exams ADD CONSTRAINT Exams_Studies
    FOREIGN KEY (studies_id)
        REFERENCES Studies (studies_id);

-- Reference: Exams_Users (table: Exams)
ALTER TABLE Exams ADD CONSTRAINT Exams_Users
    FOREIGN KEY (user_id)
        REFERENCES Users (user_id);

-- Reference: Intership_meeting_attendance_list_Intership_meetings (table: Intership_meeting_attendance_list)
ALTER TABLE Intership_meeting_attendance_list ADD CONSTRAINT Intership_meeting_attendance_list_Intership_meetings
    FOREIGN KEY (inter_meeting_id,studies_id)
        REFERENCES Intership_meetings (inter_meeting_id,studies_id);

-- Reference: Intership_meeting_attendance_list_Users (table: Intership_meeting_attendance_list)
ALTER TABLE Intership_meeting_attendance_list ADD CONSTRAINT Intership_meeting_attendance_list_Users
    FOREIGN KEY (user_id)
        REFERENCES Users (user_id);

-- Reference: Intership_meetings_Studies (table: Intership_meetings)
ALTER TABLE Intership_meetings ADD CONSTRAINT Intership_meetings_Studies
    FOREIGN KEY (studies_id)
        REFERENCES Studies (studies_id);

-- Reference: Order_course_Courses (table: Order_course)
ALTER TABLE Order_course ADD CONSTRAINT Order_course_Courses
    FOREIGN KEY (course_id)
        REFERENCES Courses (course_id);

-- Reference: Order_course_Order_details (table: Order_course)
ALTER TABLE Order_course ADD CONSTRAINT Order_course_Order_details
    FOREIGN KEY (order_detail_id)
        REFERENCES Order_details (order_detail_id);

-- Reference: Order_details_Event_types (table: Order_details)
ALTER TABLE Order_details ADD CONSTRAINT Order_details_Event_types
    FOREIGN KEY (type_id)
        REFERENCES Event_types (type_id);

-- Reference: Order_details_Orders (table: Order_details)
ALTER TABLE Order_details ADD CONSTRAINT Order_details_Orders
    FOREIGN KEY (order_id)
        REFERENCES Orders (order_id);

-- Reference: Order_meeting_studies_Order_details (table: Order_module_studies)
ALTER TABLE Order_module_studies ADD CONSTRAINT Order_meeting_studies_Order_details
    FOREIGN KEY (order_detail_id)
        REFERENCES Order_details (order_detail_id);

-- Reference: Order_studies_Order_details (table: Order_studies)
ALTER TABLE Order_studies ADD CONSTRAINT Order_studies_Order_details
    FOREIGN KEY (order_detail_id)
        REFERENCES Order_details (order_detail_id);

-- Reference: Order_studies_Studies (table: Order_studies)
ALTER TABLE Order_studies ADD CONSTRAINT Order_studies_Studies
    FOREIGN KEY (studies_id)
        REFERENCES Studies (studies_id);

-- Reference: Order_webinars_Order_details (table: Order_webinars)
ALTER TABLE Order_webinars ADD CONSTRAINT Order_webinars_Order_details
    FOREIGN KEY (order_detail_id)
        REFERENCES Order_details (order_detail_id);

-- Reference: Order_webinars_Webinar_info (table: Order_webinars)
ALTER TABLE Order_webinars ADD CONSTRAINT Order_webinars_Webinar_info
    FOREIGN KEY (webinar_id)
        REFERENCES Webinars (webinar_id);

-- Reference: Studies_Employees (table: Studies)
ALTER TABLE Studies ADD CONSTRAINT Studies_Employees
    FOREIGN KEY (studies_coordinator_id)
        REFERENCES Employees (employee_id);

-- Reference: Studies_Module_Order_meeting_studies (table: Order_module_studies)
ALTER TABLE Order_module_studies ADD CONSTRAINT Studies_Module_Order_meeting_studies
    FOREIGN KEY (module_id)
        REFERENCES Studies_Module (studies_module_id);

-- Reference: Studies_makeup_meeting_attendacne_list_Studies_module_meetings (table: Studies_makeup_meeting_attendance_list)
ALTER TABLE Studies_makeup_meeting_attendance_list ADD CONSTRAINT Studies_makeup_meeting_attendacne_list_Studies_module_meetings
    FOREIGN KEY (meeting_id,studies_id)
        REFERENCES Studies_module_meetings (meeting_id,studies_id);

-- Reference: Studies_makeup_meeting_attendacne_list_Users (table: Studies_makeup_meeting_attendance_list)
ALTER TABLE Studies_makeup_meeting_attendance_list ADD CONSTRAINT Studies_makeup_meeting_attendacne_list_Users
    FOREIGN KEY (user_id)
        REFERENCES Users (user_id);

-- Reference: Studies_meeting_attendance_list_Studies_module_meetings (table: Studies_meeting_attendance_list)
ALTER TABLE Studies_meeting_attendance_list ADD CONSTRAINT Studies_meeting_attendance_list_Studies_module_meetings
    FOREIGN KEY (meeting_id,studies_id)
        REFERENCES Studies_module_meetings (meeting_id,studies_id);

-- Reference: Studies_meeting_attendance_list_Users (table: Studies_meeting_attendance_list)
ALTER TABLE Studies_meeting_attendance_list ADD CONSTRAINT Studies_meeting_attendance_list_Users
    FOREIGN KEY (user_id)
        REFERENCES Users (user_id);

-- Reference: Studies_module_meeting_stationary_Studies_module_meetings (table: Studies_stationary_meeting)
ALTER TABLE Studies_stationary_meeting ADD CONSTRAINT Studies_module_meeting_stationary_Studies_module_meetings
    FOREIGN KEY (meeting_id,studies_id)
        REFERENCES Studies_module_meetings (meeting_id,studies_id);

-- Reference: Studies_module_meetings_Employees (table: Studies_module_meetings)
ALTER TABLE Studies_module_meetings ADD CONSTRAINT Studies_module_meetings_Employees
    FOREIGN KEY (lecturer_id)
        REFERENCES Employees (employee_id);

-- Reference: Studies_module_meetings_Studiies_Module (table: Studies_module_meetings)
ALTER TABLE Studies_module_meetings ADD CONSTRAINT Studies_module_meetings_Studiies_Module
    FOREIGN KEY (module_id)
        REFERENCES Studies_Module (studies_module_id);

-- Reference: Studies_module_meetings_Translators (table: Studies_module_meetings)
ALTER TABLE Studies_module_meetings ADD CONSTRAINT Studies_module_meetings_Translators
    FOREIGN KEY (translator_id)
        REFERENCES Translators (translator_id);

-- Reference: Studies_module_meetings_meeting_type (table: Studies_module_meetings)
ALTER TABLE Studies_module_meetings ADD CONSTRAINT Studies_module_meetings_meeting_type
    FOREIGN KEY (meeting_type_id)
        REFERENCES meeting_type (meeting_type_id);

-- Reference: Studies_sync_async_meeting_Studies_module_meetings (table: Studies_sync_async_meeting)
ALTER TABLE Studies_sync_async_meeting ADD CONSTRAINT Studies_sync_async_meeting_Studies_module_meetings
    FOREIGN KEY (meeting_id,studies_id)
        REFERENCES Studies_module_meetings (meeting_id,studies_id);

-- Reference: Studiies_Module_Studies (table: Studies_Module)
ALTER TABLE Studies_Module ADD CONSTRAINT Studiies_Module_Studies
    FOREIGN KEY (studies_id)
        REFERENCES Studies (studies_id);

-- Reference: Studiies_Module_module_type (table: Studies_Module)
ALTER TABLE Studies_Module ADD CONSTRAINT Studiies_Module_module_type
    FOREIGN KEY (module_type_id)
        REFERENCES module_type (module_type_id);

-- Reference: Translators_Course_module_meetings (table: Course_module_meetings)
ALTER TABLE Course_module_meetings ADD CONSTRAINT Translators_Course_module_meetings
    FOREIGN KEY (translator_id)
        REFERENCES Translators (translator_id);

-- Reference: Translators_Employees (table: Translators)
ALTER TABLE Translators ADD CONSTRAINT Translators_Employees
    FOREIGN KEY (employee_id)
        REFERENCES Employees (employee_id);

-- Reference: Translators_languages_used_Languages (table: Translators_languages_used)
ALTER TABLE Translators_languages_used ADD CONSTRAINT Translators_languages_used_Languages
    FOREIGN KEY (language_id)
        REFERENCES Languages (language_id);

-- Reference: Translators_languages_used_Translators (table: Translators_languages_used)
ALTER TABLE Translators_languages_used ADD CONSTRAINT Translators_languages_used_Translators
    FOREIGN KEY (translator_id)
        REFERENCES Translators (translator_id);

-- Reference: Webinar_info_Employees (table: Webinars)
ALTER TABLE Webinars ADD CONSTRAINT Webinar_info_Employees
    FOREIGN KEY (teacher_id)
        REFERENCES Employees (employee_id);

-- Reference: meeting_type_Course_module_meetings (table: Course_module_meetings)
ALTER TABLE Course_module_meetings ADD CONSTRAINT meeting_type_Course_module_meetings
    FOREIGN KEY (meeting_type_id)
        REFERENCES meeting_type (meeting_type_id);

-- Reference: module_type_Studies_module_meetings (table: Studies_module_meetings)
ALTER TABLE Studies_module_meetings ADD CONSTRAINT module_type_Studies_module_meetings
    FOREIGN KEY (module_id)
        REFERENCES module_type (module_type_id);

-- Reference: topics_list_Studies_module_meetings (table: Studies_module_meetings)
ALTER TABLE Studies_module_meetings ADD CONSTRAINT topics_list_Studies_module_meetings
    FOREIGN KEY (topic_id)
        REFERENCES topics_list (topic_id);

-- End of file.

