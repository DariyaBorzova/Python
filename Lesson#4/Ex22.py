mol = [int(x) for x in input(
    "Введите через пробел количество элементов 1ого множества и 2ого мноества: ").split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
print ("Введите через пробел элементы 1ого множества")
a = [int(x) for x in input().split()]
k = set(a)
for i in k:
    set_1.add(i)
print("Введите элементы 2ого множества")
b = [int(x) for x in input().split()]
k1 = set(b)
for i in k1:
    set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
print(kool)
