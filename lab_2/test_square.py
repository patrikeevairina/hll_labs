import math

from square import Circle, Triangle, Rectangle


def test_circle_incorrect_init():
    incorrect_r = (-5, 0)
    for radius in incorrect_r:
        try:
            c = Circle(radius)
            assert not isinstance(c, Circle)
        except Exception:
            assert True


def test_circle_correct_init():
    correct_radius = (3, 4.5, math.pi)
    for radius in correct_radius:
        try:
            c = Circle(radius)
            assert isinstance(c, Circle)
        except Exception:
            assert False
    assert True


def test_triangle_incorrect_init():
    incorrect_sides = ((1, 2, 3), (-2, 0, 2), (0, 0, 1), (-3, -4, -5), (-3, 4, -5))
    for sides in incorrect_sides:
        try:
            t = Triangle(sides[0], sides[1], sides[2])
            assert not isinstance(t, Triangle)
        except Exception:
            assert True


def test_triangle_correct_init():
    correct_sides = ((3, 4, 5), (math.e, math.pi, 1))
    for sides in correct_sides:
        try:
            t = Triangle(sides[0], sides[1], sides[2])
            assert isinstance(t, Triangle)
        except Exception:
            assert False
    assert True


def test_rectangle_incorrect_init():
    incorrect_sides = ((0, 0), (-1, -4), (3, 4), (5, -3), (0, 2), (5, 0))
    for sides in incorrect_sides:
        try:
            r = Rectangle(sides[0], sides[1])
            assert not isinstance(r, Rectangle)
        except Exception:
            assert True


def test_rectangle_correct_init():
    correct_sides = ((3, 5.6), (math.e, math.pi))
    for sides in correct_sides:
        try:
            r = Rectangle(sides[0], sides[1])
            assert isinstance(r, Rectangle)
        except Exception:
            assert False
    assert True


def test_shapes_types():
    circle_attr = "Circle"
    triangle_attr = "Triangle"
    rectangle_attr = "Rectangle"
    other_attr = "Other"

    c = Circle(4)
    t = Triangle(3, 4, 5)
    r = Rectangle(4, 5)

    assert c.type == circle_attr
    assert t.type == triangle_attr
    assert r.type == rectangle_attr

    try:
        c.type = other_attr
        assert c.type == circle_attr
    except Exception:
        assert c.type == circle_attr

    try:
        t.type = other_attr
        assert t.type == triangle_attr
    except Exception:
        assert t.type == triangle_attr

    try:
        r.type = other_attr
        assert r.type == rectangle_attr
    except Exception:
        assert r.type == rectangle_attr
