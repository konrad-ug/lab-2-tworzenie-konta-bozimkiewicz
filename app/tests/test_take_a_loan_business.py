import unittest
from parameterized import parameterized

from ..KontoFirmowe import KontoFirmowe

class TestTakeALoanBusiness(unittest.TestCase):
    nazwa = "Testowanie sp. z o.o."
    nip = "9876543210"

    def setUp(self):
        self.konto = KontoFirmowe(self.nazwa, self.nip)

    @parameterized.expand([
        (1000, 500, [1775], True),
        (0, 500, [1775], False),
        (1000, 500, [], False),
        (0, 500, [], False)

    ])
    def test_zaciagnij_kredyt_konto_biznesowe(self, saldo, kwota, historia, wynik_wniosku):
        self.konto.historia = historia
        self.konto.saldo = saldo
        czy_przyznano = self.konto.zaciagnij_kredyt(kwota)

        self.assertEqual(czy_przyznano, wynik_wniosku)

    @parameterized.expand([
        (1000, 500, [1775], 1500),
        (0, 500, [1775], 0),
        (1000, 500, [], 1000),
        (0, 500, [], 0)

    ])
    def test_zaciagnij_kredyt_konto_biznesowe_kwota(self, saldo, kwota, historia, oczekiwane_saldo):
        self.konto.historia = historia
        self.konto.saldo = saldo
        
        self.konto.zaciagnij_kredyt(kwota)

        self.assertEqual(self.konto.saldo, oczekiwane_saldo)
