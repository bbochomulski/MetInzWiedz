import random
import math
import numpy as np


def wczytaj(nazwa_pliku):
    """
    wczytaj z pliku australian.dat liste wektorow

    :param file_name: nazwa pliku
    :return: lista wektorow
    """
    wektory = []
    with open(nazwa_pliku, 'r') as file:
        for line in file.readlines():
            wektory.append(tuple(map(lambda x: float(x), line.split())))
    return wektory


def przypisz_klasy(wektory, ilosc_klas):
    """
    przypisz randomowe klasy decyzyjne i umiesc je w slowniku {randomowa_klasa: [lista_wektorow]}

    :param wektory: lista wektorow
    :param ilosc_klas: ilosc klas
    :return: slownik {randomowa_klasa: [lista_wektorow]}
    """
    klasy_wektory = {}
    for i in range(ilosc_klas):
        klasy_wektory[float(i)] = []
    # klasy_wektory = {
    #     0.0: [],
    #     1.0: [],
    # }
    for wektor in wektory:
        klasy_wektory[random.choice(list(klasy_wektory.keys()))].append(wektor)

    return klasy_wektory


def odleglosc(wektor1, wektor2):
    """
    wyznaczenie odleglosci miedzy dwoma wektorami

    :param wektor1: wektor
    :param wektor2: wektor
    :return: odleglosc
    """
    a = np.array(wektor1) - np.array(wektor2)
    return math.sqrt(np.dot(a, a))


def odleglosci_do_wszystkich_wektorow(wektory):
    """
    wyznaczenie odleglosci dla kazdego wektora return: slownik {wektor: suma_odleglosci_do_wszystkich_wektorow}

    :param wektory: lista wektorow
    :return: slownik {wektor: suma_odleglosci_do_wszystkich_wektorow}
    """
    odleglosci = {}
    for wektor in wektory:
        suma_odleglosci = 0
        for wektor2 in wektory:
            suma_odleglosci += odleglosc(wektor, wektor2)
        odleglosci[wektor] = suma_odleglosci
    return odleglosci


def srodek_masy(klasy_wektory):
    """
    wyznaczenie srodka masy ktory jest wektorem z najmniejsza odlegloscia do pozostalych wektorow z tej samej klasy

    :param klasy_wektory: slownik {klasa: [lista wektorow]}
    :return: slownik {klasa: srodek_masy}
    """
    srodki_masy = {}
    for klasa in klasy_wektory:
        odleglosci = odleglosci_do_wszystkich_wektorow(klasy_wektory[klasa])
        srodki_masy[klasa] = min(odleglosci, key=odleglosci.get)
    return srodki_masy


def zmiana_klasy(klasy_wektory, srodki_masy):
    """
    zmiana klasy wektora na klase najblizsza srodkiem masy

    :param klasy_wektory: slownik {klasa: [lista wektorow]}
    :param srodki_masy: slownik {klasa: srodek_masy}
    :return: liczba zmian
    """
    liczba_zmian = 0
    for klasa, lista_wektorow in klasy_wektory.items():
        for wektor in lista_wektorow:
            odleglosci = []
            for k, v in srodki_masy.items():
                odleglosci.append((k, odleglosc(wektor, v)))
            najblizszy_srodek_masy = min(odleglosci, key=lambda x: x[1])
            if klasa != najblizszy_srodek_masy[0]:
                liczba_zmian += 1
                klasy_wektory[najblizszy_srodek_masy[0]].append(wektor)
                klasy_wektory[klasa].remove(wektor)
    return liczba_zmian


if __name__ == '__main__':
    ilosc_klas_decyzyjnych = 4

    wektory = wczytaj('australian.dat')
    klasy_wektory = przypisz_klasy(wektory, ilosc_klas_decyzyjnych)

    zmiany = -1
    iteracje = 0
    while zmiany != 0:
        iteracje += 1
        srodki_masy = srodek_masy(klasy_wektory)
        zmiany = zmiana_klasy(klasy_wektory, srodki_masy)
        print("Liczba zmian: {}".format(zmiany))

    # assert len(klasy_wektory[0]) == 637 and len(klasy_wektory[1]) == 53

    suma = 0
    print("\nKlasa \t|\t Liczba Elementow")
    print("------------------------------")
    for klasa, lista in klasy_wektory.items():
        print(f"{klasa} \t|\t {len(lista)}")
        suma += len(lista)

    print("\nSuma: {}".format(suma))
    print("Ilosc iteracji: {}".format(iteracje))
