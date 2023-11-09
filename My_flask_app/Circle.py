import math

class Circle():
    def __init__(self, radius = 1):
        self.radius = radius        
    
    def getPerimeter(self):
        Perimeter = 2 * self.radius * math.pi
        return str(Perimeter)

    def getArea(self):
        Area = math.pi * self.radius**2
        return str(Area)

    def setRadius(self, radius):
        self.radius = radius
