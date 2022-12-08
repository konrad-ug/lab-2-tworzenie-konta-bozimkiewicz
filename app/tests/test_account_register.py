import unittest

from ..RejestrKont import RejestrKont
from ..Konto import Konto

class TestAccountRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.konto_pierwsze = Konto("Dariusz", "Januszewski", "99123456789")
        cls.konto_drugie = Konto("Tomasz", "Nowak", "98123456789")
        cls.konto_trzecie = Konto("Adam", "Kowalski", "97123456789")

    def test_1_dodanie_konta(cls):
        RejestrKont.dodaj_konto(cls.konto_pierwsze)
        cls.assertEqual(RejestrKont.zwroc_ilosc_kont(), 1)

    def test_2_dodanie_konta_drugie(cls):
        RejestrKont.dodaj_konto(cls.konto_drugie)
        cls.assertEqual(RejestrKont.zwroc_ilosc_kont(), 2)

    def test_3_wyszukaj_konto(cls):
        RejestrKont.dodaj_konto(cls.konto_trzecie)
        cls.assertEqual(RejestrKont.wyszukaj_konto_osobiste("97123456789"), cls.konto_trzecie)

    @classmethod
    def tearDownClass(cls):
        RejestrKont.konta = []