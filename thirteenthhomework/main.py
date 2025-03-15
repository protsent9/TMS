# 1. Реализовать программу для бесконечной циклической последовательности
# чисел (например, 1-2-3-1-2-3-1-2...). Последовательность реализовать с
# помощью генераторной функции, количество чисел для вывода задаётся
# пользователем с клавиатуры.
# def generator(repeat):
#     x = 0
#     while x < repeat:
#         for number in range(1, 4):
#             if x >= repeat:
#                 return
#             yield number
#             x += 1
#
# rep = int(input("Введите количество повторений: "))
#
# gen = generator(rep)
# for i in gen:
#     print(i, end = "-")

# 2. Создайте класс Pizza, который содержит следующие  атрибуты: size,
# cheese, pepperoni, mushrooms, onions, bacon.
class Pizza:
    def __init__(self, size=None, cheese=False, pepperoni=False, mushrooms=False, onions=False, bacon=False):
         self.size = size
         self.cheese = cheese
         self.pepperoni = pepperoni
         self.mushrooms = mushrooms
         self.onions = onions
         self.bacon = bacon

    def __str__(self):
        ingredients = []
        if self.cheese:
            ingredients.append("cheese")
        if self.pepperoni:
            ingredients.append("pepperoni")
        if self.mushrooms:
            ingredients.append("mushrooms")
        if self.onions:
            ingredients.append("onions")
        if self.bacon:
            ingredients.append("bacon")
        ingredients_str = ", ".join(ingredients) if ingredients else "no toppings"
        return f"Pizza (Size: {self.size}, Toppings: {ingredients_str})"

# - Создайте класс PizzaBuilder, который использует паттерн «Строитель»
# для создания экземпляра Pizza. Этот класс должен содержать методы для
# добавления каждого из атрибутов Pizza.
class PizzaBuilder:
    def __init__(self):
        self._size = None
        self._cheese = False
        self._pepperoni = False
        self._mushrooms = False
        self._onions = False
        self._bacon = False

    def size(self, size):
        self._size = size
        return self

    def cheese(self):
        self._cheese = True
        return self

    def pepperoni(self):
        self._pepperoni = True
        return self

    def mushrooms(self):
        self._mushrooms = True
        return self

    def onions(self):
        self._onions = True
        return self

    def bacon(self):
        self._bacon = True
        return self

    def build(self):
        return Pizza(
            size = self._size,
            cheese = self._cheese,
            pepperoni = self._pepperoni,
            mushrooms = self._mushrooms,
            onions = self._onions,
            bacon = self._bacon,
        )

# - Создайте класс PizzaDirector, который принимает экземпляр
# PizzaBuilder и содержит метод make_pizza, который использует
# PizzaBuilder для создания Pizza
# class PizzaDirector:
class PizzaDirector1:
    def __init__(self):
        self._builder = PizzaBuilder()

    def make_pizza(self):
        return (self._builder
                .size("Big")
                .cheese()
                .onions()
                .bacon()
                .build()
                )

class PizzaDirector2:
    def __init__(self):
        self._builder = PizzaBuilder()

    def make_pizza(self):
        return (self._builder
                .size("Small")
                .cheese()
                .pepperoni()
                .mushrooms()
                .onions()
                .build()
                )

builder = PizzaBuilder()

director1 = PizzaDirector1()
pizza = director1.make_pizza()
print(pizza)
director2 = PizzaDirector2()
pizza2 = director2.make_pizza()
print(pizza2)

# 3. Паттерн «Фабричный метод»
# - Создайте абстрактный класс Animal, у которого есть абстрактный метод
# speak.
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# - Создайте классы Dog и Cat, которые наследуют от Animal и реализуют
# метод speak.
class Dog(Animal):
    def speak(self):
        return 'Гав'

class Cat(Animal):
    def speak(self):
        return 'Мяу'

# - Создайте класс AnimalFactory, который использует паттерн «Фабричный
# метод» для создания экземпляра Animal. Этот класс должен иметь метод
# create_animal, который принимает строку («dog» или «cat») и возвращает
# соответствующий объект (Dog или Cat).
class AnimalFactory:
    def create_animal(self, animal_type) -> Animal:
        if animal_type == 'Dog' or animal_type == 'dog':
            return Dog()
        if animal_type == 'Cat' or animal_type == 'cat':
            return Cat()

animal = AnimalFactory()

dog = animal.create_animal('dog')
print(dog.speak())

cat = animal.create_animal('cat')
print(cat.speak())





# class MyIter:
#     def __init__(self, start, end):
#         self.end = end
#         self.i = start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.i >= self.end:
#             raise StopIteration
#         value = self.i
#         self.i += 1
#         return value
#
# my_iter = MyIter(1,5)
#
# print(my_iter.__next__())
# print(my_iter.__next__())
# print(my_iter.__next__())
# print(my_iter.__next__())
# print(my_iter.__next__())

# list_gen = [1, 2, 3]
# generator = []
# repeat = int(input())
# x = 0
# while x < repeat:
#     b = 0
#     i = 0
#     for x in range(repeat):
#         i *= 3
#         generator = [i for i in list_gen]
#         b += 1
#
# for a in generator:
#     print(a, end = '-')