import unittest

from ..Konto import Konto

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
