# Создайте универсальный декоратор, который будет управлять тем,
# сколько раз запускается декорируемая функция
# Код, использующий этот декоратор может выглядеть, например, так:

# ЭТО НЕ ПРОВЕРЯТЬ ПОКА, НО ПРИ ЖЕЛАНИИ ДАТЬ ФИДБЕК ;)
def repeat_me(count):
    def decorator_1(func):
        def decorator_2(*args):
            for _ in range(count):
                func(*args)
        return decorator_2
    return decorator_1


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')
