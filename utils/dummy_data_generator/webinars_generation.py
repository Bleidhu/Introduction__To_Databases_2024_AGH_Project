import db_tables_classes as db_model
from faker import Faker
import datetime
import random
import dummy_values as dval
import utility_functions as uf
import random

import employees_generation as emp
CITIES_AMOUNT = len(dval.cities)
COUNTRIES_AMOUNT = len(dval.countries)
LANGUAGES_AMOUNt = len(dval.languages)
WEBINARS_AMOUNT = 10
START_DATE_ALL = datetime.date.fromisoformat(dval.START_DATE_ALL)
fk = Faker()

## Webinars
# To do: Better descriptions (maybe from chatgpt)
# Better start date
# Assigning teachers
employees, _, _ = emp.generate_employees_table()
last_date = START_DATE_ALL
webinars = []
def generate_webinar(id):
    global last_date
    last_date = fk.date_between(last_date, last_date+datetime.timedelta(days=100))
    return db_model.Webinar(id, fk.catch_phrase(), "Lorem ipsum",
                             random.choice(uf.get_employees_not_working_on_date(uf.get_employees_hired_after_date(employees, last_date), date=last_date.isoformat(), webinars_meetings=webinars)).employee_id,
                             #0,
                               random.randint(0, 500) ,last_date, fk.url(), last_date)
def generate_webinars():
    
    for i in range(WEBINARS_AMOUNT):
        webinars.append(generate_webinar(i))
    return webinars

#print(uf.get_employees_not_working_on_date(uf.get_employees_hired_after_date(employees, last_date), date=last_date.isoformat(), webinars_meetings=webinars))

webinars = generate_webinars()
for webinar in webinars:
    print(webinar)