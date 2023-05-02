"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
text = ['разработка', 'администрирование', 'protocol', 'standart']
text1 = []
for i in text:
    text1.append(i.encode('utf-8'))
print(text1)

text2 = []
for i in text1:
   text2.append(i.decode('utf-8'))
print(text2)

