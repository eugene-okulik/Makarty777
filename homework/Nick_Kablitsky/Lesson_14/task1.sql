# Создайте в базе данных полный набор информации о студенте, заполнив все таблички:
# Создайте студента (student)
# Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
# Создайте группу (group) и определите своего студента туда
# Создайте несколько учебных предметов (subjects)
# Создайте по два занятия для каждого предмета (lessons)
# Поставьте своему студенту оценки (marks) для всех созданных вами занятий
# Все действия нужно выполнить именно в том порядке, который указан здесь в задании.
#
# Получите информацию из базы данных:
# Все оценки студента
# Все книги, которые находятся у студента
# Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
# (всё одним запросом с использованием Join)
# Все запросы, которые сделаете, сохраняйте в файлик с расширением .txt или .sql, и сдавайте как обычно.

CREATE TABLE student(id INTEGER PRIMARY KEY, student_name TEXT)
INSERT INTO student(id, student_name) VALUES (1, Tony)
CREATE TABLE books(id INTEGER PRIMARY KEY, books_name TEXT, student_id INTEGER)
INSERT INTO books(id, books_name, student_id) VALUES (1, Demidova, 1)
INSERT INTO books(id, books_name, student_id) VALUES (2, Akrapovich, 1)
INSERT INTO books(id, books_name, student_id) VALUES (3, Vavilova, 1)
CREATE TABLE group(id INTEGER PRIMARY KEY, group_name TEXT, student_id INTEGER)
INSERT INTO group(id, group_name, student_id) VALUES (1, 11v, 1)
CREATE TABLE subjects (id INTEGER PRIMARY KEY, subjects_name TEXT, student_id INTEGER)
INSERT INTO subjects(id, subjects_name, student_id) VALUES (1, Match, 1)
INSERT INTO subjects(id, subjects_name, student_id) VALUES (2, Phusik, 1)
INSERT INTO subjects(id, subjects_name, student_id) VALUES (3, Art, 1)
CREATE TABLE lessons (id INTEGER PRIMARY KEY, lessons_name TEXT, student_id INTEGER)
INSERT INTO lessons(id, lessons_name, student_id) VALUES (1, Lesson_1, 1)
INSERT INTO lessons(id, lessons_name, student_id) VALUES (2, Lesson_1, 1)
CREATE TABLE marks (id INTEGER PRIMARY KEY, lessons_name TEXT, student_id INTEGER, grade INTEGER)
INSERT INTO marks(id, lessons_name, student_id, grade) VALUES (1, Lesson_1, 1, 5)
INSERT INTO marks(id, lessons_name, student_id, grade) VALUES (1, Lesson_2, 1, 4)

SELECT