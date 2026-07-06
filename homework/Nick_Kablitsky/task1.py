# Создать классы цветов: 
# общий класс для всех цветов  +
# классы для нескольких видов  +
# Создать экземпляры (объекты) цветов разных видов. Собрать букет (букет - еще один класс) 
# с определением его стоимости. В букете цветы пусть хранятся в списке. Это будет список объектов.
# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров 
# (свежесть/цвет/длина стебля/стоимость)(это тоже методы)
# Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни) (и это тоже метод).

import random


сlass Bouquet():

class Flowers():
    def __init__(self, zapah, lepestki, chastota_yxashivania, price):
        self.zapah = zapah 
        self.lepestki = lepestki
        self.chastota_yxashivania = chastota_yxashivania
        self.price = price


class HomeFlowers(Flowers):
    def __init__(self, zapah, lepestki, chastota_yxashivania, price, zdanie):
        self.zapah = zapah 
        self.lepestki = lepestki
        self.chastota_yxashivania = chastota_yxashivania
        self.price = price
        self.zdanie = zdanie

class PresentFlowers(Flowers):
    def __init__(self, zapah, lepestki, chastota_yxashivania, price, podarok):
        self.zapah = zapah 
        self.lepestki = lepestki
        self.chastota_yxashivania = chastota_yxashivania
        self.price = price
        self.podarok = podarok

Byket = []

flower1 = HomeFlowers(zapah=False, lepestki=True, chastota_yxashivania=7, price=500, zdanie=True)
flower2 = HomeFlowers(zapah=True, lepestki=False, chastota_yxashivania=365, price=0, zdanie=True)
flower3 = PresentFlowers(zapah=True, lepestki=True, chastota_yxashivania=2, price=730, podarok=True)
flower4 = PresentFlowers(zapah=True, lepestki=True, chastota_yxashivania=1, price=8000, podarok=True)

Byket.append(flower1)
Byket.append(flower2)
Byket.append(flower3)
Byket.append(flower4)

print(f"В букете {len(Byket)} цветов")
total_price = random.randint(120, 1000000)
wilting_time = ((flower1.chastota_yxashivania + flower2.chastota_yxashivania + 
                 flower3.chastota_yxashivania + flower4.chastota_yxashivania) / 4)
sort_by_price = sorted([flower1.price, flower2.price, flower3.price, flower4.price])
find_by_lifetime = (
    flower1.chastota_yxashivania, flower2.chastota_yxashivania, 
    flower3.chastota_yxashivania, flower4.chastota_yxashivania
    ) / 4
print(f'Перкуп цветов говорит, что курс не стабильные, букет стоит {total_price}')
