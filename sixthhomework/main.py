# 1. Дан список чисел, отсортированных по возрастанию. На вход
# принимается значение, равное одному из элементов списка. Реализовать
# функцию, выполняющую рекурсивный алгоритм бинарного поиска, на выходе
# программа должна вывести позицию искомого элемента в исходном списке.
def research(my_list, number, index = 0):
    if index >= len(list_a):
        print(f'Значение {number} в списке не найдено')
        return

    if number == my_list[index]:
        print(f'Значение {number} находится в списке на позиции {index}')
        return
    else:
        research(my_list, number, index + 1)

list_a = [1, 2, 3, 4, 5, 6]
print(f'Дан список чисел: {list_a}')
a = int(input('Введите значение элемента, которое ищете: '))
research(list_a, a)

# 2. Программа получает на вход число в десятичной системе счисления.
# Реализовать функцию, которая переводит входное число в двоичную
# систему счисления. Допускается реализация функции как в рекурсивном
# варианте, так и с итеративным подходом.
def translate_function(decimal_number):
    if decimal_number == 0:
        return 0

    if decimal_number == 1:
        return 1
    else:
        remainder = decimal_number % 2 #остаток
        quotient = decimal_number // 2 #частное
        return str(translate_function(quotient)) + str(remainder)

number = int(input('Введите число в десятичной системе счисления: '))
binary = translate_function(number)
print(f"Двоичное представление числа {number}: {binary}")

# 3. Программа получает на вход число. Реализовать функцию, которая
# определяет, является ли это число простым (делится только на единицу
# и на само себя).
def determine_function(number, divisor = 1, count = 0):
    if number == 1:
       print(f'Число {number} простым не является')
       return

    if divisor > number:
        if count == 2:
            print(f'Число {number} является простым')
        else:
            print(f'Число {number} простым не является')
        return

    if number % divisor == 0:
        count += 1

    determine_function(number, divisor + 1, count)

a = int(input('Введите число на проверку на проверку: '))
determine_function(a)

# 4. Программа получает на вход два числа и находит их НОД (наибольший
# общий делитель). Пример: на вход подаются числа 12 и 18, их НОД равен 6.
def nod_function(number_a, number_b, divisor = 1):
    if number_a == 0:
        print('Первое число является нулём, нахождение НОД невозможно')
    elif number_b == 0:
        print('Второе число является нулём, нахождение НОД невозможно')
    else:
        if number_a % divisor == 0 and number_b % divisor == 0:
            max_divisor = divisor

        if divisor == number_a or divisor == number_b:
            print(f'Наибольший общий делитель равен {max_divisor}')
            return
        else:
            nod_function(number_a, number_b, divisor + 1)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
nod_function(a, b)
'''
# 5. Программа получает на вход строку – сообщение и указание, что нужно
# сделать: шифровать или дешифровать. Реализовать две функции: первая
# шифрует заданное сообщение шифром Цезаря, вторая – расшифровывает. В
# зависимости от выбора пользователя (шифровать или дешифровать)
# вызывается соответствующая функция, результат выводится в консоль.
def encrypt_function(text, shift):
    
def decrypt_function(text, shift):
    
text = str(input('Введите текст надо которым хотите совершить преобразование: '))
shift = int(input('Введите цифру сдвига: '))
action = str(input('Что вы хотите сделать с сообщением: зашифровать или дешифровать: '))
if action == 'зашифровать':
    encrypt_function(text, shift)
elif action == 'дешифровать':
    decrypt_function(text, shift)
'''
# 7. Реализовать функцию, которая создаёт матрицу размером M строк на N
# столбцов и заполняет её рандомными числами.
import random

def matrix_function(size_a, size_b):
    matrix = []
    for row in range(size_a):
        matrix_row = []
        for columns in range(size_b):
            matrix_row.append(random.randint(10,99))
        matrix.append(matrix_row)

    print('Полученная матрица: ')
    for row in matrix:
        print(row)


height = int(input('Введите высоту матрицы: '))
width = int(input('Введите ширину матрицы: '))
matrix_function(height, width)


# 8. Реализовать функцию, которая находит минимальный и максимальный
# элементы в матрице (матрица M x N). Вывести в консоль индексы
# найденных элементов.
import random

def extrema_function(size_a, size_b):
    matrix = []
    for row in range(size_a):
        matrix_row = []
        for columns in range(size_b):
            matrix_row.append(random.randint(1, 20))
        matrix.append(matrix_row)

    print('Полученная матрица: ')
    for row in matrix:
        print(row)

    max_value = matrix[0][0]
    min_value = matrix[0][0]
    max_index = (0,0)
    min_index = (0,0)

    for i in range(size_a):
        for j in range(size_b):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_index = (i, j)
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_index = (i, j)

    print(f'Максимальное значение {max_value} находится под индексом'
          f' {max_index}, минимальное значение {min_value} находится '
          f'под индексом {min_index}')

