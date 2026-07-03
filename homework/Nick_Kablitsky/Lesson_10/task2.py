# Создайте универсальный декоратор, который будет управлять тем,
# сколько раз запускается декорируемая функция
# Код, использующий этот декоратор может выглядеть, например, так:

# ЭТО НЕ ПРОВЕРЯТЬ ПОКА, НО ПРИ ЖЕЛАНИИ ДАТЬ ФИДБЕК ;)
def repeat_me(func):
    def repeat_me_repeat(*args):
        func(*args)
        print('Декоратор отработал')
        return
    return repeat_me_repeat()

@repeat_me(count = 2)
def example(*args, **kwargs):
    print(*args, **kwargs)

example('print me', count = 2)
# В результате работы будет такое:
