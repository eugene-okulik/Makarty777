# map | filter

# Есть такой список:
temperatures = [
20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,\
22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]

# С помощью функции map или filter создайте из этого списка новый список с жаркими днями.
new_temperatures = filter(lambda: temperatures * 1.15, temperatures)
print(new_temperatures)

# Будем считать жарким всё, что выше 28.
INNA_Hot = list(filter(lambda x: x > 28, temperatures))
print(f'Горячие хиты краснодара 2007: {INNA_Hot}')

# Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.
var_max, var_min = max(temperatures), min(temperatures)
print(f'Самая высокая температура: {var_max}; Самая низкая температура: {var_min}')
print(f'А средняя температура составляет: {(sum(temperatures)) / len(temperatures)}')
