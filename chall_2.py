import math


class Circle:
    def __init__(self,r):
        self.r = r

    def calculate_area(self):
        return math.pi ** 2 * self.r


a_circle = Circle(4)
print(a_circle.calculate_area())
