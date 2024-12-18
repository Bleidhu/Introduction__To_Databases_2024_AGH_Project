import db_tables_classes as db_model
from faker import Faker
import datetime
import random
import dummy_values as dval
USERS_LIMIT = 100
CITIES_AMOUNT = len(dval.cities)
COUNTRIES_AMOUNT = len(dval.countries)
LANGUAGES_AMOUNt = len(dval.languages)

fk = Faker()

def generate_email_from_name(first_name: str, last_name: str):
    return first_name.lower() + last_name.lower() + "@" + fk.domain_name()
def generate_user(id):
    name, last_name = fk.first_name(), fk.last_name()
    tmp = db_model.User(id, generate_email_from_name(name, last_name), name, last_name, random.randint(0, CITIES_AMOUNT), random.randint(0, COUNTRIES_AMOUNT), random.randint(100000000, 999999999), fk.street_name(), fk.building_number(), fk.date_of_birth(minimum_age=16, maximum_age=80))

    return tmp

def generate_users_table():
    tmp = [generate_user(i) for i in range(USERS_LIMIT)]

    return tmp