# Дана такая дата: "Jan 15, 2023 - 12:05:33"
# Преобразуйте эту дату в питоновский формат, после этого:

import datetime
import locale

# Принудительно инглиш взял с нейронки
locale.setlocale(locale.LC_TIME, 'English_United States.1252')

data = 'Jan 15, 2023 - 12:05:33'
# 1. Распечатайте полное название месяца из этой даты
print(datetime.datetime.strptime(data, '%b %d, %Y - %H:%M:%S').strftime('%B'))
# 2. Распечатайте дату в таком формате: "15.01.2023, 12:05"
print(datetime.datetime.strptime(data, '%b %d, %Y - %H:%M:%S').strftime('%d.%m.%Y, %H:%M'))
