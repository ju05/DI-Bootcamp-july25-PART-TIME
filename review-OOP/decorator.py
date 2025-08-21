import math

#DECORATORS

class Circle:

    def __init__(self, radius=0, diameter=0):
        self.radius = radius
        self.diameter = diameter
        self._color = None 

    @classmethod
    def from_diameter(cls, diameter):
        diameter = diameter
        radius = round(diameter/2)
        return cls(radius, diameter)
    
    @staticmethod
    def area_from_radius(radius):
        return math.pi * (radius ** 2)
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color
        return self
    

# circle1 = Circle(diameter = 10)
# print(circle1.radius)
# print(circle1.diameter)

circle2 = Circle.from_diameter(10)
circle2.color = 'red'
print(circle2.color)
# print(circle2.radius)
# print(circle2.diameter)

# print(circle2.area_from_radius(circle2.radius))