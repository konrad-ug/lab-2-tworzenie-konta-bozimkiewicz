import unittest
from parameterized import parameterized

from ..Konto import Konto

class TestTakeALoanParameterized(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "99123456789"

    def setUp(self):
        self.konto = Konto(self.imie, self.nazwisko, self.pesel)

    @parameterized.expand([
        ([], False),
        ([500, 500, 500], True),
        ([500, -500, 500], False),

    ])
    def test_zaciagnij_kredyt_warunek_pierwszy(self, historia, wynik_wniosku):
        self.konto.historia = historia
        czy_przyznano = self.konto.check_zaciagnij_kredyt_ostatnie_transakcje_wplaty()

        self.assertEqual(czy_przyznano, wynik_wniosku)

    @parameterized.expand([
        ([], 1000, False),
        ([-100, 500, 500, -300, 500], 1000, True),
        ([-250, 500, 500, -300, 500], 1000, False)
    ])
    def test_zaciagnij_kredyt_warunek_drugi(self, historia, kwota, wynik_wniosku):
        self.konto.historia = historia
        czy_przyznano = self.konto.check_zaciagnij_kredyt_suma_transakcji(kwota)
        
        self.assertEqual(czy_przyznano, wynik_wniosku)

    @parameterized.expand([
        ([], 1000, 0, False),
        ([500, 500, 500], 1000, 1000, True),
        ([-100, 500, 500, -300, 500], 1000, 1000, True),
        ([500, -500, 500], 1000, 0, False),
        ([-250, 500, 500, -300, 500], 1000, 0, False)
    ])
    def test_zaciagnij_kredyt_kwota(self, historia, kwota, saldo, wynik_transakcji):
        self.konto.historia = historia

        self.konto.zaciagnij_kredyt(kwota)

        self.assertEqual(self.konto.saldo, saldo)
        self.assertEqual(self.konto.zaciagnij_kredyt(1000), wynik_transakcji)    