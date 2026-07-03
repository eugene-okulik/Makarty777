# Напишите программу: Есть функция которая делает одну из арифметических операций с переданными
# ей числами (числа и операция передаются в аргументы функции). Функция выглядит примерно так:

def calc(first, second):
    def decorator(func):
        def wrapper(operation):
            if operation == '+':
                result = first + second
            elif operation == '-':
                result = first - second
            elif operation == '*':
                result = first * second
            elif operation == '/' or operation == ':':
                result = first / second
            elif operation == '**' or operation == '^':
                result = first ** second
            func(operation, result)
        return wrapper
    return decorator


# Программа спрашивает у пользователя 2 числа (вне функции)
first, second = int(input('Введите первое число: ')), int(input('Введите второе число: '))


# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
@calc(first, second)
def calculator(operation, result):
    print(f'{first} {operation} {second} = {result}')


# если одно из чисел отрицательное - умножени
if (0 > first) or (0 > second):
    calculator('*')
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
elif first == second:
    calculator('+')
# если первое больше второго, то происходит вычитание второго из певрого
elif first > second:
    calculator('-')
# если второе больше первого - деление первого на второе
else:
    calculator(':')
