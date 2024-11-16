# 1. Создать класс MyTime. Атрибуты: hours, minutes, seconds.
# Методы: переопределить магические методы сравнения(==, !=, >=, <=, <, >),
# сложения, вычитания, умножения на число, вывод на экран. Перегрузить
# конструктор на обработку входных параметров вида: одна строка, три числа,
# другой объект класса MyTime, и отсутствие входных параметров. Реализовать
# нормальное отображение времени.
# class MyTime:
#     def __init__(self, hours, minutes, seconds):
#         if hours > 24 or hours < 0:
#             print("Your hours type is incorrect.")
#             exit()
#         if minutes > 59 or minutes < 0:
#             print("Your minutes type is incorrect.")
#             exit()
#         if seconds > 59 or seconds < 0:
#             print("Your seconds type is incorrect.")
#             exit()
#
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     # Магический метод <
#     def __lt__(self, second):
#         if second.hours > 24 or second.hours < 0:
#             print("Your hours type is incorrect.")
#             exit()
#         if second.minutes > 59 or second.minutes < 0:
#             print("Your minutes type is incorrect.")
#             exit()
#         if second.seconds > 59 or second.seconds < 0:
#             print("Your seconds type is incorrect.")
#             exit()
#
#         if self.hours < second.hours:
#             return "That's true"
#         elif self.hours == second.hours:
#             if self.minutes < second.minutes:
#                 return "That's true"
#             elif self.minutes == second.minutes:
#                 if self.seconds < second.seconds:
#                     return "That's true"
#                 else:
#                     return "That's false"
#             else:
#                 return "That's false"
#         else:
#             return "That's false"
#
#     # Магический метод <=
#     def __le__(self, second):
#         if second.hours > 24 or second.hours < 0:
#             print("Your hours type is incorrect.")
#             exit()
#         if second.minutes > 59 or second.minutes < 0:
#             print("Your minutes type is incorrect.")
#             exit()
#         if second.seconds > 59 or second.seconds < 0:
#             print("Your seconds type is incorrect.")
#             exit()
#
#         if self.hours <= second.hours:
#             return "That's true"
#         else:
#             return "That's false"
#
#     # Магический метод ==
#     def __eq__(self, second):
#         if second.hours > 24 or second.hours < 0:
#             print("Your hours type is incorrect.")
#             exit()
#         if second.minutes > 59 or second.minutes < 0:
#             print("Your minutes type is incorrect.")
#             exit()
#         if second.seconds > 59 or second.seconds < 0:
#             print("Your seconds type is incorrect.")
#             exit()
#
#         if self.hours == second.hours:
#             if self.minutes == second.minutes:
#                 if self.seconds == second.seconds:
#                     return "That's true"
#                 else:
#                     return "That's false"
#             else:
#                 return "That's false"
#         else:
#             return "That's false"
#
#     # Магический метод !=
#     def __ne__(self, second):
#         if second.hours > 24 or second.hours < 0:
#             print("Your hours type is incorrect.")
#             exit()
#         if second.minutes > 59 or second.minutes < 0:
#             print("Your minutes type is incorrect.")
#             exit()
#         if second.seconds > 59 or second.seconds < 0:
#             print("Your seconds type is incorrect.")
#             exit()
#
#         if self.hours != second.hours:
#             return "That's true"
#         else:
#             if self.minutes != second.minutes:
#                 return "That's true"
#             else:
#                 if self.seconds != second.seconds:
#                     return "That's true"
#                 else:
#                     return "That's false"
#
#     # Магический метод >=
#     def __ge__(self, second):
#         if second.hours > 24 or second.hours < 0:
#             print("Your hours type is incorrect.")
#             exit()
#         if second.minutes > 59 or second.minutes < 0:
#             print("Your minutes type is incorrect.")
#             exit()
#         if second.seconds > 59 or second.seconds < 0:
#             print("Your seconds type is incorrect.")
#             exit()
#
#         if self.hours >= second.hours:
#             if self.minutes >= second.minutes:
#                 if self.seconds >= second.seconds:
#                     return "That's true"
#                 else:
#                     return "That's false"
#             else:
#                 return "That's false"
#         else:
#             return "That's false"
#
#     # Магический метод >
#     def __qt__(self, second):
#         if second.hours > 24 or second.hours < 0:
#             print("Your hours type is incorrect.")
#             exit()
#         if second.minutes > 59 or second.minutes < 0:
#             print("Your minutes type is incorrect.")
#             exit()
#         if second.seconds > 59 or second.seconds < 0:
#             print("Your seconds type is incorrect.")
#             exit()
#
#         if self.hours > second.hours:
#             return "That's true"
#         elif self.hours == second.hours:
#             if self.minutes > second.minutes:
#                 return "That's true"
#             elif self.minutes == second.minutes:
#                 if self.seconds > second.seconds:
#                     return "That's true"
#                 else:
#                     return "That's false"
#             else:
#                 return "That's false"
#         else:
#             return "That's false"
#
#     # Магический метод сложения
#     def __add__(self, second):
#         add_seconds = self.seconds + second.seconds
#         add_minutes = self.minutes + second.minutes + (add_seconds // 60)
#         add_hours = self.hours + second.hours + (add_minutes // 60)
#
#         add_seconds %= 60
#         add_minutes %= 60
#         add_hours %= 24
#
#         return "Полученное время равно " + str(add_hours) + ":" + str(add_minutes) + ":" + str(add_seconds)
#
#     # Магический метод вычитания
#     def __sub__(self, second):
#         sub_seconds = self.seconds - second.seconds
#         sub_minutes = self.minutes - second.minutes
#         sub_hours = self.hours - second.hours
#
#         if sub_seconds < 0:
#             sub_seconds += 60
#             sub_minutes -= 1
#
#         if sub_minutes < 0:
#             sub_minutes += 60
#             sub_hours -= 1
#
#         if sub_hours < 0:
#             sub_hours += 24
#
#         return "Полученное время равно " + str(sub_hours) + ":" + str(sub_minutes) + ":" + str(sub_seconds)
#
#     # Магический метод умножения на число
#     def __mul__(self, number):
#         mul_seconds = self.seconds * number
#         mul_minutes = self.minutes * number + (mul_seconds // 60)
#         mul_hours = self.hours * number + (mul_minutes // 60)
#
#         mul_seconds %= 60
#         mul_minutes %= 60
#         mul_hours %= 24
#
#         return "Полученное время равно " + str(mul_hours) + ":" + str(mul_minutes) + ":" + str(mul_seconds)
#
#     # Вывод на экран
#     def __str__(self):
#         return "Время " + str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)
#
#
# first_time = MyTime(24,25,15)
# second_time = MyTime(24,25,14)
# print(first_time)

