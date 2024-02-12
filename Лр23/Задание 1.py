import numpy as np

# Создаем случайное количество строк и столбцов от 15 до 100
num_rows = np.random.randint(15, 101)
num_columns = np.random.randint(15, 101)

# Заполняем массив целыми числами от 1 до 1000
matrix = np.random.randint(1, 1001, size=(num_rows, num_columns))

# Выводим массив на экран полностью
print("Прямоугольный массив:")
print(matrix)

# Находим минимальный элемент в столбце
min_element = np.min(matrix, axis=0)
column_index = np.argmin(min_element)  # Индекс столбца с минимальным элементом

# Выводим минимальный элемент на экран
print(f"Минимальный элемент в {column_index + 1}-м столбце: {min_element[column_index]}")

# Находим сумму всех элементов матрицы и найденного минимального элемента
total_sum = np.sum(matrix) + min_element[column_index]
print(f"Сумма элементов матрицы и найденного элемента: {total_sum}")