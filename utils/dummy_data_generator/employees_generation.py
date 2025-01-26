
import db_tables_classes as db_model
from faker import Faker
import datetime
import random
import dummy_values as dval
import utility_functions as uf
EMPLOYEES_LIMIT = 10
CITIES_AMOUNT = len(dval.cities)
COUNTRIES_AMOUNT = len(dval.countries)
LANGUAGES_AMOUNt = len(dval.languages)

fk = Faker()

def generate_email_from_name(first_name: str, last_name: str):
    return first_name.lower() + last_name.lower() + "@" + fk.domain_name()

def generate_role_id():
    return 0

def generate_employee(id, role):
    tmp = db_model.Employee(id,  fk.first_name(), fk.last_name(), fk.date_this_decade() ,fk.date_of_birth(minimum_age=18, maximum_age=60) ,random.randint(100000000, 999999999), fk.email(), role ,random.randint(1, CITIES_AMOUNT), random.randint(1, COUNTRIES_AMOUNT))

    return tmp

def generate_employees_table():
    teachers = [generate_employee(i+1, 2) for i in range(EMPLOYEES_LIMIT)]
    translators = [generate_employee(i+len(teachers)+1, 3) for i in range(EMPLOYEES_LIMIT*0,5)]
    translators_table = [db_model.Translator(i, i+len(teachers)+1) for i in range(EMPLOYEES_LIMIT*0,5)]
    translators_language_used = []

    for translator in translators_table:
        lang_count = random.randint(2, 3)

        languages = []

        for i in range(lang_count):
            tmp_lang_id = random.randint(1,LANGUAGES_AMOUNt)
            while tmp_lang_id in languages:
                tmp_lang_id = random.randint(1,LANGUAGES_AMOUNt)
            languages.append(tmp_lang_id)
        
        for lang in languages:
            tmp_translator_lang = db_model.TranslatorsLanguagesUsed(len(translators_language_used), translator.translator_id,  lang)
            translators_language_used.append(tmp_translator_lang)

    ceo = generate_employee(len(teachers) + len(translators)+1, 1)
    all_employees = teachers + translators
    all_employees.append(ceo)
    return all_employees, translators_table, translators_language_used

# employes, translators, translators_langs = generate_employees_table()

# print("INSER INTO Translators (translator_id, employee_id) VALUES")

# for translator in translators:
#     print("(" + translator.__str__() + "),")

# print("INSER INTO TranslatorsLanguagesUsed (id, translator_id, language_id) VALUES")
# for langs in translators_langs:
#     print("(" + langs.__str__() + "),")

def main():
    all_employees, translators, translators_languages = generate_employees_table()
    uf.object_table_table_to_csv(all_employees, './dummy_data/employees.csv')
    uf.object_table_table_to_csv(translators, './dummy_data/translators.csv')
    uf.object_table_table_to_csv(translators_languages, './dummy_data/translators_languages.csv')

if __name__ == "__main__":
    main()