# 2.  Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость
# (по умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
# скорости(скорость - 5), стоп (сброс скорости на 0), отображение скорости,
# разворот(изменение знака скорости). Все атрибуты приватные. Сделать для
# каждого атрибута getter и setter используя декораторы.
# class Car:
#     def __init__(self, mark, model, year, speed = 0):
#         self.__mark = mark
#         self.__model = model
#         self.__year = year
#         self.__speed = speed
#
#     def speed_up (self):
#         self.__speed += 5
#
#     def speed_down (self):
#         self.__speed -= 5
#
#     def speed_reverse (self):
#         self.__speed *= -1
#
#     def speed_zero (self):
#         self.__speed = 0
#
#     @property
#     def speed(self):
#         return self.__speed
#
#     @speed.setter
#     def speed(self, number):
#         self.__speed = number
#
#     @property
#     def mark(self):
#         return self.__mark
#
#     @mark.setter
#     def mark(self, name):
#         self.__mark = name
#
#     @property
#     def model(self):
#         return self.__model
#
#     @model.setter
#     def model(self, name):
#         self.__model = name
#
#     @property
#     def year(self):
#         return self.__year
#
#     @year.setter
#     def year(self, number):
#         self.__year = number
#
# honda = Car("Honda", "Civic", "2003")
# print(honda.speed)      # Значение скорости по умолчанию
#
# honda.speed = 10        # Использование сеттера для скорости
# print(honda.speed)
#
# honda.speed_up()        # Увеличение скорости на 5
# print(honda.speed)
#
# honda.speed_down()      # Уменьшение скорости на 5
# print(honda.speed)
#
# honda.speed_reverse()   # Разворот, смена знака скорости
# print(honda.speed)
#
# honda.speed_zero()      # Стоп, сброс скорости
# print(honda.speed)
#
# print(honda.mark)       # Изначальное наименование марки
# honda.mark = "Toyota"   # Использование сеттера для марки
# print(honda.mark)
#
# print(honda.model)      # Изначальная модель
# honda.model = "RAV"     # Использование сеттера для модели
# print(honda.model)
#
# print(honda.year)       # Изначальный год изготовления
# honda.year = "2014"     # Использование сеттера для года изготовления
# print(honda.year)
#
# print(honda.mark, honda.model, honda.year)

# 3. Разработать класс SuperStr, который наследует функциональность
# стандартного типа str и содержит два новых метода:
class SuperStr(str):
    # - метод is_repeatance(s), который принимает некоторую строку и возвращает
    # True или False в зависимости от того, может ли текущая строка быть получена
    # целым количеством повторов строки s. Считать, что пустая строка не содержит
    # повторов.
    def is_repeatance(self, s):
        if len(s) == 0:
            return False
        elif s * (len(self) // len(s)) == self:
            return True
        else:
            return False

    # - метод is_palindrom(), который возвращает True или False в зависимости от
    # того, является ли строка палиндромом вне зависимости от регистра. Пустую
    # строку считать палиндромом.
    def is_palindrom(self):
        s = self.upper()
        if s == s[::-1]:
            return True
        elif len(s) == 0:
            return True
        else:
            print("False")
            return False

string = SuperStr("abbaabba")
print(string.is_repeatance("abba"))     # Метод  is_repeatance

print(string.is_palindrom())            # Метод is_palindrom
