import math


# Для того, чтобы можно было прогнать тесты по своим фигурам, необходимо:
# BaseFlat - абстрактный класс, Circle, Rectangle, Triangle - конкретные реализации
# доступ к типу фигуры осуществляется методом класса type
# конструктор Circle принимает в качестве параметра радиус круга
# конструктор Triangle принимает в качестве параметров длины сторон треугольника
# конструктор Rectangle принимает в качестве параметров высоту и ширину
class BaseFlat:  # базовый класс
    _type = "Abstract Figure"

    def square(self):
        raise NotImplementedError()

    @property
    def type(self):
        return self._type


class Circle(BaseFlat):
    _type = "Circle"

    def __new__(cls, radius):
        if radius > 0:
            return super(Circle, cls).__new__(cls)
        else:
            raise ValueError

    def __init__(self, radius):
        self.__radius = radius

    def square(self):
        sq = math.pi * self.__radius ** 2
        return sq


class Triangle(BaseFlat):
    _type = "Triangle"

    def __new__(cls, a, b, c):
        first_cond = (a + b) > c
        second_cond = (b + c) > a
        third_cond = (a + c) > b
        positive_sides_cond = a > 0 and b > 0 and c > 0

        if first_cond and second_cond and third_cond and positive_sides_cond:
            return super(Triangle, cls).__new__(cls)
        else:
            raise ValueError()

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def square(self):
        half_p = (self.__a + self.__b + self.__c) / 2
        s = half_p * (half_p - self.__a) * (half_p - self.__b) * (half_p - self.__c)
        return s


class Rectangle(BaseFlat):
    _type = "Rectangle"

    def __new__(cls, width, height):
        positive_sides_cond = width > 0 and height > 0

        if positive_sides_cond:
            return super(Rectangle, cls).__new__(cls)
        else:
            raise ValueError()

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def square(self):
        return self.__width * self.__height
