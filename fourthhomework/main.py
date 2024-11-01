import math

print('Задание №1')
a = 4
b = 5
y = ((pow(a, 2) / 3) + ((pow(a, 2) + 4) / b) + (math.sqrt(pow(a, 2) + 4) / 4)
     + math.sqrt(pow(pow(a, 2) + 4, 3)) / 4)
print(f'а) С учётом значений а = {a} и b = {b}, получаем значение y равное '
      f'{round(y, 2)}')

degrees = 90
x = math.radians(degrees)
y = math.cos(x) + math.sin(x)
print(f'b) Учитывая, что переменная x равна {degrees} градусов, получаем '
      f'значение y равное {round(y, 2)}')

degrees = 45
x = math.radians(degrees)
y = math.cbrt(pow(math.cos(pow(x,2)), 2) + pow(math.sin(2*x - 1), 2))
print(f'c) Учитывая, что переменная x равна {degrees} градусов, получаем '
      f'значение y равное {round(y, 2)}')

degrees = 30
x = math.radians(degrees)
y = 5 * x + 3 * pow(x, 2) * math.sqrt(1 + pow(math.sin(x), 2))
print(f'd) Учитывая, что переменная x равна {degrees} градусов, получаем '
      f'значение y равное {round(y, 2)}')
print()

# Не совсем понял во втором задании для чего испольузется переменная i
# (так как отсутствует в формуле),поэтому не использовал её
print('Задание №2')
p = 0.04
p_st = str(p)
s = 40000
n = 9
print(f'Месячная процентная ставка равна {p_st[-1]}%, сумма займа составляет'
      f' {s} бел. рублей, кредит взят на {n} месяцев.')
m = (s * p * pow(1 + p, n))/(pow(1 + p, n) - 1)
print(f'С учётом данных показателей получаем, что ежемесячная выплата равна '
      f'{round(m, 2)} бел. рублей')
full = m * n
print(f'Всего пользователь заплатит банку сумму равную {round(full, 2)} бел. '
      f'рублей')
over = full - s
print(f'Переплата составит {round(over, 2)} бел. рублей')
print()

print('Задание №3')
first_r = 2900
first_v = 24500
print(f'Радиус орбиты первой планеты составляет {first_r} млн. км., а её '
      f'орбитальная скорость {first_v} км/ч.')
second_r = 110
second_v = 126000
print(f'Радиус орбиты второй планеты составляет {second_r} млн. км., а её '
      f'орбитальная скорость {second_v} км/ч.')
first_rkm = first_r * pow(10, 6)
second_rkm = second_r * pow(10, 6)
first_l = (2 * first_rkm * math.pi) / first_v
second_l = (2 * second_rkm * math.pi) / second_v
print(f'Длина года на первой планете составляет {int(first_l)} часов')
print(f'Длина года на второй планете составляет {int(second_l)} часов')
if first_l > second_l:
    print('Год на первой планете длиннее, чем на второй')
elif first_l < second_l:
    print ('Год на первой планете короче, чем на второй')
else:
    print('Год на первой планете и на второй одинаковый')