height = int(input('Введите высоту матрицы: '))
width = int(input('Введите ширину матрицы: '))
extrema_function(height, width)

# 9. Реализовать функцию, которая находит сумму элементов матрицы
# (матрица M x N). Определить, какую долю в общей сумме (процент)
# составляет сумма элементов каждого столбца.
import random

def summa_function(size_a, size_b):
    matrix = []
    for row in range(size_a):
        matrix_row = []
        for columns in range(size_b):
            matrix_row.append(random.randint(1, 5))
        matrix.append(matrix_row)

    print('Полученная матрица: ')
    for row in matrix:
        print(row)

    summa = 0

    for i in range(size_a):
        for j in range(size_b):
            summa += matrix[i][j]
    print(f'Сумма всех элементов матрицы равна {summa}')

    for j in range(size_b):
        column_sum = 0
        for i in range(size_a):
            column_sum += matrix[i][j]
        print(f'Сумма {j + 1} столбца равна {column_sum}')
        dirty_percent = (column_sum / summa) * 100
        percent = round(dirty_percent, 2)
        print(f'Сумма {j + 1} столбца составляет {percent}% от суммы всей матрицы')

height = int(input('Введите высоту матрицы: '))
width = int(input('Введите ширину матрицы: '))
summa_function(height, width)

# 12. Программа получает на вход число H. Реализовать функцию, которая
# определяет, какие столбцы имеют хотя бы одно такое же число, а какие
# не имеют (матрица M x N).
import random

def contain_column(size_a, size_b, number):
    matrix = []
    for row in range(size_a):
        matrix_row = []
        for columns in range(size_b):
            matrix_row.append(random.randint(1, 5))
        matrix.append(matrix_row)

    print('Полученная матрица: ')
    for row in matrix:
        print(row)

    for j in range(size_b):
        count = 0
        for i in range(size_a):
            if matrix[i][j] == number:
                count += 1
        if count >= 1:
            print(f'Столбец {j+1} содержит данное число')
        else:
            print(f'Столбец {j+1} не содержит данное число')

height = int(input('Введите высоту матрицы: '))
width = int(input('Введите ширину матрицы: '))
my_number = int(input('Введите число: '))
contain_column(height, width, my_number)

# 13. Реализовать функцию, которая находит сумму элементов на главной
# диагонали и сумму элементов на побочной диагонали (матрица M x N).
import random
def diagonal_summa(size_a, size_b):
    matrix = []
    for row in range(size_a):
        matrix_row = []
        for columns in range(size_b):
            matrix_row.append(random.randint(1, 10))
        matrix.append(matrix_row)

    print('Полученная матрица: ')
    for row in matrix:
        print(row)

    main_summa = 0

    if size_a <= size_b:
        for i in range(size_a):
            main_summa += matrix[i][i]
    elif size_a > size_b:
        for i in range(size_b):
            main_summa += matrix[i][i]
    print(f'Сумма элементов главной диагонали {main_summa}')

    secondary_summa = 0

    if size_a >= size_b:
        for i in range(size_b):
            secondary_summa += matrix[i][size_b - 1 - i]
    elif size_a < size_b:
        for i in range(size_a):
            secondary_summa += matrix[i][size_b - 1 - i]
    print(f'Сумма элементов побочной диагонали {secondary_summa}')

height = int(input('Введите высоту матрицы: '))
width = int(input('Введите ширину матрицы: '))
diagonal_summa(height, width)

# 14. Дана матрица M x N. Исходная матрица состоит из нулей и единиц.
# Реализовать функцию, которая добавит к матрице ещё один столбец,
# элементы которого делают количество единиц в соответствующей строке чётным.
import random

def add_column(size_a, size_b):
    matrix = []
    for row in range(size_a):
        matrix_row = []
        for columns in range(size_b):
            matrix_row.append(random.randint(0, 1))
        matrix.append(matrix_row)

    print('Исходная матрица: ')
    for row in matrix:
        print(row)

    for row in matrix:
        summa = 0
        for j in row:
            if j == 1:
                summa += 1

        if summa % 2 == 0:
            row.append(0)
        else:
            row.append(1)

    print('Полученная матрица: ')
    for row in matrix:
        print(row)


height = int(input('Введите высоту матрицы: '))
width = int(input('Введите ширину матрицы: '))
add_column(height, width)