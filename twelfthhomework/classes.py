# - Класс Book:
#    Используем dataclass для создания книги.
#    Атрибуты: book_id, pages, year, author, price. Book_id по умолчанию
#    None присваивается только при добавлении книги в библиотеку.

#    Выполняем валидацию атрибутов при создании книги. Для валидации
#    создаем собственные исключения.
#    Реализуем метод сравнения книг по цене.
from dataclasses import dataclass, field

@dataclass (order = True)
class Book:
    pages: int
    year: int
    author: str
    price: float
    book_id: int = field(default = 0, init = False)

    def increment(self):
        self.book_id += 1
        Book.book_id = self.book_id

    def __str__(self):
        return (f"Книга под номером {self.book_id} имеет {self.pages} "
              f"страниц, издана в {self.year} году, её автором является"
              f" {self.author}, а её стоимость составляет {self.price} рублей.")

    def __post_init__(self):
        if self.pages <= 0:
            print("Количество страниц на может быть меньше нуля")
            raise PagesError
        if self.year <= 0 or self.year > 2024:
            raise YearError
        if self.price <= 0:
            raise PriceError

# - Класс Library:
#    Хранит книги и автоматически присваивает каждой книге уникальный id.
#    Имеет методы add_book и get_book_info.
#    Поддерживает метод для поиска книг по автору с перегрузкой: можно
#    искать по одному автору или передавать список авторов.
class Library:
    def __init__(self):
        self.books = []
        self.id = 0

    def add_book(self, book: Book):
        # self.id = Book.book_id
        self.id += 1
        self.books.append(book)

    def author_search(self, *args):
        found =[]
        for i in self.books:
            if i.author in args:
                found.append(i)
        if found:
            return found
        else:
            return "Не найдено"

    def get_book_info(self):
        if self.books:
            for i in self.books:
                print(str(i))
            return "Вывод книг окончен"
        else:
            return "Пусто"


class PagesError(Exception):
    pass

class YearError(Exception):
    pass

class PriceError(Exception):
    pass



# class MyExceptions():
