import math

def f(a, b):
    # Функция для вычисления длины гипотенузы
    return math.sqrt(a ** 2 + b ** 2)


def c(triangle1, triangle2):
    # Функция для сравнения длин гипотенуз двух треугольников
    hypotenuse1 = f(triangle1[0], triangle1[1])
    hypotenuse2 = f(triangle2[0], triangle2[1])

    if hypotenuse1 > hypotenuse2:
        return "Первый треугольник имеет большую гипотенузу."
    elif hypotenuse1 < hypotenuse2:
        return "Второй треугольник имеет большую гипотенузу."
    else:
        return "Оба треугольника имеют одинаковую длину гипотенузы."


# Задайте катеты для двух треугольников
triangle1 = (6, 9)  # Катеты первого треугольника
triangle2 = (9, 3)  # Катеты второго треугольника

result = c(triangle1, triangle2)
print(result)