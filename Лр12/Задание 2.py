class House:
    def __init__(self):
        self._address = None
        self._num_of_rooms = None
        self._square = None
        self._year_built = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def num_of_rooms(self):
        return self._num_of_rooms

    @num_of_rooms.setter
    def num_of_rooms(self, value):
        self._num_of_rooms = value

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, value):
        self._square = value

    @property
    def year_built(self):
        return self._year_built

    @year_built.setter
    def year_built(self, value):
        self._year_built = value

    def __del__(self):
        print(f"В дом по адресу был вызван деструктор. {self.address}")

# Создаем список из 10 объектов класса House
houses = []
for i in range(10):
    house = House()
    house.address = input(f"Введите адрес для дома {i + 1}: ")
    house.num_of_rooms = int(input(f"Введите количество комнат для дома {i + 1}: "))
    house.square = float(input(f"Введите площадь для дома {i + 1}: "))
    house.year_built = int(input(f"Введите год постройки для дома {i + 1}: "))
    houses.append(house)

# Пример использования списка домов
for i, house in enumerate(houses):
    print(f"\nИнформация о доме {i + 1}:")
    print(f"Адрес: {house.address}")
    print(f"Количество комнат: {house.num_of_rooms}")
    print(f"Площадь: {house.square}")
    print(f"Год постройки: {house.year_built}")

# После завершения программы деструктор будет вызван для каждого объекта