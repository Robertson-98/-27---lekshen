# Slash Commands

* \l - вывод списка всех баз данных
* \с - показывает в какой базе данных и через какого пользователя подключились
* \c name_of_db - подключаемся к какой-то базе данных
* \du - список всех юзеров в postges
* alter role "user" with:  -  добовляем права пользователю
* \dt - текущие(список) таблице в этой базе данных  - \d+  таже информация, только подробнее
* \q - выход из субд (psql)



# Создание бд и таблиц
```sql
CREATE DATABASE name_of_bd;
-- создание баз данных
```

```sql
CREATE DATABASE name_of_bd(
    column1 data_types1,
    culumn2 data_types2,
    .....
)
-- создание столбцов в таблице
```

# Удаление баз данных и таблиц

```sql
DROP DATABASE name_of_db;
-- удаление баз данных
```
```sql
DROP TABLE name_of_db;
-- удаление таблиц
```



# Заполнение таблицы

```sql 
INSERT INTO name_of_db VALUES
('яблоки', 80, 'витамины')
('груши', 60, 'минералы')
-- запись данных в таблицу (заполнение всех полей)
```


# Вывод данных из таблицы
```sql
SELECT * FROM name_of_table;
-- вывод всех записей со всеми полями
```

```sql
SELECT column1, column2 FROM name_of_table;
--  вывод конкретных полей
```



# Условия 

```sql
DELETE FROM name_of_table WHERE condition;
-- удаление всех записей из таблицы соответсвующих данному условию
```


```sql
# (короче ilike и like чаше используется в поиске в таблице)
-- like - чувствительный к регистру (World - не пройдет)
SELECT * FROM name_of_table WHERE title ilike '%world%';
-- ilike - не чувствительный к регистру
-- WORLD
-- World
-- worLD
-- hello World
-- world Hello
-- HEllo WORLD hello
SELECT * FROM name_of_table ORDER BY column1;
-- сортировка по определенному полю (по возрастанию ASC)
 SELECT * FROM name_of_table ORDER BY column1 DESC;
-- сортировка по определенному полю (по убыванию DESC)
SELECT * FROM name_of_table LIMIT 10;
-- выводит первые 10 записей
# select * from product  where id > 4 limit 3;
(тут я поставила условие если айдишка больше 4 - букв вытащи мне 3 таких продуктов)
SELECT * FROM name_of_table OFFSET 10;
-- пропускает первые 10 записей
SELECT * FROM name_of_table LIMIT 5 OFFSET; 10
-- пропускает первые 10 записей
-- выбирает следующие 5 записей
```



```sql
SELECT * FROM name_of_table ORDER BY column;
-- сортировка записей по данному полю возврастания 
```

```sql
SELECT * FROM name_of_table ORDER BY column DESC;
-- сортировка записей по данному полю в обратном порядке
```
   

```sql
SELECT * FROM name_of_table LIMIT 10;
-- вывод первых 10 записей 
```

```sql
SELECT * FROM product OFFSET 3
-- данный код пропускает первый 3 записи в таблице и идет дальше
```

# Обновление таблицы
**ADD**	Добавляет столбец в существующую таблицу
**ADD CONSTRAINT**	Добавляет ограничение после того, как таблица уже создана
**ALTER**	Добавляет, удаляет или изменяет столбцы в таблице, а также изменяет данные тип столбца в таблице
**ALTER COLUMN**	Изменяет тип данных столбца в таблице
**ALTER TABLE**	Добавляет, удаляет или изменяет столбцы в таблице

```sql
ALTER TABLE name_of_table DROP COLUMN col_name;
-- удаляет колонки из таблицы
```

```sql
ALTER TABLE name_of_table RENAME COLUMN col_name TO new_col_name
-- переменование колонки в таблице
```

# Ограничения
**unique** - это команда позволяет добовлять только уникальные названия(без повторения), используется всегда в конце названия столбца.
**not null** - эта команда требует обязательного заполнения поля, используется тоже в конце 
**primary key** - это команда накидывает два ограничения в одном (те что выше)б плюс строит биннароное дерево для более быстрого поиска.
**foreing key** - ссылается на PK в другой таблице и проверяет сущ. ли такой id



# Связи
## Виды связи
> Один к одному (one to one)
* один человек - один профиль 
* один автор - одна биография 

> Один ко многим (one to many)
* один блогер - много постов 
* один человек - много отношений
* один продукт - много комментариев 

> Многие ко многим (many to many)
* один разработчик - много проектов, один проект - много разработчиков
* один ученик - много учителей, один учитель - много учеников


## реализация one2many в postgres
```sql
create table blogger(id serial primary key, name varchar(50), email varchar(70), age int);
-- создали таблицу блогер

create table post(id serial, title varchar(100), body text, blogger_id int, 

constraint fk_post_blogger foreign key(blogger_id) references blogger(id));


```

