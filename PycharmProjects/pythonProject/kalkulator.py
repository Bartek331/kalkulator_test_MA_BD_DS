# kalkulator.py

import math


def dodaj(a, b):
    return a + b


def odejmij(a, b):
    return a - b


def pomnoz(a, b):
    return a * b


def podziel(a, b):
    if b != 0:
        return a / b
    else:
        return "Nie można dzielić przez zero!"


def pierwiastek(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Nie można wyciągnąć pierwiastka z liczby ujemnej!"


def kwadrat(a):
    return a ** 2


def wartosc_bezwzgledna(a):
    return abs(a)


def konwersja_celsjusz_na_fahrenheit(celsjusz):
    return (celsjusz * 9 / 5) + 32


def konwersja_fahrenheit_na_celsjusz(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def konwersja_kilometry_na_mile(kilometry):
    return kilometry * 0.621371


def konwersja_mile_na_kilometry(mile):
    return mile / 0.621371


def konwersja_litry_na_galony(litry):
    return litry * 0.264172


def konwersja_galony_na_litry(galony):
    return galony / 0.264172


def konwersja_kilogramy_na_funt(kilogramy):
    return kilogramy * 2.20462


def konwersja_funt_na_kilogramy(funt):
    return funt / 2.20462


def procent_z_liczby(liczba, procent):
    return (liczba * procent) / 100


def kalkulator():
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Pierwiastkowanie")
    print("6. Podnoszenie do kwadratu")
    print("7. Wartość bezwzględna")
    print("8. Konwersja Celsjusz na Fahrenheit")
    print("9. Konwersja Fahrenheit na Celsjusz")
    print("10. Konwersja Kilometry na Mile")
    print("11. Konwersja Mile na Kilometry")
    print("12. Konwersja Litry na Galony")
    print("13. Konwersja Galony na Litry")
    print("14. Konwersja Kilogramy na Funty")
    print("15. Konwersja Funty na Kilogramy")
    print("16. Oblicz procent z liczby")

    wybor = input("Wprowadź numer operacji (1-16): ")

    if wybor in ['1', '2', '3', '4']:
        a = float(input("Wprowadź pierwszą liczbę: "))
        b = float(input("Wprowadź drugą liczbę: "))

        if wybor == '1':
            print(f"Wynik: {dodaj(a, b)}")
        elif wybor == '2':
            print(f"Wynik: {odejmij(a, b)}")
        elif wybor == '3':
            print(f"Wynik: {pomnoz(a, b)}")
        elif wybor == '4':
            print(f"Wynik: {podziel(a, b)}")

    elif wybor in ['5', '6', '7']:
        a = float(input("Wprowadź liczbę: "))

        if wybor == '5':
            print(f"Wynik: {pierwiastek(a)}")
        elif wybor == '6':
            print(f"Wynik: {kwadrat(a)}")
        elif wybor == '7':
            print(f"Wynik: {wartosc_bezwzgledna(a)}")

    elif wybor in ['8', '9']:
        a = float(input("Wprowadź temperaturę: "))

        if wybor == '8':
            print(f"Wynik: {konwersja_celsjusz_na_fahrenheit(a)} °F")
        elif wybor == '9':
            print(f"Wynik: {konwersja_fahrenheit_na_celsjusz(a)} °C")

    elif wybor in ['10', '11']:
        a = float(input("Wprowadź wartość: "))

        if wybor == '10':
            print(f"Wynik: {konwersja_kilometry_na_mile(a)} mil")
        elif wybor == '11':
            print(f"Wynik: {konwersja_mile_na_kilometry(a)} km")

    elif wybor in ['12', '13']:
        a = float(input("Wprowadź objętość: "))

        if wybor == '12':
            print(f"Wynik: {konwersja_litry_na_galony(a)} galonów")
        elif wybor == '13':
            print(f"Wynik: {konwersja_galony_na_litry(a)} litrów")

    elif wybor in ['14', '15']:
        a = float(input("Wprowadź masę: "))

        if wybor == '14':
            print(f"Wynik: {konwersja_kilogramy_na_funt(a)} funtów")
        elif wybor == '15':
            print(f"Wynik: {konwersja_funt_na_kilogramy(a)} kilogramów")

    elif wybor == '16':
        a = float(input("Wprowadź liczbę: "))
        b = float(input("Wprowadź procent: "))
        print(f"Wynik: {procent_z_liczby(a, b)}")

    else:
        print("Nieprawidłowy wybór!")


if __name__ == "__main__":
    kalkulator()
