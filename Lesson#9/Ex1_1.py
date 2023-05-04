import time

class TrafficColor:
    def __set__(self, instance, value):
        if value != "red" and value != "yellow" and value != "green":
            raise ValueError("Указан неверный цвет")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class TrafficLight:
    __color = TrafficColor()

    def running(self):
        self.__color = "red"
        print(self.__color)
        time.sleep(7)
        self.__color = "yellow1"
        print(self.__color)
        time.sleep(2)
        self.__color = "green"
        print(self.__color)
        time.sleep(5)


tl = TrafficLight()
tl.running()