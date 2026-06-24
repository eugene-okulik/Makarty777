# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь
katet_1_int, katet_2_int = int(input("Введите первый катет: ")), int(input("Введите второй катет: "))
giptenza_katet_1_katet_2 = (((katet_1_int ** 2) + (katet_2_int ** 2)) ** 0.5)
square = ((katet_1_int * katet_2_int) * 0.5)
print(
    'giptenza:', giptenza_katet_1_katet_2,
    'square:', square
)
