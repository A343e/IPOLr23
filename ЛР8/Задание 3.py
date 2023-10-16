i = input("Введите последовательность символов: ")
s_set = set()
a = ['+', '-', '*', '/']
p = ['.', ',', ';', ':', '!', '?']

for s in i:
    if s in a or s in p:
        s_set.add(s)

print(s_set)