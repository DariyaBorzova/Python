proceeds = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
if proceeds > costs:
    print("Финансовый результат: прибыль. Её размер =",
          proceeds - costs)
    rent = int(proceeds - costs) / proceeds
    print("Рентабельность = ", rent)
    employee = int(input("Введите количество сотрудников: "))
    profit_emp = (proceeds - costs) / employee
    print("Прибыль фирмы в расчете на одного сотрудника = ", profit_emp)
elif proceeds == costs:
    print("Финансовый результат: ноль.")
else:
    print("Финансовый результат: убыток.")
