# Даны числа x и y. Получить x − y / 5 + xy
x_int, y_int = int(input("Введите число x : ")), int(input("Введите число y : "))
match_xy = (x_int - y_int)/(5 + (x_int * y_int))
