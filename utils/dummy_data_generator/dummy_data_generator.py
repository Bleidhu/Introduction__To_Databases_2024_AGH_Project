
import db_tables_classes as db_model
from faker import Faker
import random
USERS_LIMIT = 10
EMPLOYEES_LIMIT = 10
COURSES_LIMIT = 10
COURSE_MODULE_MEETINGS_LIMIT = 10
CITIES_AMOUNT = 10
COUNTRIES_AMOUNT = 10

fk = Faker()

def generate_user(id):
    tmp = db_model.User(id, fk.email(), fk.first_name(), fk.last_name(), random.randint(0, CITIES_AMOUNT), random.randint(0, COUNTRIES_AMOUNT))

    return tmp

def generate_users_table():
    tmp = [generate_user(i) for i in range(USERS_LIMIT)]

    return tmp

def generate_employee(id):
    tmp = db_model.Employee(id,  fk.first_name(), fk.last_name(), fk.date_of_birth(minimum_age=18, maximum_age=60), fk.date_this_decade() ,fk.phone(), fk.email(), 0,random.randint(0, CITIES_AMOUNT), random.randint(0, COUNTRIES_AMOUNT))

    return tmp

def generate_employees_table():
    tmp = [generate_employee(i) for i in range(EMPLOYEES_LIMIT)]

    return tmp

def generate_course(id):
    modules = []
    meetings = []
    enrolled_students = []
    stationary_meetings = []
    sync_async_meetings = []
    meetings_atendance_list = []


    


def main():
    users = generate_users_table()
    for user in users:
        print(user)

    employees = generate_employees_table()

if __name__ == "__main__":
    main()