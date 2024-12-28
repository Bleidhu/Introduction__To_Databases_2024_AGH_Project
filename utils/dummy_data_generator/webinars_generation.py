import db_tables_classes as db_model
from faker import Faker
import datetime
import random
import dummy_values as dval
import utility_functions as uf
import random

import employees_generation as emp

def webinars_generator(employees):
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

    last_date = START_DATE_ALL
    webinars = []
    def generate_webinar(id):
        nonlocal last_date
        last_date = fk.date_between(last_date, last_date+datetime.timedelta(days=100))
        return db_model.Webinar(id, dval.webinar_titles_and_descriptions[id][0], dval.webinar_titles_and_descriptions[id][1],
                                random.choice(uf.get_employees_not_working_on_date(uf.get_employees_hired_after_date(employees, last_date), date=last_date.isoformat(), webinars_meetings=webinars)).employee_id,
                                #0,
                                random.randint(0, 500) ,last_date, fk.url(), last_date)
    def generate_webinars():
        
        for i in range(WEBINARS_AMOUNT):
            webinars.append(generate_webinar(i))
        return webinars

    return generate_webinars()
#print(uf.get_employees_not_working_on_date(uf.get_employees_hired_after_date(employees, last_date), date=last_date.isoformat(), webinars_meetings=webinars))

if __name__ == '__main__':
    employees, _, _ = emp.generate_employees_table()
    webinars = webinars_generator(employees)

    for webinar in webinars:
        print(webinar)