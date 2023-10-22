# Для того, чтобы можно было прогнать тесты по своему вектору, вектор должен иметь интерфейс:
# конструктор принимает на вход координаты х и у
# доступ к координатам должен осуществляться через методы класса x() и y()
# длина вектора возвращается методом класса length()
class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __add__(self, other):
        x = self.__x + other.x()
        y = self.__y + other.y()
        return Vector(x, y)

    def __str__(self):
        return "<{0}, {1}>".format(self.__x, self.__y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            x = self.__x * other.x()
            y = self.__y * other.y()
            return Vector(x, y)
        else:
            x = self.__x * other
            y = self.__y * other
            return Vector(x, y)

    def __eq__(self, other):
        type_eq = isinstance(other, Vector)
        x_eq = self.__x == other.x()
        y_eq = self.__y == other.y()
        return type_eq and x_eq and y_eq

    def __ne__(self, other):
        x_neq = self.__x != other.x()
        y_neq = self.__y != other.y()
        return x_neq or y_neq

    def length(self):
        vec_len = (self.__x ** 2 + self.__y ** 2) ** 0.5
        return vec_len

    def x(self):
        return self.__x

    def y(self):
        return self.__y

