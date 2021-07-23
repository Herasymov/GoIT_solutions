# создать класс Rectangle с полями 2-х сторон и методами площади и периметра

class Rectangle:
    def __init__(self, s1, s2):
        self.a = s1
        self.b = s2

    def perimetr(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


rec1 = Rectangle(5, 4)
print("Perimetr:", rec1.perimetr())
print("Area:", rec1.area())

rec2 = Rectangle(5, 2)
print("Perimetr:", rec2.perimetr())
print("Area:", rec2.area())
