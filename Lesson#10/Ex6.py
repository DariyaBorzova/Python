"""6.	Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор». Проверить кодировку файла
 по умолчанию. Принудительно открыть файл в формате Unicode и вывести его
 содержимое."""

import chardet

file1 = open("Task6.txt", 'w+')
file1.write("сетевое программирование, сокет, декоратор")
file1.close()
f = open('Task6.txt')
print(chardet.detect(f.read().encode())['encoding'])
f.close()
file1 = open("Task6.txt", "r", -1, 'utf-8')
print(file1.read())
file1.close()

