# 1. Реализовать программу для подсчёта индекса массы тела человека.
# Пользователь вводит рост и вес с клавиатуры. На выходе – ИМТ
# и пояснение к нему в зависимости от попадания в тот или иной
# диапазон. Использовать обработку исключений.
while True:
    try:
        height = float(input('Введите ваш рост в метрах: '))
        if height <= 0:
            print('Введено отрицательное значение или 0, пожалуйста'
                  ' введите другое значение')
            continue
        if height >= 3.00:
            print('Введено слишком большое значение, пожалуйста'
                  ' введите другое значение')
            continue
        break
    except (ValueError, NameError):
        print('Пожалуйста, введите числовое значение.')

while True:
    try:
        weight = float(input('Введите ваш вес в килограммах: '))
        if weight <=0:
            print('Введено значение меньше или равное 0, пожалуйста'
                  ' введите другое значение')
            continue
        if weight >= 1000:
            print('Введено слишком большое значение, пожалуйста'
                  ' введите другое значение')
            continue
        break
    except (ValueError, NameError):
        print('Пожалуйста, введите числовое значение.')


index = weight / (height ** 2)
print(f'Индекс массы вашего тела составляет {round(index, 2)}.')

if index < 16:
    print('У вас наблюдается ярко выраженный дефицит массы тела.')
elif 16 <= index < 18.5:
    print('У вас наблюдается  дефицит массы тела.')
elif 18.5 <= index < 25:
    print('Индекс массы вашего тела находится в норме.')
elif 25 <= index < 30:
    print('Исходя из индекса массы вашего тела можно сделать вывод, что у вас предожирение.')
elif 30 <= index < 35:
    print('Исходя из индекса массы вашего тела можно сделать вывод, что вы страдаете ожирением 1-ой степени.')
elif 35 <= index < 40:
    print('Исходя из индекса массы вашего тела можно сделать вывод, что вы страдаете ожирением 2-ой степени.')
elif index >= 40:
    print('Исходя из индекса массы вашего тела можно сделать вывод, что вы страдаете ожирением 3-ой степени.')

# 2. Реализовать программу с функционалом калькулятора для операций
# над двумя числами. Числа и операция вводятся пользователем с
# клавиатуры. Использовать обработку исключений.
while True:
    try:
        first_parameter = float(input('Введите первое число: '))
        break
    except (ValueError, NameError):
        print('Пожалуйста, введите числовое значение.')

while True:
    try:
        second_parameter = float(input('Введите второе число: '))
        break
    except (ValueError, NameError):
        print('Пожалуйста, введите числовое значение.')

while True:
    operation = input('Введите необходимую операцию +, -, /, *: ')
    if operation in ['+', '-', '/', '*']:
        break
    else:
        print('Вы не выбрали необходимую функцию')
        continue

if operation == '+':
    result = first_parameter + second_parameter
    print(result)
if operation == '-':
    result = first_parameter - second_parameter
    print(result)
if operation == '*':
    result = first_parameter * second_parameter
    print(result)
if operation == '/':
    try:
        result = first_parameter / second_parameter
        print(result)
    except ZeroDivisionError:
        print('Нельзя разделить на 0')