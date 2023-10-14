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


def test_triangle_incorrect_init():
    incorrect_sides = ((1, 2, 3), (-2, 0, 2), (0, 0, 1), (-3, -4, -5), (-3, 4, -5))
    for sides in incorrect_sides:
        try:
            t = Triangle(sides[0], sides[1], sides[2])
            if isinstance(t, Triangle):
                assert False
        except Exception:
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

