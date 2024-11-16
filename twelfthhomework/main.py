#    Выполняем валидацию атрибутов при создании книги. Для валидации
#    создаем собственные исключения.

from classes import Book, Library

book1 = Book(pages = 120, year = 2007, author = 'Pushkin', price = 25.99)
book1.increment()
print(book1)

book2 = Book(pages = 200, year = 2013, author = 'Oruell', price = 45.99)
book2.increment()
print(book2)

book3 = Book(pages = 75, year = 1998, author = 'Shekspire', price = 22.99)
book3.increment()
print(book3)

print(book1.price < book2.price)
print(book1.price < book3.price)
print(book2.price < book3.price)

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.author_search("Oruell", "Shekspire"))
print(library.get_book_info())
