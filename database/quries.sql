--Создание таблицы всех вакансий
CREATE TABLE IF NOT EXISTS all_vacancies (
            id VARCHAR(4) PRIMARY KEY,
            company_name VARCHAR(30) NOT NULL,
            vacancy_name VARCHAR(100) NOT NULL,
            vacancy_salary_from INTEGER NOT NULL,
            vacancy_salary_to INTEGER NOT NULL,
            vacancy_currency VARCHAR(10),
            vacancy_url VARCHAR(100) NOT NULL
);

--Создание таблицы компании
CREATE TABLE IF NOT EXISTS {company_name}
(
    id SERIAL  PRIMARY KEY,
    vacancy_name VARCHAR(100) NOT NULL,
    vacancy_salary_from INTEGER NOT NULL,
    vacancy_salary_to INTEGER NOT NULL,
    vacancy_currency  VARCHAR(10),
    vacancy_url VARCHAR(100) NOT NULL,
    vacancy_id VARCHAR(4),
    FOREIGN KEY (vacancy_id) REFERENCES all_vacancies (id) ON DELETE CASCADE
);

--Удаление таблиц
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

--Заполнение таблицы всех вакансий
INSERT INTO all_vacancies (id, company_name, vacancy_name, vacancy_salary_from, vacancy_salary_to, vacancy_currency, vacancy_url)
VALUES (%s, %s, %s, %s, %s, %s, %s);

--Заполнение таблицы компании
INSERT INTO {company_name} (vacancy_name, vacancy_salary_from, vacancy_salary_to, vacancy_currency, vacancy_url, vacancy_id)
VALUES (%s,%s,%s,%s,%s,%s);

--Компании с количеством вакакансий
SELECT company_name, COUNT(*) AS amount_vacancies
FROM all_vacancies
GROUP BY company_name;

--Получение всех вакансий
SELECT * FROM all_vacancies;

--Средняя зарплата
SELECT
    (SELECT ROUND(AVG(vacancy_salary_from)) FROM all_vacancies WHERE  vacancy_salary_from <> 0)AS avg_salary_from,
    (SELECT ROUND(AVG(vacancy_salary_to)) FROM all_vacancies WHERE  vacancy_salary_to <> 0)AS avg_salary_to;

--Вакансии с зарплатой выше средней
SELECT * FROM  all_vacancies
where vacancy_salary_from >
    (SELECT ROUND(AVG(vacancy_salary_from)) FROM all_vacancies WHERE  vacancy_salary_from <> 0)
AND vacancy_salary_to >
    (SELECT ROUND(AVG(vacancy_salary_to)) FROM all_vacancies WHERE  vacancy_salary_to <> 0)
ORDER BY vacancy_salary_from DESC, vacancy_salary_to DESC;

--Вакансии с ключевым словом
SELECT *
FROM  all_vacancies
WHERE LOWER(vacancy_name) ILIKE %s;
