my_list = [9, 11, 7, 6, 6, 1, 2]
print(my_list)
new_el = None
while new_el != "Д":
    new_el = input("Ведите новый элемент множества (для выхода введите Д): ")
    if new_el != "Д":
        if int(new_el) > 0:
            my_list.append(int(new_el))
        else:
            print("Введите натуральное число!")
    my_list.sort(reverse=True)
    print(my_list)
