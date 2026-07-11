# Нужно прочитать файлик, который лежит в репозитории в моей папке. Здесь: homework/eugene_okulik/hw_13/data.txt
# Файлик не копируйте и никуда не переносите. Напишите программу,
# которая читает этот файл, находит в нём даты и делает с этими датами то, что после них написано.
# Опирайтесь на то, что структура каждой строки одинакова: сначала идет номер, потом дата,
# потом дефис и после него текст. У вас должен получиться код, который находит даты и для даты под
# номером один в коде должно быть реализовано то действие, которое написано в файле после этой даты.
# Ну и так далее для каждой даты.
# pattern = (number, data, defis, text)
# re.search(r'\d+', var_data)
# import re

import os
from datetime import datetime, timedelta

print('Текущая директория:', os.getcwd())
print('Файл существует?', os.path.exists('homework/eugene_okulik/hw_13/data.txt'))
print('____________________________')

with open('homework/eugene_okulik/hw_13/data.txt', 'r', encoding='UTF-8') as file:
    var_data = file.readlines()

for line in var_data:
    line = line.strip()
    if not line:
        continue

    parts = line.split(' - ')
    number_date = parts[0].split('. ')
    number = int(number_date[0])
    data_str = number_date[1]
    action = parts[1]

    date_obj = datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S.%f")

    print(f'{number} - порядковый номер строки')
    print(f'Тупо цифры с которыми предстоит работать: {number_date[1]}')
    print(f'Исходник даты целиком: {parts[0]}')
    print(f'Что нужно сделать: {action}')
    if number == 1:
        print(f'На неделю позже: {date_obj + timedelta(weeks = 1)}')
    elif number == 2:
        print(f'День недель {date_obj.strftime("%A")}')
    elif number == 3:
        print(f'Сколько дней назад была эта дата: {(datetime.now() - date_obj).days}')
    else:
        print('Ошибка переменной number, что мешало тут TRY-ить я хз, но это достойный ответ под else')
    print('____________________________')
