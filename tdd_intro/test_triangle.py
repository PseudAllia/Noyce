import pytest

import triangle

def test_equilateral_triangle():
    assert triangle.triangle_type(2, 2, 2) == "equilateral"

@pytest.mark.parametrize(
    "a,b,c,triangle_type",
    [
        (1, 2, 2, "isosceles"),
        (2, 3, 3, "isosceles"),
        (3, 3, 5, "isosceles"),
    ])
def test_isosceles_triangle(a,b,c,triangle_type):
    assert triangle.triangle_type(a,b,c) == triangle_type

def test_not_a_triangle():
    with pytest.raises(Exception):
        t = triangle.triangle_type(2, 2, 6)

def test_negative_sides():
    with pytest.raises(Exception):
        t = triangle.triangle_type(-1, 2, 6)


@pytest.mark.parametrize(
    "a,b,c,triangle_type",
    [
        (3, 4, 5, "right-angled"),
        (13, 5, 12, "right-angled"),
        (8, 10, 6, "right-angled"),
    ])
def test_right_angled(a,b,c,triangle_type):
    assert triangle.triangle_type(a,b,c) == triangle_type

