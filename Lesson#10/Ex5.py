"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import urllib.request, chardet

task5_1 = urllib.request.urlopen('http://yandex.ru').read()
x = chardet.detect(task5_1)
print(x)

task5_2 = urllib.request.urlopen('http://youtube.ru').read()
y = chardet.detect(task5_2)
print(y)