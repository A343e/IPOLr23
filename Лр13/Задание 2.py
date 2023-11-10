# Класс для работы с рублями и копейками.
class Rub(object):

    # Инициализация объекта с указанием рублей и копеек.
    def __init__(self, rub=0, kop=0):
        self.rub = rub
        self.kop = kop
        self.normalize()

    # Приведение рублей и копеек к нормальному виду (копейки < 100).
    def normalize(self):
        self.rub += self.kop // 100
        self.kop %= 100

    # Преобразование объекта в строку для вывода.
    def __str__(self):
        return f'{self.rub:03d}.{self.kop:02d} rub'

    # Сравнение двух объектов по стоимости.
    def __lt__(self, other):
        if self.rub == other.rub:
            return self.kop < other.kop
        return self.rub < other.rub

    # Сложение двух объектов.
    def __add__(self, other):
        res = Rub(self.rub + other.rub, self.kop + other.kop)
        res.normalize()
        return res

    # Вычитание двух объектов.
    def __sub__(self, other):
        rub = self.rub - other.rub
        kop = self.kop - other.kop
        if kop < 0:
            rub -= 1
            kop += 100
        return Rub(rub, kop)


# Класс описания товара: название и цена.
class Goods(object):

    # Инициализация объекта товара с указанием названия, рублей и копеек.
    def __init__(self, name='', rub=0, kop=0):
        self.name = name
        self.price = Rub(rub, kop)


# Список товаров
goods_list = [
    Goods('Молоко', 3, 67),
    Goods('Хлеб', 3, 48),
    Goods('Рис', 4, 59),
    Goods('Гречка', 4, 45),
    Goods('Колбаса', 18, 99),
    # Добавьте больше товаров по мере необходимости
]

total_price = Rub()

# Считаем общую стоимость товаров
for goods in goods_list:
    total_price += goods.price

# Сортируем список товаров по цене
goods_list.sort(key=lambda goods: goods.price, reverse=True)

# Выводим отсортированный список товаров
for goods in goods_list:
    print(f'{goods.name} {goods.price}')

# Выводим общую стоимость
print(f'Всего {total_price}')

# Спрашиваем у пользователя, сколько денег он дал
t = input('Ваше количество денег: ')
tender_rub, tender_kop = map(int, t.split('.'))

# Создаем объект для предоставленной суммы
tender_amount = Rub(tender_rub, tender_kop)
print(f'Ваше количество денег {tender_amount}')

# Вычисляем и выводим сдачу
change = tender_amount - total_price
print(f'Сдача {change}')
