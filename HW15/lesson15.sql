-- Создайте таблицу authors с полями id, first_name и last_name. 
-- Используйте PRIMARY KEY для поля id
CREATE TABLE authors (
  id int primary key,
  first_name varchar(50),
  last_name varchar(50)
);

-- Добавьте несколько авторов в таблицу authors
INSERT INTO authors (id, first_name, last_name) 
VALUES (1, 'Lev', 'Tolstoy'),
  (2, 'Jane', 'Austen'),
  (3, 'George', 'Orwell'),
  (4, 'Agatha', 'Christie'),
  (5, 'Mark', 'Twain');

SELECT * FROM authors;

-- Создайте таблицу books с полями id, title, author_id и
-- publication_year. Используйте PRIMARY KEY для поля id и
-- FOREIGN KEY для поля author_id, ссылаясь на таблицу authors
CREATE TABLE books (
  id int primary key,
  title varchar(50),
  author_id int,
  publication_year date,
  foreign key (author_id) references authors(id)
);

-- Добавьте несколько книг в таблицу books, указывая авторов из
-- таблицы authors
INSERT INTO books (id, title, author_id, publication_year) 
VALUES (1, 'War and Peace', 1, '1865-01-01'),
  (2, 'Anna Karenina', 1, '1878-01-01'),
  (3, 'Pride and Prejudice', 2, '1813-01-28'),
  (4, '1984', 3, '1949-06-08'),
  (5, 'Murder on the Orient Express', 4, '1934-01-01'),
  (6, 'Sense and Sensibility ', 2, '1811-01-01'),
  (7, 'Bible ', null, null);

SELECT * FROM books;

-- Создайте таблицу sales с полями id, book_id и quantity.
-- Используйте PRIMARY KEY для поля id и FOREIGN KEY для
-- поля book_id, ссылаясь на таблицу books
CREATE TABLE sales (
  id int primary key,
  book_id int,
  quantity int,
  foreign key (book_id) references books(id)
);

-- Добавьте записи о продажах книг в таблицу sales
INSERT INTO sales (id, book_id, quantity) 
VALUES 
  (1, 1, 15),
  (2, 2, 20),
  (3, 3, 32),
  (4, 4, 21),
  (5, 5, 17),
  (6, 7, 50);
    
SELECT * FROM sales;

-- Используйте INNER JOIN для получения списка всех книг и их
-- авторов.
SELECT books.title AS book, authors.last_name as author
FROM books
INNER JOIN authors ON books.author_id = authors.id;

-- Используйте LEFT JOIN для получения списка всех авторов и
-- их книг (включая авторов, у которых нет книг).
SELECT books.title AS book, authors.last_name as author
FROM authors
LEFT JOIN books ON books.author_id = authors.id;

-- Используйте RIGHT JOIN для получения списка всех книг и их
-- авторов, включая книги, у которых автор не указан
SELECT books.title AS book, authors.last_name as author
FROM authors
RIGHT JOIN books ON books.author_id = authors.id;

-- Используйте INNER JOIN для связывания таблиц authors, books 
-- и sales, чтобы получить список всех книг, их авторов и продаж
SELECT books.title AS book, authors.last_name as author, sales.quantity as quantity
FROM books
INNER JOIN authors ON books.author_id = authors.id
INNER JOIN sales ON sales.book_id = books.id;

-- Используйте LEFT JOIN и функции агрегации для определения
-- общего количества проданных книг каждого автора, включая
-- авторов без продаж
SELECT books.title AS book, authors.last_name as author, sales.quantity as quantity
FROM authors
LEFT JOIN books ON authors.id = books.author_id
LEFT JOIN sales ON books.id = sales.book_id;
