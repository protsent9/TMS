# 1. Дан список чисел. С помощью map() получить список, где каждое
# число из исходного списка переведено в строку.
my_list = [1, 2, 3]
print(list(map(lambda x: str(x), my_list)))

# 2. Дан список чисел. С помощью filter() получить список тех
# элементов из исходного списка, значение которых больше 0.
second_list =[1, -2, 23, -5, 3, 5, 3, -9]
print(list(filter(lambda x: x > 0, second_list)))

# 3. Дан список строк. С помощью filter() получить список тех строк
# из исходного списка, которые являются палиндромами (читаются в обе
# стороны одинаково, например, ’abccba’)
third_list = ['abccba', 'aderda', 'ghaahg', 'koook', 'lpsslp', 'sdaads']
print(list(filter(lambda x: x == x[::-1], third_list)))

# 4. Сделать декоратор, который измеряет время, затраченное на
# выполнение декорируемой функции.
import time

def time_func(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        difference = end - start
        print(f'На исходную функцию потребовалось {difference} секунд.')
    return wrapper


@time_func
def input_func(a, b):
    c =  a + b
    print(f'Результат сложения равен: {c}')

input_func(5, 7)

# 5. Используя map() и reduce() посчитать площадь квартиры, имея на
# входе характеристики комнат квартиры. Пример входных данных:
# rooms = [
# {"name": ”Kitchen", "length": 6, "width": 4},
# {"name": ”Room 1", "length": 5.5, "width": 4.5},
# {"name": ”Room 2", "length": 5, "width": 4},
# {"name": ”Room 3", "length": 7, "width": 6.3},
# ]
from functools import reduce

rooms = [
 {"name": 'Kitchen', 'length': 6, 'width': 4},
 {"name": 'Room 1', 'length': 5.5, 'width': 4.5},
 {"name": 'Room 2', 'length': 5, 'width': 4},
 {"name": 'Room 3', 'length': 7, 'width': 6.3},
]

print('Данные по квартире: ')
for row in rooms:
    name = row['name']
    length = row['length']
    width = row['width']
    print(f'Комната: {name}, длина: {length}, ширина: {width}')

print()

room_area = list(map(lambda x: x['length'] * x['width'], rooms))
rooms_area = reduce(lambda x,y: x + y, room_area)
print(f'Площадь квартиры равна: {rooms_area}')