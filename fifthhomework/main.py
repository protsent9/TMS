# 1. Создайте квадратную матрицу и заполните её числами с шагом 2, начиная от 100.
i = int(input(f'Введите порядок матрицы: '))
matrix = []
item = 98

for row in range(i):
    matrix_row = []
    for columns in range(i):
        item += 2
        matrix_row.append(item)
    matrix.append(matrix_row)

print('Матрица: ')
for row in matrix:
    print(row)

# 2. Вывести матрицу в консоль по примеру.
for row in matrix:
    print(*row)

# 3. Транспонирование матрицы (перестановка строк и столбцов).
print('Матрица: ')
for row in matrix:
    print(row)

trans_matrix = []

for columns in range(len(matrix[0])):
    new_row = []
    for row in range(len(matrix)):
        new_row.append(matrix[row][columns])
    trans_matrix. append(new_row)

print('Транспонированная матрица: ')
for row in trans_matrix:
    print(row)

# 4. Маша хочет накопить на телефон, который стоит N денег. Маша может
# откладывать k рублей каждый день, кроме воскресенья (в воскресенье
# она тратит эти деньги на поход в кино). Маша начинает копить в
# понедельник. За сколько дней она накопит нужную сумму?
n = int(input('Введите сумму, за которую планируется покупка телефона: '))
k = int(input('Введите сумму, которую Маша откладывает ежедневно: '))
day = 0
s = 0

while s < n:
    day += 1
    if day % 7 == 0:
        s = s
    else:
        s += k

print(f'Маша накопит на телефон через {day} дней.')

# 5. Реализовать вывод последовательности чисел Фибоначчи (1 1 2 3 5 8
# 13 21 34 55 89 ...), где каждое следующее число является суммой двух
# предыдущих.
n = int(input('Введите сколько чисел вы хотите вывести из последовательности Фибоначчи: '))
number = 1
sequence = []
a = 0
b = 1
sequence.append(a)
sequence.append(b)

for i in range(n):
    a = int(sequence[len(sequence) - 2])
    b = int(sequence[-1])
    c = a + b
    sequence.append(c)

print(*sequence)

# 6. Дан список чисел. Реализовать программу, которая посчитает сумму
# всех чисел в списке, а также найдет минимальный и максимальный элементы
first_list = [16, 34, 245, 97, 73, 165]
summa = 0
minimum = first_list[0]
maximum = first_list[0]

for i in range(len(first_list)):
    summa +=  first_list[i]

for j in first_list:
    if j < minimum:
        minimum = j
    if j > maximum:
        maximum = j

print(f'Сумма элементов списка равна {summa}')
print(f'Минимальное число в списке {minimum}')
print(f'Максимальное число в списке {maximum}')

# 7. Дан список чисел. Реализовать программу, которая проверит, все ли
# числа в списке уникальны (встречаются только один раз). Программа
# должна вывести результат проверки, и, если не все элементы уникальны,
# вывести дублирующиеся элементы и количество их повторений в списке.
second_list = [1, 2, 3, 4, 4, 5, 4, 12, 1, 57]
# Список без повторений
# second_list = [1, 2, 3, 4, 12, 57]

indicator = False
checked_numbers = set()

for i in range(len(second_list)):
    if second_list[i] in checked_numbers:
        continue

    repeat_number = 1
    for j in range(i + 1, len(second_list)):
        if second_list[i] == second_list[j]:
            repeat_number += 1
            indicator = True

    if repeat_number > 1:
        print(f'Число {second_list[i]} повторяется {repeat_number} раза')
    checked_numbers.add(second_list[i])

if indicator == 0:
    print('Повторяющихся чисел в списке нет')

# 8. Дан список чисел, отсортированных по возрастанию. На вход принимается
# значение, равное одному из элементов списка. Реализовать алгоритм
# бинарного поиска, на выходе программа должна вывести позицию искомого
# элемента в исходном списке.
third_list = [1,2,3,4,5,6]
search = int(input(f'Введите число, позицию которого ищете: '))
left = 0
right = len(third_list) - 1

while left <= right:
    middle = (left + right) // 2

    if third_list[middle] == search:
        print(f'Данное число найдено на позиции: {middle}.')
        break
    elif third_list[middle] < search:
        left = middle + 1
    else:
        right = middle - 1
else:
    print(f'Данное число {search} не найдена в списке.')