import unittest
from kalkulator import (
    dodaj, odejmij, pomnoz, podziel, pierwiastek, kwadrat, wartosc_bezwzgledna,
    konwersja_celsjusz_na_fahrenheit, konwersja_fahrenheit_na_celsjusz,
    konwersja_kilometry_na_mile, konwersja_mile_na_kilometry,
    konwersja_litry_na_galony, konwersja_galony_na_litry,
    konwersja_kilogramy_na_funt, konwersja_funt_na_kilogramy, procent_z_liczby
)

class TestKalkulator(unittest.TestCase):

    # Testy dla operacji arytmetycznych
    def test_dodaj(self):
        self.assertEqual(dodaj(2, 3), 5)
        self.assertEqual(dodaj(-1, 1), 0)
        self.assertEqual(dodaj(0, 0), 0)

    def test_odejmij(self):
        self.assertEqual(odejmij(10, 5), 5)
        self.assertEqual(odejmij(-1, -1), 0)
        self.assertEqual(odejmij(0, 5), -5)

    def test_pomnoz(self):
        self.assertEqual(pomnoz(2, 3), 6)
        self.assertEqual(pomnoz(-2, 3), -6)
        self.assertEqual(pomnoz(0, 100), 0)

    def test_podziel(self):
        self.assertEqual(podziel(10, 2), 5)
        self.assertEqual(podziel(10, 0), "Nie można dzielić przez zero!")
        self.assertEqual(podziel(0, 5), 0)

    # Testy dla funkcji matematycznych
    def test_pierwiastek(self):
        self.assertEqual(pierwiastek(9), 3)
        self.assertEqual(pierwiastek(0), 0)
        self.assertEqual(pierwiastek(-4), "Nie można wyciągnąć pierwiastka z liczby ujemnej!")

    def test_kwadrat(self):
        self.assertEqual(kwadrat(4), 16)
        self.assertEqual(kwadrat(-3), 9)
        self.assertEqual(kwadrat(0), 0)

    def test_wartosc_bezwzgledna(self):
        self.assertEqual(wartosc_bezwzgledna(10), 10)
        self.assertEqual(wartosc_bezwzgledna(-10), 10)
        self.assertEqual(wartosc_bezwzgledna(0), 0)

    # Testy dla konwersji temperatury
    def test_konwersja_celsjusz_na_fahrenheit(self):
        self.assertEqual(konwersja_celsjusz_na_fahrenheit(0), 32)
        self.assertEqual(konwersja_celsjusz_na_fahrenheit(100), 212)
        self.assertEqual(konwersja_celsjusz_na_fahrenheit(-40), -40)

    def test_konwersja_fahrenheit_na_celsjusz(self):
        self.assertEqual(konwersja_fahrenheit_na_celsjusz(32), 0)
        self.assertEqual(konwersja_fahrenheit_na_celsjusz(212), 100)
        self.assertEqual(konwersja_fahrenheit_na_celsjusz(-40), -40)

    # Testy dla konwersji odległości
    def test_konwersja_kilometry_na_mile(self):
        self.assertAlmostEqual(konwersja_kilometry_na_mile(1), 0.621371, places=6)
        self.assertEqual(konwersja_kilometry_na_mile(0), 0)

    def test_konwersja_mile_na_kilometry(self):
        self.assertAlmostEqual(konwersja_mile_na_kilometry(1), 1.60934, places=5)
        self.assertEqual(konwersja_mile_na_kilometry(0), 0)

    # Testy dla konwersji objętości
    def test_konwersja_litry_na_galony(self):
        self.assertAlmostEqual(konwersja_litry_na_galony(1), 0.264172, places=6)
        self.assertEqual(konwersja_litry_na_galony(0), 0)

    def test_konwersja_galony_na_litry(self):
        self.assertAlmostEqual(konwersja_galony_na_litry(1), 3.78541, places=5)
        self.assertEqual(konwersja_galony_na_litry(0), 0)

    # Testy dla konwersji masy
    def test_konwersja_kilogramy_na_funt(self):
        self.assertAlmostEqual(konwersja_kilogramy_na_funt(1), 2.20462, places=5)
        self.assertEqual(konwersja_kilogramy_na_funt(0), 0)

    def test_konwersja_funt_na_kilogramy(self):
        self.assertAlmostEqual(konwersja_funt_na_kilogramy(1), 0.453592, places=6)
        self.assertEqual(konwersja_funt_na_kilogramy(0), 0)

    # Testy dla procentów
    def test_procent_z_liczby(self):
        self.assertEqual(procent_z_liczby(200, 10), 20)
        self.assertEqual(procent_z_liczby(100, 50), 50)
        self.assertEqual(procent_z_liczby(0, 10), 0)

# Uruchamianie testów
if __name__ == '__main__':
    unittest.main()
