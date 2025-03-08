--1. Создание таблицы Employees.
CREATE TABLE EMPLOYEES (
  id int primary key,
  name varchar(100),
  position varchar(100),
  department varchar(100),
  salary decimal(10,2)
);

--2. Вставка в таблицу нескольких записей с информацией о сотрудниках.
INSERT INTO EMPLOYEES (id, name, position, department, salary)
VALUES (1, 'Nikita', 'Senior Developer', 'IT', 4700.6),           
       (2, 'Anastasia', 'Salesperson', 'Sales', 4300.1),   
       (3, 'Anton', 'Manager', 'Management', 5300.2),      
       (4, 'Petr', 'Economist', 'Economics', 3100.3),      
       (5, 'Varvara', 'Economist', 'Economics', 4250.5);   

SELECT * FROM EMPLOYEES;

--3. UPDATE employees
UPDATE EMPLOYEES
SET position = 'Senior Economist'
WHERE id = 4;

SELECT * FROM EMPLOYEES
WHERE id = 4;

--4. Добавление нового поля HireDate
ALTER TABLE EMPLOYEES 
ADD COLUMN hiredate date;

SELECT * FROM EMPLOYEES;

--5. Добавление записей о дате приема на работу для всех сотрудников
UPDATE EMPLOYEES
SET hiredate = '2022-12-04' 
WHERE id = 1;

UPDATE EMPLOYEES
SET hiredate = '2024-05-28' 
WHERE id = 2;

UPDATE EMPLOYEES
SET hiredate = '2021-11-17' 
WHERE id = 3;

UPDATE EMPLOYEES
SET hiredate = '2023-05-05' 
WHERE id = 4;

UPDATE EMPLOYEES
SET hiredate = '2022-09-07' 
WHERE id = 5;

SELECT * FROM EMPLOYEES;

--6. Найти всех сотрудников, у которых зарплата больше 500 долларов
SELECT * FROM EMPLOYEES
WHERE salary > 5000;

--7. Найти всех сотрудников, которые работают в отделе
SELECT * FROM EMPLOYEES
WHERE department = 'Sales';

--8. Найти среднюю зарплату по всем сотрудникам
SELECT AVG(salary) as average_salary
FROM EMPLOYEES;

--9. Удаление таблицы
DROP TABLE EMPLOYEES;
