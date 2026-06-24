# Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел
var1_int, var2_int = int(input("Введите перове число: ")), int(input("Введите второе число: "))
MidleArif, MidleGeom = ((var1_int + var2_int) / 2), ((var1_int * var2_int) ** 0.5)
print(
    'MidleArif:', MidleArif,
    'MidleGeom:', MidleGeom
)
