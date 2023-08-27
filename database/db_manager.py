import psycopg2
from utils.sql_reading import sql_reading
import pandas as pd
from config import DB_CONNECT


class DBManager:
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    def __init__(self):
        self.connection = None
        self.sql_dict = sql_reading()

    def connecting_to_bd(self):
        self.connection = psycopg2.connect(DB_CONNECT)

    def disconnect_db(self):
        if self.connection:
            self.connection.close()

    def __execute_query(self, query, params=None):
        with self.connection:
            with self.connection.cursor() as curs:
                curs.execute(query, params)

    def ___show_result_bd_query(self, query, params=None):
        with self.connection:
            with self.connection.cursor() as curs:
                curs.execute(query, params)
                result = curs.fetchall()
                columns = [desc[0] for desc in curs.description]
                print(pd.DataFrame(result, columns=columns).to_string(index=False))

    def create_all_vacancies_table(self):
        query = self.sql_dict['Создание таблицы всех вакансий']
        self.__execute_query(query)

    def create_company_table(self, company_name):
        query = self.sql_dict['Создание таблицы компании'].replace("{company_name}", company_name)
        self.__execute_query(query)

    def delete_all_table(self):
        query = self.sql_dict['Удаление таблиц']
        self.__execute_query(query)

    def insert_all_vacancies_table(self, **kwargs):
        query = self.sql_dict['Заполнение таблицы всех вакансий']
        params = list(kwargs.values())
        self.__execute_query(query, params)

    def insert_company_table(self, compnany_name, **kwargs):
        query = self.sql_dict['Заполнение таблицы компании'].replace("{company_name}", compnany_name)
        params = list(kwargs.values())
        self.__execute_query(query, params)

    def get_compnay_vacancies_count(self):
        query = self.sql_dict['Компании с количеством вакакансий']
        self.___show_result_bd_query(query)

    def get_all_vacancies(self):
        query = self.sql_dict['Получение всех вакансий']
        self.___show_result_bd_query(query)

    def get_avg_salary(self):
        query = self.sql_dict['Средняя зарплата']
        self.___show_result_bd_query(query)

    def get_vacancies_with_hight_salary(self):
        query = self.sql_dict['Вакансии с зарплатой выше средней']
        self.___show_result_bd_query(query)

    def get_vacancies_with_keyword(self, keyword):
        params = ("%" + keyword + "%",)
        query = self.sql_dict['Вакансии с ключевым словом']
        self.___show_result_bd_query(query, params=params)
