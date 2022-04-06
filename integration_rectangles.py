# create function for integration using rectangles

import numpy as np


def integrate(f, a, b, n):
    """
    This function integrates a function f from a to b using rectangles.
    """
    h = (b - a) / n
    sum = 0
    for i in range(n):
        sum += f(a + i * h)
    return sum * h


def f(x):
    return np.sin(x)


if __name__ == "__main__":
    print("integrate(f, 0, 1, 10) =", integrate(f, 0, 10, 10))
    print("integrate(f, 0, 1, 100) =", integrate(f, 0, 10, 100))
    print("integrate(f, 0, 1, 1000) =", integrate(f, 0, 10, 1000))
    print("integrate(f, 0, 1, 10000) =", integrate(f, 0, 10, 10000))
