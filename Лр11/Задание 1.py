class ResidentialHouse:
    '''
    Класс, описывающий жилой дом в микрорайоне.

    Атрибуты:
    - address: адрес дома
    - num_of_floors: количество этажей
    - num_of_rooms: количество комнат
    - year_of_construction: год постройки
    - owner_name: имя владельца
    - is_parking_available: наличие парковки

    Методы:
    1. get_house_info(): выводит информацию о доме.
    2. is_old_house(): проверяет, является ли дом старым (более 20 лет).
    3. add_room(new_room): добавляет новую комнату к дому.
    4. change_owner(new_owner): изменяет владельца дома.'''

    def __init__(self, address, num_of_floors, num_of_rooms, year_of_construction, owner_name, is_parking_available):
        self.address = address
        self.num_of_floors = num_of_floors
        self.num_of_rooms = num_of_rooms
        self.year_of_construction = year_of_construction
        self.owner_name = owner_name
        self.is_parking_available = is_parking_available

    def get_house_info(self):
        """Выводим информацию о доме."""
        print(f"Дом по адресу {self.address}, {self.num_of_floors} этаж(а), {self.num_of_rooms} комнат(ы), "
              f"построен в {self.year_of_construction} году, владелец: {self.owner_name}.")

    def is_old_house(self):
        """Проверяет, является ли дом старым (более 20 лет)."""
        current_year = 2023
        return current_year - self.year_of_construction > 20

    def add_room(self, new_room):
        """Добавляет новую комнату к дому."""
        self.num_of_rooms += new_room
        print(f"К дому по адресу {self.address} добавлена новая комната. Теперь в нем {self.num_of_rooms} комнат(ы).")

    def change_owner(self, new_owner):
        """Изменяет владельца дома."""
        print(f"Владелец дома по адресу {self.address} сменился. Новый владелец: {new_owner}.")
        self.owner_name = new_owner


# Основная программа
# Вывод документации класса
print(ResidentialHouse.__doc__)

# Создание и инициализация экземпляров класса
house1 = ResidentialHouse("ул. Примерная, 1", 3, 5, 2005, "Иванов", True)
house2 = ResidentialHouse("ул. Тестовая, 7", 5, 8, 1990, "Петров", False)
house3 = ResidentialHouse("пр. Образцовый, 12", 2, 4, 2015, "Сидоров", True)
house4 = ResidentialHouse("ул. Показательная, 5", 4, 6, 1980, "Кузнецов", True)
house5 = ResidentialHouse("пр. Особенный, 8", 6, 10, 2008, "Федоров", False)

# Вывод информации о каждом доме
house1.get_house_info()
house2.get_house_info()
house3.get_house_info()
house4.get_house_info()
house5.get_house_info()

# Проверка, является ли дом старым
print(f"Дом по адресу {house1.address} {'старый' if house1.is_old_house() else 'новый'}.")
print(f"Дом по адресу {house4.address} {'старый' if house4.is_old_house() else 'новый'}.")

# Добавление комнаты к дому
house3.add_room(2)

# Смена владельца дома
house2.change_owner("Новосельцев")

# Вывод информации о доме после изменений
house3.get_house_info()
house2.get_house_info()