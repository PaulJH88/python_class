import math

class Shape:
    color = "Red"                           #class variable

class Square(Shape):
    def __init__(self, length):             #instance variable
        # super().__init__(self)
        self.length = length

    def area(self):
        print("Area of Square: ",self.length*self.length)
        print("Color: ",self.color)

class Circle(Shape):
    def __init__(self, radius):
          # super().__init__(self)
         self.radius = radius

    def area(self):
        print("Area of Circle: ",math.pi*self.radius*self.radius)
        print("Color: ",self.color)
class Triangle(Shape):
    def __init__(self, base, height):
        # super().__init__(self)
        self.base = base
        self.height = height

    def area(self):
        print("Area of Triangle: ",self.base*self.height/2)
        print("Color: ",self.color)

class Rectangle(Square):
    def __init__(self, length, breadth):
        super().__init__(length)
        self.breadth = breadth

    def area(self):
        print("Area of Rectangle: ",self.length*self.breadth)
        print("Color: ",self.color)

sq = Square(10)
sq.area()
rect = Rectangle(10, 20)
rect.area()