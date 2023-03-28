sec = input("Введите время в секундах: ")
hours = sec // 3600
ost = sec % 3600
minutes = ost // 60
sec %= 60
print("Время в формате ч:м:с - ", hours, ":", minutes, ":", sec, ".")

n = int(input("Введите число n: "))
nn = str(n)+str (n)
nnn = str(n)+str (n)+str (n)
sum = n+int(nn)+int(nnn)
print("Результат: ", sum)