# JOINS
> **JOINS** - инструкция, которая позволяет одним SELECT, брать данные из двух таблиц(у которых есть связанные поля)

> **INNER JOIN (JOIN)** - достаются только те записи у которых есть данные в обоих таблицах

> **FULL JOIN** - достаится все записи и с первой таблицы и второй




"""
create table post(id serial, title varchar(100), body text, blogger_id int, constraint fk_post_blogger foreign key(blogger_id) 
blog(# references blogger(id));  -- этими командами создаем связи"""


## реализация one2one в postgres
```sql
CREATE TABLE author (id SERIAL PRIMARY KEY, name VARCHAR, last_name VARCHAR(70), year DATA);
--СОЗДАЛИ ТАБЛИЦУ

CREATE TABLE autobiography (id SERIAL PRIMARY KEY, published DATE, body TEXT, author_id INT UNIQUE, --что бы создать ONE TO ONE
CONSTRAINT fk_author_bio
FOREIGN KEY (author_id), REFERENCES author (id));
```

## реализация many2many в postgres
```sql
CREATE TABLE developer (id SERIAL PRIMARY KEY, name VARCHAR(50), age INT, experience INT);
--СОЗДАЛИ ТАБЛИЦУ

CREATE TABLE project (id SERIAL PRIMARY KEY, title VARCHAR(100), tz TEXT, deadline DATE);
-- СОЗДАЛИ ВТОРУЮ ТАБЛИЦУ

CREATE TABLE dev_proj (dev_id INT, proj_id INT, CONSTRAINT fk_dev_m2m FOREIGN KEY (dev_id) REFERENCES developer (id),
CONSTRAINT fk_proj_m2m FOREIGN KEY (proj_id) REFERENCES project (id);
)
```


```sql
-- one2one / one2many
SELECT * FROM blogger
JOIN post ON blogger.id = post.blogger_id;
```

```sql
-- many2many
SELECT * FROM developer
JOIN dev_proj ON developer.id = dev_proj.dev_id
JOIN project ON project.id = dev_proj.proj_id;
```


--- pg_dump blog > blog.sql -  код который сохраняет базу данных на компьтер в виде файла sql('blog'-название базы данных)
--- pg_du db_name < file.sql - код который сохраняет переводит файл компьтера в базу данных psql.



# Агрегатные функции
> все агрегатные функции мы используем с GROUP BY

> **SUM** - считает сумму всех записей в сгруппированном поле
```sql
SELECT customer.name, SUM(product.price) FROM customer
JOIN cart ON customer.id = cart.customer_id
JOIN product ON product.id = cart.product_id
GROUP BY (customer.id) ;

    name    | sum  
------------+------
 customer 2 |  470
 customer 3 |  688
 customer 1 | 1079
```
> AVG - считает среднее значение всех записей в сгруппированном поле 
```sql
SELECT customer.name, ROUND(AVG(product.price)) FROM customer
JOIN cart ON customer.id = cart.customer_id
JOIN product ON product.id = cart.product_id
GROUP BY (customer.id) ;
    name    | round 
------------+-------
 customer 2 |   470
 customer 3 |   344
 customer 1 |   360
(3 rows)
```
> ARRAY_AGG - собирает значения всех записей в сгруппированном поле в массив (список)
```sql
SELECT blogger.name, array_agg(post.body) FROM blogger JOIN post ON blogger.id = post.blogger_id GROUP BY (blogger.id) ;
   name    |                         array_agg                         
-----------+-----------------------------------------------------------
 blogger 1 | {"my first blog","today is a good day","it is my b-day!"}
 blogger 2 | {"my first post","some post"}
 blogger 3 | {"i am not a blogger"}
(3 rows)
```
> MIN/MAX - выбирает минимальное/максимальное значение из всех записей в сгруппированном поле
```sql
SELECT blogger.name, MAX(post.created_at), MIN(post.created_at) FROM blogger JOIN post ON blogger.id = post.blogger_id GROUP BY (blogger.id) ;
   name    |    max     |    min     
-----------+------------+------------
 blogger 2 | 2022-06-23 | 2013-05-10
 blogger 3 | 2022-08-15 | 2022-08-15
 blogger 1 | 2021-09-30 | 2020-08-01
(3 rows)
```
> COUNT - считает количество в сгруппированном поле 
```sql
SELECT blogger.name, COUNT(post.created_at) FROM blogger JOIN post ON blogger.id = post.blogger_id GROUP BY (blogger.id) ;
   name    | count 
-----------+-------
 blogger 2 |     2
 blogger 3 |     1
 blogger 1 |     3
(3 rows)
```