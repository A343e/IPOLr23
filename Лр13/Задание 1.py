class Drob(object):
    """ Дробь вида a/b"""
    def __init__(self, a=0, b=1):
        self.a = a
        self.b = b
        self.normalize()

    def normalize(self):
        """ Приводит дробь вида 4/6 к 2/3"""
        gcd = self.gcd(self.a, self.b)
        self.a //= gcd
        self.b //= gcd

    def gcd(self, x, y):
        """Нахождение наибольшего общего делителя"""
        while y != 0:
            x, y = y, x % y
        return x

    def __eq__(self, other):
        """Проверка на равенство"""
        return self.a * other.b == other.a * self.b

    def __lt__(self, other):
        """Проверка на меньше"""
        return self.a * other.b < other.a * self.b

    def __add__(self, other):
        """Сложение"""
        new_a = self.a * other.b + other.a * self.b
        new_b = self.b * other.b
        return Drob(new_a, new_b)

    def __sub__(self, other):
        """Вычитание"""
        new_a = self.a * other.b - other.a * self.b
        new_b = self.b * other.b
        return Drob(new_a, new_b)

    def __mul__(self, other):
        """Умножение"""
        new_a = self.a * other.a
        new_b = self.b * other.b
        return Drob(new_a, new_b)

    def __truediv__(self, other):
        """Деление"""
        new_a = self.a * other.b
        new_b = self.b * other.a
        return Drob(new_a, new_b)

    def __str__(self):
        return '{}/{}'.format(self.a, self.b)

# Проверка
if __name__ == "__main__":
    x = Drob(1, 2)
    y = Drob(3, 4)
    print("x =", x)
    print("y =", y)
    print("x == y:", x == y)
    print("x < y:", x < y)
    z = x + y
    print("x + y =", z)
    z = x - y
    print("x - y =", z)
    z = x * y
    print("x * y =", z)
    z = x / y
    print("x / y =", z)
