# создать классы фигура, прямоугольник, трекгольник и круг. у фигуры стороны это список и методы площадь.
# эти аргументы переопределяются и добавляется title.
from cmath import pi


class Figure:
    sides = []

    def area(self):
        return "Some area"

    def get_sides(self):
        return self.sides

    def set_sides(self, list_of_sides):
        self.sides = list_of_sides


class Rectangle(Figure):
    sides = [1, 2]

    def area(self):
        return self.sides[0] * self.sides[1]


class Circle(Figure):
    radius = 5

    def area(self):
        return pi * (self.radius ** 2)


class SomeFigure(Figure):
    sides = [3, 5, 3, 2, 7]


c = Circle()
c.radius = 7
print(c.sides)
print(c.radius)
print(c.area())

r = Rectangle()
print(r.sides)
print(r.area())

sm = SomeFigure()
print(sm.sides)
print(sm.area())
