# Первый класс
# Создайте класс book с атрибутами:
# - материал страниц
# - наличие текста
# - название книги
# - автор
# - кол-во страниц
# - ISBN
# - флаг зарезервирована ли книга или нет (True/False).
# Какие-то из атрибутов будут общими для всех книг (материал, наличие текста), какие-то индивидуальными.
# Создайте несколько (штук 5) экземпляров разных книг.
# После создания пометьте одну книгу как зарезервированную.
# Распечатайте детали о каждой книге в таком виде:
# Если книга зарезервирована:
# Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага, зарезервирована
# если не зарезервирована:
# Название: Идиот, Автор: Достоевский, страниц: 500,  материал: бумага
# Второй класс
# Создайте дочерний класс для первого. Это будет класс для школьных учебников. В нем будут дополнительные атрибуты:
# - предмет (типа математика, история, география),
# - класс (школьный класс, для которого этот учебник)
#  (осторожно с названием переменной. class - зарезервированное слово),
# - наличие заданий (bool)
# - Создайте несколько экземпляров учебников.
# - После создания пометьте один учебник как зарезервированный.
# - Распечатайте детали о каждом учебнике в таком виде: Если учебник зарезервирован:
# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9, зарезервирована
# если не зарезервирован:
# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9

import random
liabary = []


class Book:
    def __init__(self, book_title, author, number_of_pages, isbn,
                 reserved, page_material='бумага', presence_of_text=True):
        self.page_material = page_material
        self.presence_of_text = presence_of_text
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.reserved = reserved

    def show_info(self):
        base_info = (
            f'''Материал страниц: {self.page_material},
                Наличие текста: {self.presence_of_text},
                Название книги: {self.book_title},
                Автор: {self.author},
                Количество страниц: {self.number_of_pages},
                ISBN: {self.isbn}'''
        )
        if self.reserved:
            print(base_info + ' Книга зарезервирована!')
        else:
            print(base_info + ' Книга доступна!')


class LernBook(Book):
    def __init__(self, book_title, author, number_of_pages, isbn, reserved, discipline,
                 auditory, zdanie, page_material='бумага', presence_of_text=True):
        super().__init__(
            page_material, presence_of_text, book_title, author, number_of_pages, isbn, reserved
        )
        self.discipline = discipline
        self.auditory = auditory
        self.zdanie = zdanie

    def show_info(self):
        base_info = (
            f'''Материал страниц: {self.page_material},
            Наличие текста: {self.presence_of_text},
            Название книги: {self.book_title},
            Автор: {self.author},
            Количество страниц: {self.number_of_pages},
            Предмет: {self.discipline},
            Класс: {self.auditory},
            Наличие заданий: {self.zdanie}
            '''
        )
        if self.reserved:
            print(base_info + ', зарезервирована')
        else:
            print(base_info + ', доступна')


def add_book():
    book_title = input('Название книги? ')
    page_material = input('Какой материал страниц? ')
    presence_of_text = input('Наличие текста? ')
    author = input('Автор? ')
    number_of_pages = input('Количество страниц? ')
    isbn = int(input('Введите номер isbn: '))
    reserved = (input('Зарезервирована ли книга (да/нет)? ')).lower()
    if reserved == 'да':
        reserved = True
    else:
        reserved = False
    new_book = Book(
        page_material, presence_of_text, book_title, author, number_of_pages, isbn, reserved
    )
    liabary.append(new_book)


def show_books():
    print('-----Все книги----')
    for _ in liabary:
        _.show_info()


def reservation_book():
    show_books()
    answer_reservation_book = input('Какую книгу вы хотите зарезервировать? (или "назад" для возврата)').lower()
    if answer_reservation_book == 'назад':
        return
    for _ in liabary:
        if _.book_title == answer_reservation_book:
            _.reserved = True
            break
    else:
        print('Такой книги нет в списке')


def dereservation_book():
    show_books()
    answer_reservation_book = input('Какую книгу вы хотите зарезервировать? (или "назад" для возврата)').lower()
    if answer_reservation_book == 'назад':
        return
    for _ in liabary:
        if _.book_title == answer_reservation_book:
            _.reserved = False
            break
    else:
        print('Такой книги нет в списке')


def gen_random_book(i):
    book_title = (f'Name is {i + 1}')
    page_material = (random.choice(['Кожзам', 'Пластик', 'Кожа']))
    presence_of_text = (random.choice(['Нет', 'Да']))
    author = (random.choice(['А.С Летчик-Пушки', 'М.Ю Лермонтов', 'С.У Ка(China inc)', 'Mr.Beast']))
    number_of_pages = (random.randint(0, 10000))
    isbn = (int(str(random.randint(323232, 3287329362)) + '777'))
    reserved = (random.choice(['Нет', 'Да'])).lower()
    if reserved == 'да':
        reserved = True
    else:
        reserved = False
    return {
        'page_material': page_material,
        'presence_of_text': presence_of_text,
        'book_title': book_title,
        'author': author,
        'number_of_pages': number_of_pages,
        'isbn': isbn,
        'reserved': reserved
    }


def testing_def():
    for i in range(6):
        data = gen_random_book(i)
        new_book = Book(**data)
        liabary.append(new_book)


def testing_lern_def():
    for i in range(6):
        data = gen_random_book(i)
        discipline = (random.choice(['Математика', 'Болталогия', 'Физика']))
        auditory = (random.choice(['777', '67', '666']))
        zdanie = (random.choice(['Нет', 'Да'])).lower()
        data['discipline'] = discipline
        data['auditory'] = auditory
        data['zdanie'] = zdanie
        new_book = LernBook(**data)
        liabary.append(new_book)


def programma():
    while True:
        answer = int(input(
            '''
            Что вы хотите сделать (номер подходящего ответа)?
            0. Я тестировщик, мне нужно 5 рыбных книг
            1. Добавить книгу
            2. Посмотреть список доступных книг
            3. Зарезервировать книгу
            4. Отменить резервацию книги
            5. Выйти из систему
            ___________________________________________________
            00. Я тестировщик, мне нужно 5 учебных рыбных книг
            22. Посмотреть список доступных учебных книг
            33. Зарезервировать учебную книгу
            44. Отменить резервацию учебную книги
            ___________________________________________________
            Ваш ответ:
            '''
        ))
        if answer == 0:
            testing_def()
        elif answer == 1:
            add_book()
        elif answer == 2:
            show_books()
        elif answer == 3:
            reservation_book()
        elif answer == 4:
            dereservation_book()
        if answer == 00:
            testing_lern_def()
        elif answer == 22:
            show_books()
        elif answer == 33:
            reservation_book()
        elif answer == 44:
            dereservation_book()
        elif answer == 5:
            exit()
        else:
            print('Такого варианта нет, введите номер ответа.')


print('Запуск программы....')
programma()
