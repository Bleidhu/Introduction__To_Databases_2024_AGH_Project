from dummy_values import *
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
    def __str__(self):
        return (f"{self.first_name}, {self.last_name}, {self.city_id}, {self.country_id}, {self.phone}, {self.street}, {self.house_number}")

def generate_random_person():
    person = Person(fk.name(), fk.last_name(), 0, fk.phone_number(), fk.street_name(), fk.street_address(), fk.building_number())

    return person

class Employee(Person):
    def __init__ (self, first_name, last_name, city_id, country_id, phone, street, house_number, role_id):
        super().__init__(first_name, last_name, city_id, country_id, phone, street, house_number)
        self.role_id = role_id

def generate_random_employee():
    pass

class Course:
    def __init__ (self, course_id, course_name, course_description, start_date, students_limit, price, course_coordinator_id):
        self.course_id = course_id
        self.course_name = course_name
        self.course_description = course_description
        self.start_date = start_date
        self.students_limit = students_limit
        self.price = price
        self.course_coordinator_id = course_coordinator_id


# def generate_course():

# class Course_Module: