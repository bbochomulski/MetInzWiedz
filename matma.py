import numpy as np
import pandas as pd


def srednia(wektor):
    """
    Obliczenie sredniej wektora

    :param wektor: wektor
    :return: srednia
    """
    wektor = np.array(wektor)
    jednostkowa = np.array([1 for _ in range(len(wektor))])
    return np.dot(wektor, jednostkowa) / len(wektor)


def wariancja(wektor):
    """
        obliczanie wariancji elementow wektora

        :param wektor: wektor
        :return: wariancja elementow wektora
    """
    srednia_macierzy = srednia(wektor)
    suma = 0
    for wartosc in wektor:
        suma += (wartosc - srednia_macierzy) ** 2
    return suma / len(wektor)


def odchylenie_standardowe(wektor):
    """
        obliczanie odchylenia standardowego elementow wektora

        :param wektor: wektor
        :return: odchylenie standardowe elementow wektora
    """
    return wariancja(wektor) ** 0.5


wektor_testowy = [1, 2, 3, 4, 5, 6]

test = {
    "Srednia": srednia(wektor_testowy),
    "Wariancja": wariancja(wektor_testowy),
    "Odchylenie standardowe": odchylenie_standardowe(wektor_testowy)
}

print(pd.DataFrame(data=test, index=[""]))


punkty = [(2, 1), (5, 2), (7, 3), (8, 3)]

x = np.array([[1, x[0]] for x in punkty])
y = np.array([y[1] for y in punkty])

beta = np.dot(np.dot(np.linalg.inv(np.dot(x.T, x)), x.T), y)
print(beta)

# Beta = (Xt*x)^-1*Xt*y


import matplotlib.pyplot as plt

plt.plot([x[0] for x in punkty], [y[1] for y in punkty], 'ro')
plt.plot([x[0] for x in punkty], [beta[0] + beta[1] * x[0] for x in punkty], 'b')
plt.show()
