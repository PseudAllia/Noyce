import math


def solve_quadratic(a: float, b: float, c: float) -> tuple[float, float]:
    if discriminant(a, b, c) < 0:
        raise Exception('Discriminant cannot be negative')

    x1 = ( -b - math.sqrt(discriminant(a, b, c))) / (2 * a)
    x2 = ( -b + math.sqrt(discriminant(a, b, c))) / (2 * a)

    return x1, x2

def discriminant(a: float, b: float, c: float) -> float:
    return b ** 2 - 4 * a * c

if __name__ == '__main__':
    solve_quadratic(0, 1, 1)
