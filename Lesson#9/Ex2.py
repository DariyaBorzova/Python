class NewClass(type):
    _attr = None

    def __call__(cls):
        if cls._attr == None:
            cls._attr == super(NewClass, cls).__call__()
        return cls._attr


class My_Class(metaclass=NewClass):
    pass


obj1 = My_Class()
obj2 = My_Class()

print(obj1 is obj2)
