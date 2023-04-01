shop = []
number = 1
ans = "да"
while ans == "да":
    name = input("Введите нименование товара: ")
    cost = input("Введите цену товара: ")
    kol = input("Введите количество товара: ")
    ed = input("Введите ед. измерения: ")
    my_dict = {"Наименование": name, "Цена": cost, "Количество": kol,
               "Ед.": ed}
    shop.append(tuple([number, my_dict]))
    ans = input("Хотите добавить товар?")
    number += 1
print(shop)
product_names = []
product_costs = []
product_kol = []
product_ed = []
for product in shop:
    product_names.append(product[1]["Наименование"])
    product_costs.append(product[1]["Цена"])
    product_kol.append(product[1]["Количество"])
    product_ed.append(product[1]["Ед."])
analytics = {"Названия": product_names, "Цены": product_costs, "Количества": product_kol, "Ед.": product_ed}
print(analytics)