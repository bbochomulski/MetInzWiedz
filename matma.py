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

#obliczanie "linii trendu"

punkty = [(2, 1), (5, 2), (7, 3), (8, 3)]

x = np.array([np.array([1 for _ in range(len(punkty))]), np.array([x[0] for x in punkty])])
y = [y[1] for y in punkty]

B = (np.dot(x,x)) ** -1

print(B)



# Beta = (Xt*x)^-1*Xt*y