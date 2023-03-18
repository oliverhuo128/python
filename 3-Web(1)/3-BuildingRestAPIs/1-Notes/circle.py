import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius *self.radius

    def perimeter(self):
        return 2*math.pi * self.radius
    
    def summary(self):
        return f"are = {self.area()}, circumference = {self.circumference()}"