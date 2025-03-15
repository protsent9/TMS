import os
from textwrap import indent

# 1. Есть папка, в которой лежат файлы с разными расширениями.
# Программа должна:
# 1.1 Вывести имя вашей ОС.
if os.name == 'posix':
    print('Имя вашей ОС - Linux или macOS.')
if os.name == 'nt':
    print('Имя вашей ОС - Windows')


# 1.2 Вывести путь до папки, в которой вы находитесь.
print('Пусть к папке в которой вы находитесь:', os.getcwd())


# 1.3 Рассортировать файлы по расширениям, например, для текстовых
# файлов создается папка, в неё перемещаются все файлы с расширением
# .txt, то же самое для остальных расширений.
files = os.listdir()

print('Данная директория содержит следующие файлы: ')
for i in files:
    print(i)

counts = {}
file_sizes = {}
for i in files:
    if os.path.isdir(i):
        continue
    extension = os.path.splitext(i)[1][1:]
    if os.path.exists(extension) == 0:
        os.mkdir(extension)
    os.replace(i, os.path.join(extension, i))
    if extension not in counts:
        counts[extension] = 0
    counts[extension] += 1
    file_size = os.path.getsize(os.path.join(extension, i))
    if extension not in file_sizes:
        file_sizes[extension] = 0
    file_sizes[extension] += file_size


# 1.4 После рассортировки выводится сообщение типа «в папке с текстовыми
# файлами перемещено 5 файлов, их суммарный размер - 50 гигабайт»
for extension in counts:
    print(f'Количество файлов, перемещённых в папку с расширением '
          f'".{extension}": {counts[extension]}, их суммарный размер:'
          f' {file_sizes[extension]} байт')


# 1.5 Как минимум один файл в любой из получившихся поддиректорий
# переименовать. Сделать вывод сообщения типа «Файл data.txt был
# переименован в some_data.txt»
import random

# Создаём список поддиректорий в выбранной папке
subdirectories = [i for i in os.listdir(os.getcwd())
                  if os.path.isdir(os.path.join(os.getcwd(), i))]

# Выбираем случайную папку в папке в которой находимся
selected_directory = random.choice(subdirectories)
# Формируем новый путь отталкиваясь от выбранной папки
full_directory = os.path.join(os.getcwd(), selected_directory)
# Выбираем все файлы в выбранной папке
files_in_full_directory = os.listdir(full_directory)
# Выбираем случайный файл из файлов в выбранной папке
selected_file = random.choice(files_in_full_directory)
# Формируем старый путь
old_path = os.path.join(full_directory, selected_file)
# Задаём новое имя
new_name = 'newname'
# Формируем новый путь
new_path = os.path.join(full_directory, new_name)
# Заменяем старое на новое
os.rename(old_path, new_path)
print(f'В директории {full_directory} файл {selected_file} переименован в {new_name}')


# 2. Имеется текстовый файл. Напечатать:
# a) его первую строку:
with open ("exerciseone.txt", 'r') as text_file:
    line = text_file.readline()

print('1-ая строка: ', line)

# b) его пятую строку:
with open ("exerciseone.txt", 'r') as text_file:
    for i in range(4):
        text_file.readline()
    line = text_file.readline()
#
# print('5-ая строка: ', line)
#
# c) его первые 5 строк:
with open ("exerciseone.txt", 'r') as text_file:
    for i in range(5):
        print(f'{i+1}-ая строка: ', text_file.readline().strip())

# d) его строки с s1-й по s2-ю:
with open("exerciseone.txt", 'r') as text_file:
    lines = text_file.readlines()
    while True:
        try:
            s = int(input('Введите значение s: '))

            if s > 5:
                print('Текстовый файл не содержит необходимое количество строк')
                continue
            else:
                break

        except ValueError:
            print('Введите целое число')

    first_line_index = s * 10
    second_line_index = s * 10 + 1

    if first_line_index < len(lines) and second_line_index < len(lines):
        line_f = lines[first_line_index].strip()
        line_s = lines[second_line_index].strip()

    print(f'{first_line_index + 1}-ая строка: {line_f}')
    print(f'{second_line_index + 1}-ая строка: {line_s}')

