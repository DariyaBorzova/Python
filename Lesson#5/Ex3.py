"""Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""
el = 1
all_sum = 1
def my_sum(n, el, all_sum):
    if n > 0:
        el = el * (-0.5)
        all_sum += el
        n -= 1
        my_sum(n, el, all_sum)
    else:
        return el
n=int(input("Введите количество элементов: "))

print(my_sum(n, el, all_sum))