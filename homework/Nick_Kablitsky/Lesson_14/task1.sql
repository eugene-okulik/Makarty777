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

-- Создаём студента
CREATE TABLE student(id INTEGER PRIMARY KEY, student_name TEXT);
INSERT INTO student(id, student_name) VALUES (1, 'Tony');

-- книги и указываем, что студент их взял
CREATE TABLE books(id INTEGER PRIMARY KEY, book_name TEXT, student_id INTEGER);
INSERT INTO books(id, book_name, student_id) VALUES (1, 'Demidova', 1);
INSERT INTO books(id, book_name, student_id) VALUES (2, 'Akrapovich', 1);
INSERT INTO books(id, book_name, student_id) VALUES (3, 'Vavilova', 1);

-- Группа и студент
-- ВАЖНО: 'group' зарезервированное слово, называем student_group
CREATE TABLE student_group(id INTEGER PRIMARY KEY, group_name TEXT, student_id INTEGER);
INSERT INTO student_group(id, group_name, student_id) VALUES (1, '11v', 1);

-- Предметы
CREATE TABLE subjects(id INTEGER PRIMARY KEY, subject_name TEXT);
INSERT INTO subjects(id, subject_name) VALUES (1, 'Match');
INSERT INTO subjects(id, subject_name) VALUES (2, 'Phusik');
INSERT INTO subjects(id, subject_name) VALUES (3, 'Art');

-- Занятия для каждого предмета
CREATE TABLE lessons(id INTEGER PRIMARY KEY, lesson_name TEXT, subject_id INTEGER);
-- Математика (id=1)
INSERT INTO lessons(id, lesson_name, subject_id) VALUES (1, 'Lesson_1_Match', 1);
INSERT INTO lessons(id, lesson_name, subject_id) VALUES (2, 'Lesson_2_Match', 1);
-- Физика (id=2)
INSERT INTO lessons(id, lesson_name, subject_id) VALUES (3, 'Lesson_1_Phusik', 2);
INSERT INTO lessons(id, lesson_name, subject_id) VALUES (4, 'Lesson_2_Phusik', 2);
-- Рисование (id=3)
INSERT INTO lessons(id, lesson_name, subject_id) VALUES (5, 'Lesson_1_Art', 3);
INSERT INTO lessons(id, lesson_name, subject_id) VALUES (6, 'Lesson_2_Art', 3);

-- Оценки студенту за все занятия
CREATE TABLE marks(id INTEGER PRIMARY KEY, student_id INTEGER, lesson_id INTEGER, grade INTEGER);
INSERT INTO marks(id, student_id, lesson_id, grade) VALUES (1, 1, 1, 5);
INSERT INTO marks(id, student_id, lesson_id, grade) VALUES (2, 1, 2, 4);
INSERT INTO marks(id, student_id, lesson_id, grade) VALUES (3, 1, 3, 5);
INSERT INTO marks(id, student_id, lesson_id, grade) VALUES (4, 1, 4, 3);
INSERT INTO marks(id, student_id, lesson_id, grade) VALUES (5, 1, 5, 4);
INSERT INTO marks(id, student_id, lesson_id, grade) VALUES (6, 1, 6, 5);

-- ПОЛУЧЕНИЕ ИНФОРМАЦИИ
SELECT 
    student.student_name, student_group.group_name, books.book_name, 
    subjects.subject_name, lessons.lesson_name, marks.grade
FROM student
LEFT JOIN student_group ON student.id = student_group.student_id
LEFT JOIN books ON student.id = books.student_id
LEFT JOIN marks ON student.id = marks.student_id
LEFT JOIN lessons ON marks.lesson_id = lessons.id
LEFT JOIN subjects ON lessons.subject_id = subjects.id
WHERE student.student_name = 'Tony';
