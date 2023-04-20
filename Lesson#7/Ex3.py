class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"wage": 0, "bonus": 0}


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname
    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self._income['wage'] = wage
        self._income['bonus'] = bonus


a = Position("Иван", "Петров", 35000, 20000)
print(a.get_full_name())
print(a.get_total_income())











