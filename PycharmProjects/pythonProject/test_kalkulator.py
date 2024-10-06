import math
import pytest
from kalkulator import (
    dodaj, odejmij, pomnoz, podziel, pierwiastek, kwadrat, wartosc_bezwzgledna,
    konwersja_celsjusz_na_fahrenheit, konwersja_fahrenheit_na_celsjusz,
    konwersja_kilometry_na_mile, konwersja_mile_na_kilometry,
    konwersja_litry_na_galony, konwersja_galony_na_litry,
    konwersja_kilogramy_na_funt, konwersja_funt_na_kilogramy, procent_z_liczby
)

# Testy dla operacji arytmetycznych
def test_dodaj():
    assert dodaj(2, 3) == 5
    assert dodaj(-1, 1) == 0
    assert dodaj(0, 0) == 0

def test_odejmij():
    assert odejmij(10, 5) == 5
    assert odejmij(-1, -1) == 0
    assert odejmij(0, 5) == -5

def test_pomnoz():
    assert pomnoz(2, 3) == 6
    assert pomnoz(-2, 3) == -6
    assert pomnoz(0, 100) == 0

def test_podziel():
    assert podziel(10, 2) == 5
    assert podziel(10, 0) == "Nie można dzielić przez zero!"
    assert podziel(0, 5) == 0

# Testy dla funkcji matematycznych
def test_pierwiastek():
    assert pierwiastek(9) == 3
    assert pierwiastek(0) == 0
    assert pierwiastek(-4) == "Nie można wyciągnąć pierwiastka z liczby ujemnej!"

def test_kwadrat():
    assert kwadrat(4) == 16
    assert kwadrat(-3) == 9
    assert kwadrat(0) == 0

def test_wartosc_bezwzgledna():
    assert wartosc_bezwzgledna(10) == 10
    assert wartosc_bezwzgledna(-10) == 10
    assert wartosc_bezwzgledna(0) == 0

# Testy dla konwersji temperatury
def test_konwersja_celsjusz_na_fahrenheit():
    assert konwersja_celsjusz_na_fahrenheit(0) == 32
    assert konwersja_celsjusz_na_fahrenheit(100) == 212
    assert konwersja_celsjusz_na_fahrenheit(-40) == -40

def test_konwersja_fahrenheit_na_celsjusz():
    assert konwersja_fahrenheit_na_celsjusz(32) == 0
    assert konwersja_fahrenheit_na_celsjusz(212) == 100
    assert konwersja_fahrenheit_na_celsjusz(-40) == -40

# Testy dla konwersji odległości
def test_konwersja_kilometry_na_mile():
    assert konwersja_kilometry_na_mile(1) == pytest.approx(0.621371)
    assert konwersja_kilometry_na_mile(0) == 0

def test_konwersja_mile_na_kilometry():
    assert konwersja_mile_na_kilometry(1) == pytest.approx(1.60934)
    assert konwersja_mile_na_kilometry(0) == 0

# Testy dla konwersji objętości
def test_konwersja_litry_na_galony():
    assert konwersja_litry_na_galony(1) == pytest.approx(0.264172)
    assert konwersja_litry_na_galony(0) == 0

def test_konwersja_galony_na_litry():
    assert konwersja_galony_na_litry(1) == pytest.approx(3.78541)
    assert konwersja_galony_na_litry(0) == 0

# Testy dla konwersji masy
def test_konwersja_kilogramy_na_funt():
    assert konwersja_kilogramy_na_funt(1) == pytest.approx(2.20462)
    assert konwersja_kilogramy_na_funt(0) == 0

def test_konwersja_funt_na_kilogramy():
    assert konwersja_funt_na_kilogramy(1) == pytest.approx(0.453592)
    assert konwersja_funt_na_kilogramy(0) == 0

# Testy dla procentów
def test_procent_z_liczby():
    assert procent_z_liczby(200, 10) == 20
    assert procent_z_liczby(100, 50) == 50
    assert procent_z_liczby(0, 10) == 0
