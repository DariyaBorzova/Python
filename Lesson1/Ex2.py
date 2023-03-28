sec = input("Введите время в секундах: ")
hours = sec // 3600
ost = sec % 3600
minutes = ost // 60
sec %= 60
print("Время в формате ч:м:с - ", hours, ":", minutes, ":", sec, ".")