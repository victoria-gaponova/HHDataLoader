from api.hh_api import HH
from database.db_manager import DBManager
from config import EMPLOYER_MAP
from utils.currency_converter import get_currency_converter
from utils.generation_unique_key import generate_unique_key

if __name__ == '__main__':
    keys_list = []
    hh = HH()
    db_manager = DBManager()
    db_manager.connecting_to_bd()
    user_input = int(input("Для работы со старыми данными из БД: нажмите любую клавишу\n"
                           "Для новых данных: 2\n"))

    if user_input == 2:
        db_manager.delete_all_table()
        db_manager.create_all_vacancies_table()
        for employer_name, employer_id in EMPLOYER_MAP.items():
            compnay_vacancies = hh.get_vacancies(employer_id)
            db_manager.create_company_table(employer_name)
            for vacancy in compnay_vacancies:
                vacancy_name = vacancy["name"]
                vacancy_url = vacancy["alternate_url"]
                vacancy_from = int(
                    vacancy["salary"]["from"]) if vacancy.get("salary") is not None and vacancy["salary"].get(
                    "from") is not None else 0
                vacancy_to = int(
                    vacancy["salary"]["to"]) if vacancy.get("salary") is not None and vacancy["salary"].get(
                    "to") is not None else 0
                if vacancy.get("salary") and vacancy["salary"]["currency"] not in ["RUR", "RUB"]:
                    vacancy_from *= get_currency_converter(vacancy["salary"]["currency"])
                    vacancy_to *= get_currency_converter(vacancy["salary"]["currency"])

                vacancy_currency = "RUR"
                vacancy_id = generate_unique_key(keys_list)
                db_manager.insert_all_vacancies_table(id=vacancy_id, company_name=employer_name,
                                                      vacancy_name=vacancy_name,
                                                      vacancy_salary_from=vacancy_from, vacancy_salary_to=vacancy_to,
                                                      vacancy_currency=vacancy_currency,
                                                      vacancy_url=vacancy_url)
                db_manager.insert_company_table(employer_name, vacancy_name=vacancy_name,
                                                vacancy_salary_from=vacancy_from, vacancy_salary_to=vacancy_to,
                                                vacancy_currency=vacancy_currency, vacancy_url=vacancy_url,vacancy_id=vacancy_id)
    while True:
        user_choice = int(input("Получение всех вакансий: 1\n"
                                "Средняя зарплата: 2\n"
                                "Вакансии с зарплатой выше средней: 3\n"
                                "Вакансии с ключевым словом: 4\n"
                                "Компании с количеством вакакансий: 5\n"
                                "Выход: 0\n"))
        if user_choice == 1:
            db_manager.get_all_vacancies()
        elif user_choice == 2:
            db_manager.get_avg_salary()
        elif user_choice == 3:
            db_manager.get_vacancies_with_hight_salary()
        elif user_choice == 4:
            db_manager.get_vacancies_with_keyword(input("Введите ключевое слово: "))
        elif user_choice == 5:
            db_manager.get_compnay_vacancies_count()
        elif user_choice == 0:
            exit()
        else:
            print("Введено неверное значение!")
    db_manager.disconnect_db()
