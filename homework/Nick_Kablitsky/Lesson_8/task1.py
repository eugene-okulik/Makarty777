# Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool.
# Спросите у пользователя salary. А bonus пусть назначается рандомом.
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.
# Примеры результатов:
# 10000, True - '$10255'
# waaaaa25000, False - '$25000'
# 600, True - '$3785'

import random
while True:
    salary, bonus = input('Введите целое число: '), bool(random.randint(0, 1))
    if salary.isdigit():
        if bonus:
            print(f"{salary}, {bonus} - '${salary + random.randint(1, 10000)}'")
        else:
            print(f"{salary}, {bonus} - '${salary}'")
        break
    else:
        print('Число неверно! Но не переживай сейчас мы соберем его ;)')
        sclad_id_digit = []
        for kasdaya in salary:
            if kasdaya.isdigit():
                sclad_id_digit.append(kasdaya)
        salary = int(''.join(sclad_id_digit))
        if bonus:
            print(f"{salary}, {bonus} - '${salary + random.randint(1, 10000)}' ")
        else:
            print(f"{salary}, {bonus} - '${salary}' ")
        break
