from dummy_values import countries
from faker import Faker

fk = Faker()

class Person:
    def __init__ (self, first_name, last_name, city_id, country_id, phone, street, house_number):
        self.first_name = first_name
        self.last_name = last_name
        self.city_id = city_id
        self.country_id = country_id
        self.phone = phone
        self.street = street
        self.house_number = house_number

def generate_random_person():
    person = Person(fk.name(), fk.last_name(), 0, fk.phone_number(), fk.street(), fk.street_address())

    return person

class Employee(Person):
    def __init__ (self, first_name, last_name, city_id, country_id, phone, street, house_number):
        super()

def generate_random_employee():
    pass

class Course:
    def __init__ (self, course_id, course_name, course_description, start_date, students_limit, price, coursee_coordinator_id):
        pass

def generate_course():

class Course_Module: