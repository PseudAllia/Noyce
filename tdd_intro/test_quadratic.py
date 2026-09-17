import pytest

from quadratic import solve_quadratic, discriminant


def test_solve_quadratic():
    assert solve_quadratic(1, 4, -21) == (-7, 3)


def test_solve_quadratic_2():
    assert solve_quadratic(1, 0, -49) == (-7, 7)

def test_solve_quadratic_equal_roots():
    assert solve_quadratic(1, -6, 9) == (3, 3)

@pytest.mark.parametrize("a, b, c, expected",
                         [
                             [1,-6,9,(3,3)],
                             [4,4,1,(-0.5,-0.5)],
                             [1,2,1,(-1,-1)]
                        ]
                         )
def test_solve_quadratic(a, b, c, expected):
    assert solve_quadratic(a, b, c) == expected

def test_solve_quadratic_3():
    with pytest.raises(Exception):
        solve_quadratic(1, 0, 20)

def test_solve_quadratic_zero_coefficient():
    with pytest.raises(ZeroDivisionError):
        solve_quadratic(0, 1, 1)


def test_discriminant():
    assert discriminant(1, 2, 3) == -8
