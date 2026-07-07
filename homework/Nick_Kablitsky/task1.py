# Создать классы цветов:
# общий класс для всех цветов  +
# классы для нескольких видов  +
# Создать экземпляры (объекты) цветов разных видов. +
# Собрать букет (букет - еще один класс) с определением его стоимости. +
# В букете цветы пусть хранятся в списке. Это будет список объектов.+
# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров
# (свежесть/цвет/длина стебля/стоимость)(это тоже методы)
# Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни) (и это тоже метод).


class Bouquet():
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_price_Bouquet(self):
        return sum(flower.price for flower in self.flowers)

    def wilting_time(self):
        return sum(flower.chastota_yxashivania for flower in self.flowers) / len(self.flowers)

    def find_arg_lifetime(self, min_days):
        return [flower for flower in self.flowers if flower.chastota_yxashivania >= min_days]

    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price)

    def search_flower_parameters(
        self, find_arg_lifetime=None, fresh=None, color=None, leng_cabels=None, price=None
        ):
        resault = []
        for flower in self.flowers:
            if find_arg_lifetime is not None and flower.chastota_yxashivania < find_arg_lifetime:
                continue
            if fresh is not None and flower.fresh != fresh:
                continue
            if color is not None and flower.color != color:
                continue
            if price is not None and flower.price < price:
                continue
            resault.append(flower)
        return resault


class Flowers():
    def __init__(self, zapah, lepestki, chastota_yxashivania, price, fresh, color, leng_cabels):
        self.zapah = zapah
        self.lepestki = lepestki
        self.chastota_yxashivania = chastota_yxashivania
        self.price = price
        self.fresh = fresh
        self.color = color
        self.leng_cabels = leng_cabels


    def __str__(self):
        return f'Цвет {self.color}, время жизни: {self.chastota_yxashivania} дней, цена: {self.price}'

    def __repr__(self):
        return self.__str__()


class HomeFlowers(Flowers):
    def __init__(self, zapah, lepestki, chastota_yxashivania, price, fresh, color, leng_cabels, zdanie):
        super().__init__(zapah, lepestki, chastota_yxashivania, price, fresh, color, leng_cabels)
        self.zdanie = zdanie


class PresentFlowers(Flowers):
    def __init__(self, zapah, lepestki, chastota_yxashivania, price, fresh, color, leng_cabels, podarok):
        super().__init__(zapah, lepestki, chastota_yxashivania, price, fresh, color, leng_cabels)
        self.podarok = podarok


flower1 = HomeFlowers(
    zapah=False, lepestki=True, chastota_yxashivania=7, price=500,
    zdanie=True, fresh=True, color='Red', leng_cabels=0.2
)
flower2 = HomeFlowers(
    zapah=True, lepestki=False, chastota_yxashivania=365, price=0, zdanie=True,
    fresh=True, color='Blue', leng_cabels=0.5
)
flower3 = PresentFlowers(
    zapah=True, lepestki=True, chastota_yxashivania=2, price=730, podarok=True,
    fresh=True, color='White', leng_cabels=0.3
)
flower4 = PresentFlowers(
    zapah=True, lepestki=True, chastota_yxashivania=1, price=8000, podarok=True,
    fresh=False, color='Red', leng_cabels=0.5
)

my_bouquet = Bouquet()
my_bouquet.add_flower(flower1)
my_bouquet.add_flower(flower2)
my_bouquet.add_flower(flower3)
my_bouquet.add_flower(flower4)

print(f'В букете {len(my_bouquet.flowers)} цветов')
print(f'Перкуп цветов говорит, что курс не стабильные, букет стоит: {my_bouquet.total_price_Bouquet()}')
print(f'Сортировка по увяданию: {my_bouquet.wilting_time()}')
print(f'Среднее время жизни цветов в букете: {my_bouquet.find_arg_lifetime(3)}')
