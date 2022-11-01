import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe

class TestHandleFundsTransfer(unittest.TestCase):
    
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "99123456789"
    nazwa = 'Testowanie sp. z o.o.'
    nip = '9876543210'

    def test_udany_przelew_przychodzacy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        
        konto.zaksieguj_przelew_przychodzacy(250)
        self.assertEqual(konto.saldo, 750)

    def test_udany_przelew_wychodzacy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        
        konto.zaksieguj_przelew_wychodzacy(250)
        self.assertEqual(konto.saldo, 250)

    def test_nieudany_przelew_wychodzacy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        
        konto.zaksieguj_przelew_wychodzacy(750)
        self.assertEqual(konto.saldo, 500)
        self.assertEqual(konto.zaksieguj_przelew_wychodzacy(750), 'Za mało środków na koncie')

    def test_udany_przelew_ekspresowy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto_biznesowe = KontoFirmowe(self.nazwa, self.nip)
        konto_biznesowe.saldo = 100
        
        konto.wykonaj_przelew_ekspresowy(300, konto_biznesowe)
        
        self.assertEqual(konto.saldo, 199)
        self.assertEqual(konto_biznesowe.saldo, 395)
    
    def test_nieudany_przelew_ekspresowy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto_biznesowe = KontoFirmowe(self.nazwa, self.nip)
        konto_biznesowe.saldo = 100
        
        konto.wykonaj_przelew_ekspresowy(600, konto_biznesowe)
        
        self.assertEqual(konto.saldo, 500)
        self.assertEqual(konto_biznesowe.saldo, 100)
        
    def test_udany_przelew_ekspresowy_oplata_ponizej_zera_dla_zwyklego_konta(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto_biznesowe = KontoFirmowe(self.nazwa, self.nip)
        konto_biznesowe.saldo = 100
        
        konto.wykonaj_przelew_ekspresowy(500, konto_biznesowe)
        
        self.assertEqual(konto.saldo, -1)
        self.assertEqual(konto_biznesowe.saldo, 595)
        
    def test_udany_przelew_ekspresowy_oplata_ponizej_zera_dla_konta_biznesowego(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto_biznesowe = KontoFirmowe(self.nazwa, self.nip)
        konto_biznesowe.saldo = 100
        
        konto_biznesowe.wykonaj_przelew_ekspresowy(100, konto)
        
        self.assertEqual(konto.saldo, 599)
        self.assertEqual(konto_biznesowe.saldo, -5)