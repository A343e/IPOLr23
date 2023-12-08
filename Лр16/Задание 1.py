class Car:
    def __init__(self, make, model, year, price):
        self._make = make
        self._model = model
        self._year = year
        self._price = price

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

    @property
    def price(self):
        return self._price

    @make.setter
    def make(self, new_make):
        self._make = new_make

    @model.setter
    def model(self, new_model):
        self._model = new_model

    @year.setter
    def year(self, new_year):
        self._year = new_year

    @price.setter
    def price(self, new_price):
        self._price = new_price

# Создаем объект класса Car
my_car = Car(make="Toyota", model="Camry", year=2022, price=25000)

# Выводим информацию о машине
print(f"Make: {my_car.make}")
print(f"Model: {my_car.model}")
print(f"Year: {my_car.year}")
print(f"Price: ${my_car.price}")

# Изменяем значения свойств с использованием сеттеров
my_car.make = "Honda"
my_car.model = "Accord"
my_car.year = 2023
my_car.price = 27000

# Выводим обновленную информацию о машине
print("\nUpdated Information:")
print(f"Make: {my_car.make}")
print(f"Model: {my_car.model}")
print(f"Year: {my_car.year}")
print(f"Price: ${my_car.price}")