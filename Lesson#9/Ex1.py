class NoneNegative:

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value


    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

class Worker:
    wage = NoneNegative()
    bonus = NoneNegative()

    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self.wage = wage
        self.bonus = bonus

    def get_total_income(self):
        return self.wage + self.bonus


a = Worker("Иван", "Петров", 35000, 20000)
print(a.get_total_income())
