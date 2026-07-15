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
INSERT INTO students (name, second_name) VALUES ('Tony', 'Stark');

-- Получаем ID созданного студента (предположим, это 23014)
-- В реальности нужно выполнить SELECT LAST_INSERT_ID() или знать точный ID

-- Книги и указываем, что студент их взял
INSERT INTO books (title, taken_by_student_id) VALUES ('Demidova', 23014);
INSERT INTO books (title, taken_by_student_id) VALUES ('Akrapovich', 23014);
INSERT INTO books (title, taken_by_student_id) VALUES ('Vavilova', 23014);

-- Группа и студент
-- Сначала создаём группу
INSERT INTO `groups` (title, start_date, end_date) VALUES ('11v', '2024-01-01', '2024-12-31');
-- Получаем ID группы (предположим, это 22830)
-- Затем привязываем студента к группе
UPDATE students SET group_id = 22830 WHERE id = 23014;

-- Предметы
INSERT INTO subjects (title) VALUES ('Match');
INSERT INTO subjects (title) VALUES ('Phusik');
INSERT INTO subjects (title) VALUES ('Art');
-- Получаем ID предметов: Match=23031, Phusik=23032, Art=23033

-- Занятия для каждого предмета
-- Математика (id=23031)
INSERT INTO lessons (title, subject_id) VALUES ('Lesson_1_Match', 23031);
INSERT INTO lessons (title, subject_id) VALUES ('Lesson_2_Match', 23031);
-- Физика (id=23032)
INSERT INTO lessons (title, subject_id) VALUES ('Lesson_1_Phusik', 23032);
INSERT INTO lessons (title, subject_id) VALUES ('Lesson_2_Phusik', 23032);
-- Рисование (id=23033)
INSERT INTO lessons (title, subject_id) VALUES ('Lesson_1_Art', 23033);
INSERT INTO lessons (title, subject_id) VALUES ('Lesson_2_Art', 23033);
-- Получаем ID занятий: 76374, 76375, 76376, 76377, 76378, 76379

-- Оценки студенту за все занятия
INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 76374, 23014);
INSERT INTO marks (value, lesson_id, student_id) VALUES (4, 76375, 23014);
INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 76376, 23014);
INSERT INTO marks (value, lesson_id, student_id) VALUES (3, 76377, 23014);
INSERT INTO marks (value, lesson_id, student_id) VALUES (4, 76378, 23014);
INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 76379, 23014);

-- ПОЛУЧЕНИЕ ИНФОРМАЦИИ
SELECT
    s.name AS student_name,
    s.second_name AS student_second_name,
    g.title AS group_name,
    b.title AS book_name,
    sub.title AS subject_name,
    l.title AS lesson_name,
    m.value AS grade
FROM students s
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON s.id = b.taken_by_student_id
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjects sub ON l.subject_id = sub.id
WHERE s.id = 23014;
