from vector import Vector
import math

v1_x = (-3, 0, 5, 9)
v1_y = (-5, 0, 7, 9)

v2_x = (-15, 0, 34, 9)
v2_y = (-6, 0, 2, 9)

v1_list = list()
v2_list = list()

for x1 in v1_x:
    for y1 in v1_y:
        for x2 in v2_x:
            for y2 in v2_y:
                v1_list.append(Vector(x1, y1))
                v2_list.append(Vector(x2, y2))


def compare(v, v_before):
    x_eq = v.x() == v_before.x()
    y_eq = v.y() == v_before.y()
    return x_eq and y_eq


def test_add():
    for v1 in v1_list:
        for v2 in v2_list:
            v1_before = Vector(v1.x(), v1.y())
            v2_before = Vector(v2.x(), v2.y())
            v3 = v1 + v2
            assert v3.x() == v1.x() + v2.x()
            assert v3.y() == v1.y() + v2.y()
            assert compare(v1, v1_before) is True
            assert compare(v2, v2_before) is True


def test_eq():
    for v1 in v1_list:
        for v2 in v2_list:
            x_eq = v1.x() == v2.x()
            y_eq = v1.y() == v2.y()
            v_eq = v1 == v2
            assert v_eq == (x_eq and y_eq)


def test_neq():
    for v1 in v1_list:
        for v2 in v2_list:
            x_neq = v1.x() != v2.x()
            y_neq = v1.y() != v2.y()
            v_neq = v1 != v2
            assert v_neq == (x_neq or y_neq)


def test_mul_num():
    for v in v1_list:
        for num in v2_x:
            x_mul_num = v.x() * num
            y_mul_num = v.y() * num
            assert x_mul_num == (v * num).x()
            assert y_mul_num == (v * num).y()


def test_mul_vec():
    for v1 in v1_list:
        for v2 in v2_list:
            res_vec = Vector(v1.x() * v2.x(), v1.y() * v2.y())
            assert (v1 * v2).x() == res_vec.x()
            assert (v1 * v2).y() == res_vec.y()


def test_length():
    for v in v1_list:
        length = v.x() ** 2 + v.y() ** 2
        length = length ** 0.5
        assert math.isclose(v.length(), length)