# e) весь файл:
with open("exerciseone.txt", 'r') as text_file:
    print('Полный текст: ')
    print(text_file.read())


# 3. Создать текстовый файл и записать в него 6 строк. Записываемые
# строки вводятся с клавиатуры.
with open("exercisetwo.txt", 'w') as text_file:
    for i in range(6):
        print(f'Введите {i + 1} строку: ')
        line = input()
        text_file.write(line + '\n')
    print('Строки записаны в файл.')

# 4. Имеются два текстовых файла с одинаковым числом строк. Выяснить,
# совпадают ли их строки. Если нет, то получить номер первой строки,
# в которой эти файлы отличаются друг от друга
with open("exercise3.1.txt", 'r') as first_file, open("exercise3.2.txt", 'r') as second_file:
    first_lines = first_file.readlines()
    second_lines = second_file.readlines()

    for i in range(len(first_lines)):
        first_line = first_lines[i].strip()
        second_line = second_lines[i].strip()

        if first_line != second_line:
            print(f'Отличающиеся строки под индексом {i}.')
            print(f'Из файла exercise3.1: {first_line}')
            print(f'Из файла exercise3.2: {second_line}')
    else:
        print('Все строки в файлах exercise3.1 и exercise3.2 совпадают')


# 5. JSON и CSV.
# 5.0 Есть данные в формате JSON – взять с диска с исходными данными.
import json
import csv


# 5.1 Реализовать функцию, которая считает данные из исходного
# JSON-файла и преобразует их в формат CSV.
def json_convert_csv ():
    with open("employees.json", 'r') as json_file:
        data = json.load(json_file)

    print(data)

    with open("employees.csv", 'w') as csv_file:
        names = data[0].keys()
        file_writer = csv.DictWriter(csv_file, delimiter = ";",
                                     lineterminator = "\r", fieldnames=names)
        file_writer.writeheader()
        for employee in data:
            file_writer.writerow(employee)

# json_convert_csv()


# 5.2 Реализовать функцию, которая сохранит данные в CSV-файл (данные
# должны сохраняться независимо от их количества – если добавить в
# исходный JSON-файл ещё одного сотрудника, работа программы не должна
# нарушаться).

# Как понимаю 5.1 удовлетворяет данному пункту


