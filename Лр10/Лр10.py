# Запрашиваем у пользователя N и M
N = int(input("Введите N: "))
M = int(input("Введите M: "))

# Открыть файл для записи чисел
with open(f'file1_{N}.txt', 'w') as file1:
    for i in range(N):
        number = int(input(f"Введите целое число {i + 1}: "))
        file1.write(str(number) + '\n')

# Открыть файл для чтения и фильтрации чисел
with open(f'file1_{N}.txt', 'r') as file1, open(f'file2_{N}.txt', 'w') as file2:
    for line in file1:
        number = int(line)
        if number <= M:
            file2.write(str(number) + '\n')

print(f"Числа, не превышающие {M}, были записаны в файл file2_{N}.txt.")