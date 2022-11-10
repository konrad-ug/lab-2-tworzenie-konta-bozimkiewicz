import unittest

from ..Konto import Konto

class TestTakeALoan(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "99123456789"
  
    def test_zaciagnij_kredyt_historia_mniejsza_niz_3_warunek_pierwszy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        czy_przyznano = konto.check_zaciagnij_kredyt_ostatnie_transakcje_wplaty()

        self.assertFalse(czy_przyznano)

    def test_zaciagnij_kredyt_historia_mniejsza_niz_5_warunek_drugi(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        czy_przyznano = konto.check_zaciagnij_kredyt_suma_transakcji(1)

        self.assertFalse(czy_przyznano)

    def test_zaciagnij_kredyt_udany_warunek_pierwszy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [500, 500, 500]
        czy_przyznano = konto.check_zaciagnij_kredyt_ostatnie_transakcje_wplaty()

        self.assertTrue(czy_przyznano)

    def test_zaciagnij_kredyt_udany_warunek_drugi(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [-100, 500, 500, -300, 500]
        czy_przyznano = konto.check_zaciagnij_kredyt_suma_transakcji(1000)
        
        self.assertTrue(czy_przyznano)

    def test_zaciagnij_kredyt_nieudany_warunek_pierwszy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [500, -500, 500]
        czy_przyznano = konto.check_zaciagnij_kredyt_ostatnie_transakcje_wplaty()

        self.assertFalse(czy_przyznano)

    def test_zaciagnij_kredyt_nieudany_warunek_drugi(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [-250, 500, 500, -300, 500]
        czy_przyznano = konto.check_zaciagnij_kredyt_suma_transakcji(1000)

        self.assertFalse(czy_przyznano)

    def test_zaciagnij_kredyt_kwota_dodana_warunek_pierwszy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [500, 500, 500]

        konto.zaciagnij_kredyt(1000)

        self.assertEqual(konto.saldo, 1000)

    def test_zaciagnij_kredyt_kwota_dodana_warunek_drugi(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [-100, 500, 500, -300, 500]

        konto.zaciagnij_kredyt(1000)

        self.assertEqual(konto.saldo, 1000)

    def test_zaciagnij_kredyt_kwota_niedodana_warunek_pierwszy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [500, -500, 500]

        konto.zaciagnij_kredyt(1000)

        self.assertEqual(konto.saldo, 0)

    def test_zaciagnij_kredyt_kwota_niedodana_warunek_drugi(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [-250, 500, 500, -300, 500]

        konto.zaciagnij_kredyt(1000)

        self.assertEqual(konto.saldo, 0)
