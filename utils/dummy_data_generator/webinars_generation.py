import db_tables_classes as db_model
from faker import Faker
import datetime
import random
import dummy_values as dval

CITIES_AMOUNT = len(dval.cities)
COUNTRIES_AMOUNT = len(dval.countries)
LANGUAGES_AMOUNt = len(dval.languages)
WEBINARS_AMOUNT = 10

fk = Faker()

## Webinars
# To do: Better descriptions (maybe from chatgpt)
# Better start date
# Assigning teachers

def generate_webinar(id):
    start_date = fk.date_this_decade()
    return db_model.Webinar(id, fk.catch_phrase(), "Lorem ipsum", 0, random.randint(0, 500) ,start_date, fk.url(), start_date)
def generate_webinars():
    webinars = []
    for i in range(WEBINARS_AMOUNT):
        webinars.append(generate_webinar(i))
    return webinars