# map | filter
# Есть такой список:
temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
    22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]

# Будем считать жарким всё, что выше 28.
weather_hot = list(filter(lambda x: x > 28, temperatures))

print(f'Горячие хиты краснодара 2007: {weather_hot}')

# Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.
var_max, var_min = max(weather_hot), min(weather_hot)
print(f'Самая высокая температура: {var_max}; Самая низкая температура: {var_min}')
print(f'А средняя температура составляет: {(sum(weather_hot)) / len(weather_hot)}')
