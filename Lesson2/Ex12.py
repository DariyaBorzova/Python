x = int(input("Введите значение 1: "))
y = int(input("Введите значение 2: "))
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)
