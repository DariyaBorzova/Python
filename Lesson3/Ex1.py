my_list1 = ["Зима", "Весна", "Лето", "Осень"]
my_dict = {1: "Зима", 2: "Весна", 3: "Лето", 4: "Осень"}
mounth = int(input("Введите номер месяца: "))
if mounth == 1 or mounth == 2 or mounth == 12:
    print(f"Результат через список - {my_list1[0]}")
    print(f"Результат через словарь - {my_dict.get(1)}")
elif mounth == 3 or mounth == 4 or mounth == 5:
    print(f"Результат через список - {my_list1[1]}")
    print(f"Результат через словарь - {my_dict.get(2)}")
elif mounth == 6 or mounth == 7 or mounth == 8:
    print(f"Результат через список - {my_list1[2]}")
    print(f"Результат через словарь - {my_dict.get(3)}")
elif mounth == 9 or mounth == 10 or mounth == 11:
    print(f"Результат через список - {my_list1[3]}")
    print(f"Результат через словарь - {my_dict.get(4)}")
else:
    print("Такого месяца нет")
