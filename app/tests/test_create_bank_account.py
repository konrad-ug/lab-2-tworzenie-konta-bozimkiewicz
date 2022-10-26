import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "99123456789"
    pesel_senior = "45123456789"
    kupon = "PROM_ABC"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "99123456789")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, "99123456789", "Pesel nie został zapisany")

    def test_pesel_prawidlowy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(len(konto.pesel), 11, "Nieprawidłowa długość peselu")

    def test_pesel_za_krotki(self):
        zly_pesel = "123"
        konto = Konto(self.imie, self.nazwisko, zly_pesel)
        self.assertEqual(konto.pesel, "Niepoprawny pesel")

    def test_pesel_za_dlugi(self):
        zly_pesel = "99123456789123"
        konto = Konto(self.imie, self.nazwisko, zly_pesel)
        self.assertEqual(konto.pesel, "Niepoprawny pesel")

    def test_kupon_rabatowy_prawidlowy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, self.kupon)
        self.assertEqual(konto.saldo, 50, "Saldo nie równa się 50zł po użyciu kuponu")

    def test_kupon_rabatowy_za_krotki(self):
        zly_kupon = 'PROM_'
        konto = Konto(self.imie, self.nazwisko, self.pesel, zly_kupon)
        self.assertEqual(konto.saldo, 0, "Saldo nie równa się 0zł po użyciu złego kuponu")

    def test_kupon_rabatowy_za_dlugi(self):
        zly_kupon = 'PROM_ABCD'
        konto = Konto(self.imie, self.nazwisko, self.pesel, zly_kupon)
        self.assertEqual(konto.saldo, 0, "Saldo nie równa się 0zł po użyciu złego kuponu")

    def test_kupon_rabatowy_dla_seniorow(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel_senior, self.kupon)
        self.assertEqual(konto.saldo, 0, "Saldo nie równa się 0zł")
