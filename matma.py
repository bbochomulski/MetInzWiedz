from australian import readfile

australian = readfile("australian.dat")


# oblicz srednia arytmetyczna ze wszystkich tablic zawartych w australian

def srednia_arytmetyczna(obiekt):
    """
        obliczanie sredniej arytmetycznej danego obiektu

        :param obiekt: obiekt
        :return: srednia arytmetyczna elementow obiektu
    """
    suma = 0
    for element in obiekt:
        if isinstance(element, list):
            suma += srednia_arytmetyczna(element)
        elif isinstance(element, float) or isinstance(element, int):
            return sum(obiekt) / len(obiekt)
    return suma / len(obiekt)


# oblicz wariancje ze wszystkich tablic zawartych w australian

def wariancja(macierz):
    """
        obliczanie wariancji elementow macierzy

        :param macierz: macierz
        :return: wariancja elementow macierz
    """
    srednia_macierzy = srednia_arytmetyczna(macierz)
    suma = 0
    for rekord in macierz:
        suma += (srednia_arytmetyczna(rekord) - srednia_macierzy) ** 2
    return suma / len(macierz)


# oblicz odchylenie standardowe ze wszystkich tablic zawartych w australian

def odchylenie_standardowe(macierz):
    """
        obliczanie odchylenia standardowego elementow macierzy

        :param macierz: macierz
        :return: odchylenie standardowe elementow macierz
    """
    return wariancja(macierz) ** 0.5


print("Srednia arytmetyczna:\t{:.4f}".format(srednia_arytmetyczna(australian)))
print("Wariancja:\t\t\t\t{:.4f}".format(wariancja(australian)))
print("Odchylenie standardowe:\t{:.4f}".format(odchylenie_standardowe(australian)))
