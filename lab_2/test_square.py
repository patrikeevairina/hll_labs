import math

from square import Circle, Triangle, Rectangle


def test_circle_incorrect_init():
    incorrect_r = (-5, 0)
    for radius in incorrect_r:
        try:
            c = Circle(radius)
            if isinstance(c, Circle):
                assert False
        except Exception:
            assert True


def test_circle_correct_init():
    correct_radius = (3, 4.5, math.pi)
    for radius in correct_radius:
        try:
            c = Circle(radius)
            if not isinstance(c, Circle):
                assert False
        except Exception:
            assert False
    assert True


def test_triangle_incorrect_init():
    incorrect_sides = ((1, 2, 3), (-2, 0, 2), (0, 0, 1), (-3, -4, -5), (-3, 4, -5))
    for sides in incorrect_sides:
        try:
            t = Triangle(sides[0], sides[1], sides[2])
            if isinstance(t, Triangle):
                assert False
        except Exception:
            assert True


def test_triangle_correct_init():
    correct_sides = ((3, 4, 5), (math.e, math.pi, 1))
    for sides in correct_sides:
        try:
            t = Triangle(sides[0], sides[1], sides[2])
            if not isinstance(t, Triangle):
                assert False
        except Exception:
            assert False
    assert True


def test_rectangle_incorrect_init():
    incorrect_sides = ((0, 0), (-1, -4), (3, 4), (5, -3), (0, 2), (5, 0))
    for sides in incorrect_sides:
        try:
            r = Rectangle(sides[0], sides[1])
            if isinstance(r, Rectangle):
                assert False
        except Exception:
            assert True


def test_rectangle_correct_init():
    correct_sides = ((3, 5.6), (math.e, math.pi))
    for sides in correct_sides:
        try:
            r = Rectangle(sides[0], sides[1])
            if not isinstance(r, Rectangle):
                assert False
        except Exception:
            assert False
    assert True

