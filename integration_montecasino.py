import matplotlib.pyplot as plt
import numpy as np
import random


def func(x):
    return x**2


def monte_casino(f, a, b, epsilon):
    area = 0
    batch = 1000
    x = np.linspace(a, b, batch)
    y = f(x)

    last = 0
    while True:
        area = 0
        for _ in range(batch):
            x_rand = random.uniform(a, b)
            y_rand = random.uniform(min(y), max(y))
            if f(x_rand) > y_rand > 0:
                area += 1
            elif f(x_rand) < y_rand < 0:
                area -= 1

        result = ((b - a) * (max(y) - min(y))) * (area / batch)
        if abs(result - last) < epsilon:
            print(f"roznica: {abs(result - last)}")
            return result
        else:
            batch += 200
            print(f"{result} \t roznica: {abs(result - last)}")
            last = result


def trapezoid(f, a, b, n):
    x = np.linspace(a, b, n)
    y = f(x)
    return np.around(np.trapz(y, x), decimals=2)


def main():
    a = 0
    b = 10
    epsilon = 0.05
    expected = trapezoid(func, a, b, 5000)
    print(f"expected: {expected}")
    area = monte_casino(func, a, b, epsilon)
    print(f"area: {area}")


if __name__ == "__main__":
    main()
