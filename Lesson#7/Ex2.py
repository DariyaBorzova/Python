class Road:
    _length = 0
    _width = 0
    weight = 0
    depth = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_weight(self):
        return self._width * self._length * self.weight * self.depth


x = Road(5000,20)
x.weight = 25
x.depth = 0.05
print(x.calc_weight())
