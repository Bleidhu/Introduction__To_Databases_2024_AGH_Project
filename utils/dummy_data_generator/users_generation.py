import db_tables_classes as db_model
from faker import Faker
import datetime
import random
import dummy_values as dval
from typing import List
import csv
USERS_LIMIT = 100
CITIES_AMOUNT = len(dval.cities)
COUNTRIES_AMOUNT = len(dval.countries)
LANGUAGES_AMOUNt = len(dval.languages)

fk = Faker()

def generate_email_from_name(first_name: str, last_name: str):
    return first_name.lower() + last_name.lower() + "@" + fk.domain_name()
def generate_user(id):
    name, last_name = fk.first_name(), fk.last_name()
    tmp = db_model.User(id, generate_email_from_name(name, last_name), name, last_name, random.randint(1, CITIES_AMOUNT+1), random.randint(1, COUNTRIES_AMOUNT+1), random.randint(100000000, 999999999), fk.street_name(), fk.building_number(), fk.date_of_birth(minimum_age=16, maximum_age=80))

    return tmp

def generate_users_table():
    tmp = [generate_user(i) for i in range(USERS_LIMIT)]

    return tmp

def users_table_to_csv(users_table: List[db_model.User], filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['user_id', 'email', 'first_name', 'last_name', 'city_id', 'country_id', 'phone', 'street', 'house_number', 'birth_date'])
        writer.writeheader()
        for user in users_table:
            writer.writerow(user.__dict__)
def main():
    users = generate_users_table()
    users_table_to_csv(users, './dummy_data/users.csv')

if __name__ == "__main__":
    main()