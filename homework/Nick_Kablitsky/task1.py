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
        return sum(flower.frequency_courtship for flower in self.flowers) / len(self.flowers)

    def find_arg_lifetime(self, min_days):
        return [flower for flower in self.flowers if flower.frequency_courtship >= min_days]

    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price)

    def sort_by_fresh(self):
        self.flowers.sort(key=lambda flower: flower.fresh, reverse=True)

    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda flower: flower.leng_cabels, reverse=True)

    def search_flower_parameters(self, find_arg_lifetime=None, fresh=None, color=None, leng_cabels=None, price=None):
        resault = []
        for flower in self.flowers:
            if find_arg_lifetime is not None and flower.frequency_courtship < find_arg_lifetime:
                continue
            if fresh is not None and flower.fresh != fresh:
                continue
            if color is not None and flower.color != color:
                continue
            if price is not None and flower.price < price:
                continue
            resault.append(flower)
        return resault


class Flower():
    def __init__(self, smell, petals, frequency_courtship, price, fresh, color, leng_cabels):
        self.smell = smell
        self.petals = petals
        self.frequency_courtship = frequency_courtship
        self.price = price
        self.fresh = fresh
        self.color = color
        self.leng_cabels = leng_cabels

    def __str__(self):
        return f'Цвет {self.color}, время жизни: {self.frequency_courtship} дней, цена: {self.price}'

    def __repr__(self):
        return self.__str__()


class HomeFlowers(Flower):
    def __init__(self, smell, petals, frequency_courtship, price, fresh, color, leng_cabels, building):
        super().__init__(smell, petals, frequency_courtship, price, fresh, color, leng_cabels)
        self.building = building


class PresentFlowers(Flower):
    def __init__(self, smell, petals, frequency_courtship, price, fresh, color, leng_cabels, present):
        super().__init__(smell, petals, frequency_courtship, price, fresh, color, leng_cabels)
        self.present = present


flower1 = HomeFlowers(
    smell=False, petals=True, frequency_courtship=7, price=500,
    building=True, fresh=True, color='Red', leng_cabels=0.2
)
flower2 = HomeFlowers(
    smell=True, petals=False, frequency_courtship=365, price=0, building=True,
    fresh=True, color='Blue', leng_cabels=0.5
)
flower3 = PresentFlowers(
    smell=True, petals=True, frequency_courtship=2, price=730, present=True,
    fresh=True, color='White', leng_cabels=0.3
)
flower4 = PresentFlowers(
    smell=True, petals=True, frequency_courtship=1, price=8000, present=True,
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

print('_________________________________________________________________________')
my_bouquet.sort_by_price()
for flower in my_bouquet.flowers:
    print(f'Сортировка по цене:  {flower}')

print('_________________________________________________________________________')
my_bouquet.sort_by_fresh()
for flower in my_bouquet.flowers:
    print(f'Сортировка по свежест:  {flower}')

print('_________________________________________________________________________')
my_bouquet.sort_by_color()
for flower in my_bouquet.flowers:
    print(f'Сортировка по цвету:  {flower}')

print('_________________________________________________________________________')
my_bouquet.sort_by_stem_length()
for flower in my_bouquet.flowers:
    print(f'Сортировка по длине стебля:  {flower}')