# 5.3 Реализовать функцию, которая добавит информацию о новом
# сотруднике в JSON-файл. Пошагово вводятся все необходимые данные о
# сотруднике, формируются данные для записи.
from datetime import datetime
def employee_add (name, birthday, height, weight, car, languages):
    new_employee = {
        'name': name,
        'birthday': birthday,
        'height': height,
        'weight': weight,
        'car': car,
        'languages': languages
    }
    print(new_employee)

    with open("employees.json", 'r') as json_file:
        data = json.load(json_file)

    data.append(new_employee)

    with open("employees.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f'Добавлен новый сотрудник: {new_employee}')


# employee_name = str(input('Введите имя сотрудника: '))
#
# while True:
#     employee_birthday = input('Введите дату рождения сотрудника в формате DD.MM.YYYY: ')
#     try:
#         datetime.strptime(employee_birthday, '%d.%m.%Y')
#         break
#     except ValueError:
#         print("Неверный формат даты. Попробуйте снова.")
#
# while True:
#     employee_height = int(input('Введите рост сотрудника: '))
#     try:
#         if employee_height <= 0:
#             print("Рост должен быть положительным числом.")
#             continue
#         break
#     except ValueError:
#         print("Что-то не так с введённым занчением.")
#
# while True:
#     employee_weight = float(input('Введите вес сотрудника: '))
#     try:
#         if employee_weight <= 0:
#             print("Рост должен быть положительным числом.")
#             continue
#         break
#     except ValueError:
#         print("Что-то не так с введённым занчением.")
#
# employee_car = bool(input('Имеет ли сотрудник машину: '))
# employee_languages = str(input('Введите языки программирования, которыми владеет сотрудник: '))
# employee_languages = [lang.strip() for lang in employee_languages.split(',')]
#
# employee_add(employee_name, employee_birthday, employee_height, employee_weight, employee_car, employee_languages)


# 5.4 Такая же функция для добавления информации о новом сотруднике
# в CSV-файл.
from datetime import datetime
def employee_add_csv (name, birthday, height, weight, car, languages):
    new_employee = {
        'name': name,
        'birthday': birthday,
        'height': height,
        'weight': weight,
        'car': car,
        'languages': languages
    }
    print(new_employee)

    with open("employees.csv", 'a') as csv_file:
        file_writer = csv.writer(csv_file, delimiter = ';',
                                 lineterminator = "\r")
        file_writer.writerow(new_employee.values())

    print(f'Добавлен новый сотрудник: {new_employee}')


# employee_name = str(input('Введите имя сотрудника: '))
#
# while True:
#     employee_birthday = input('Введите дату рождения сотрудника в формате DD.MM.YYYY: ')
#     try:
#         datetime.strptime(employee_birthday, '%d.%m.%Y')
#         break
#     except ValueError:
#         print("Неверный формат даты. Попробуйте снова.")
#
# while True:
#     employee_height = int(input('Введите рост сотрудника: '))
#     try:
#         if employee_height <= 0:
#             print("Рост должен быть положительным числом.")
#             continue
#         break
#     except ValueError:
#         print("Что-то не так с введённым занчением.")
#
# while True:
#     employee_weight = float(input('Введите вес сотрудника: '))
#     try:
#         if employee_weight <= 0:
#             print("Рост должен быть положительным числом.")
#             continue
#         break
#     except ValueError:
#         print("Что-то не так с введённым занчением.")
#
# employee_car = bool(input('Имеет ли сотрудник машину: '))
# employee_languages = str(input('Введите языки программирования, которыми владеет сотрудник: '))
# employee_languages = [lang.strip() for lang in employee_languages.split(',')]
#
# employee_add_csv(employee_name, employee_birthday, employee_height, employee_weight, employee_car, employee_languages)

# 5.5 Реализовать функцию, которая выведет информацию об одном
# сотруднике по имени. Имя для поиска вводится с клавиатуры.
def name_search (name_s):
    with open("employees.json", 'r') as json_file:
        data = json.load(json_file)

    for employee in data:
        if employee['name'] == name_s:
            print(employee)

# name = input('Введите имя для поиска: ')
# name_search(name)

# 5.6 Реализовать функцию фильтра по языку: с клавиатуры вводится язык
# программирования, выводится список всех сотрудников, кто владеет этим
# языком программирования.
def lang_search (language_s):
    with open("employees.json", 'r') as json_file:
        data = json.load(json_file)

    for employee in data:
        if language_s in employee["languages"]:
            print(employee)

# language = input('Введите язык программирования, который требуется: ')
# lang_search (language)


# 5.7 Реализовать функцию фильтра по году: ввести с клавиатуры год
# рождения, вывести средний рост всех сотрудников, у которых год
# рождения меньше заданного.
from datetime import datetime

def birthday_search(birthday_s):
    with open("employees.json", 'r') as json_file:
        data = json.load(json_file)

    employees_height = 0
    count = 0
    for employee in data:
        employee_birthday = datetime.strptime(employee["birthday"], '%d.%m.%Y')
        if employee_birthday.year < int(birthday_s):
            employees_height += employee["height"]
            count += 1
    if count > 0:
        print(f'Получается, что средний рост сотрудников: {employees_height // count}')


# while True:
#     birthday = input('Введите год рождения сотрудника YYYY: ')
#     try:
#         datetime.strptime(birthday, '%Y')
#         break
#     except ValueError:
#         print("Неверный формат даты. Попробуйте снова.")
#
# birthday_search(birthday)


# 5.8 Программа должна представлять собой интерактив – пользовательское
# меню с возможностью выбора определённого действия (действия – функции
# из предыдущих пунктов + выход из программы). Пока пользователь не
# выберет выход из программы, должен предлагаться выбор следующего
# действия.
while True:
    print('Выберите одно из действий:')
    print('1 - Считать данные из исходного JSON-файла и преобразовать их'
      ' в формат CSV.')
    print('2 - Добавить информацию о новом сотруднике в JSON-файл.')
    print('3 - Добавить информацию о новом сотруднике в CSV-файл.')
    print('4 - Вывести информацию об одном сотруднике по имени.')
    print('5 - Вывести список сотрудников при помощи фильтра по языку '
      'программирования.')
    print('6 - Вывести средний рост сотрудников, год рождения которых'
      'меньше указанного.')
    print('7 - Закончить выполнение программы')

    choice = int(input('Выберите действие введя его цифру: '))

    if choice == 1:
        json_convert_csv()
    elif choice == 2:
        employee_name = str(input('Введите имя сотрудника: '))

        while True:
            employee_birthday = input('Введите дату рождения сотрудника в формате DD.MM.YYYY: ')
            try:
                datetime.strptime(employee_birthday, '%d.%m.%Y')
                break
            except ValueError:
                print("Неверный формат даты. Попробуйте снова.")

        while True:
            employee_height = int(input('Введите рост сотрудника: '))
            try:
                if employee_height <= 0:
                    print("Рост должен быть положительным числом.")
                    continue
                break
            except ValueError:
                print("Что-то не так с введённым занчением.")

        while True:
            employee_weight = float(input('Введите вес сотрудника: '))
            try:
                if employee_weight <= 0:
                    print("Рост должен быть положительным числом.")
                    continue
                break
            except ValueError:
                print("Что-то не так с введённым занчением.")

        employee_car = bool(input('Имеет ли сотрудник машину: '))
        employee_languages = str(input('Введите языки программирования, которыми владеет сотрудник: '))
        employee_languages = [lang.strip() for lang in employee_languages.split(',')]

        employee_add(employee_name, employee_birthday, employee_height, employee_weight, employee_car, employee_languages)
    elif choice == 3:
        employee_name = str(input('Введите имя сотрудника: '))

        while True:
            employee_birthday = input('Введите дату рождения сотрудника в формате DD.MM.YYYY: ')
            try:
                datetime.strptime(employee_birthday, '%d.%m.%Y')
                break
            except ValueError:
                print("Неверный формат даты. Попробуйте снова.")

        while True:
            employee_height = int(input('Введите рост сотрудника: '))
            try:
                if employee_height <= 0:
                    print("Рост должен быть положительным числом.")
                    continue
                break
            except ValueError:
                print("Что-то не так с введённым занчением.")

        while True:
            employee_weight = float(input('Введите вес сотрудника: '))
            try:
                if employee_weight <= 0:
                    print("Рост должен быть положительным числом.")
                    continue
                break
            except ValueError:
                print("Что-то не так с введённым занчением.")


        employee_car = bool(input('Имеет ли сотрудник машину: '))
        employee_languages = str(input('Введите языки программирования, которыми владеет сотрудник: '))
        employee_languages = [lang.strip() for lang in employee_languages.split(',')]

        employee_add_csv(employee_name, employee_birthday, employee_height, employee_weight, employee_car, employee_languages)

    elif choice == 4:
        name = input('Введите имя для поиска: ')
        name_search(name)
    elif choice == 5:
        language = input('Введите язык программирования, который требуется: ')
        lang_search (language)
    elif choice == 6:
        while True:
            birthday = input('Введите год рождения сотрудника YYYY: ')
            try:
                datetime.strptime(birthday, '%Y')
                break
            except ValueError:
                print("Неверный формат даты. Попробуйте снова.")

        birthday_search(birthday)
    elif choice == 7:
        break