import unittest

from ..RejestrKont import RejestrKont
from ..Konto import Konto

class TestAccountRegister(unittest.TestCase):

    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "99123456789"

    def test_1_dodanie_konta(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        RejestrKont.dodaj_konto(konto)
        self.assertEqual(RejestrKont.zwroc_ilosc_kont(), 1)

    def test_2_dodanie_konta_drugie(self):
        konto_drugie = Konto(self.imie, self.nazwisko, self.pesel)
        RejestrKont.dodaj_konto(konto_drugie)
        self.assertEqual(RejestrKont.zwroc_ilosc_kont(), 2)

    def test_3_wyszukaj_konto(self):
        konto_trzecie = Konto(self.imie, self.nazwisko, "98123456789")
        RejestrKont.dodaj_konto(konto_trzecie)
        self.assertEqual(RejestrKont.wyszukaj_konto_osobiste("98123456789"), konto_trzecie)
