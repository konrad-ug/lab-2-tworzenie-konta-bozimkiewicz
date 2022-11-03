import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe

class TestHistoryOfOperations(unittest.TestCase):
    def test_historia_po_przelewie_przychodzacym(self):
        konto = Konto('Adam', 'Nowak', '99123456789')
        konto.saldo = 500

        konto.zaksieguj_przelew_przychodzacy(300)
        self.assertEqual(konto.historia, [300])

    def test_historia_po_przelewie_wychodzacym(self):
        konto = Konto('Adam', 'Nowak', '99123456789')
        konto.saldo = 500

        konto.zaksieguj_przelew_wychodzacy(300)
        self.assertEqual(konto.historia, [-300])

    def test_historia_po_przelewie_wychodzacym_nieudany(self):
        konto = Konto('Adam', 'Nowak', '99123456789')
        konto.saldo = 500

        konto.zaksieguj_przelew_wychodzacy(600)
        self.assertEqual(konto.historia, [])

    def test_historia_po_serii_przelewow(self):
        konto = Konto('Adam', 'Nowak', '99123456789')
        konto.saldo = 500

        konto.zaksieguj_przelew_przychodzacy(500)
        konto.zaksieguj_przelew_wychodzacy(300)
        konto.zaksieguj_przelew_przychodzacy(250)

        self.assertEqual(konto.historia, [500, -300, 250])

    def test_historia_po_serii_przelewow_nieudany(self):
        konto = Konto('Adam', 'Nowak', '99123456789')
        konto.saldo = 500

        konto.zaksieguj_przelew_wychodzacy(700)
        konto.zaksieguj_przelew_przychodzacy(500)
        konto.zaksieguj_przelew_wychodzacy(300)
        konto.zaksieguj_przelew_przychodzacy(250)

        self.assertEqual(konto.historia, [500, -300, 250])

    def test_historia_po_przelewie_ekspresowym(self):
        konto_pierwsze = Konto('Adam', 'Nowak', '99123456789')
        konto_pierwsze.saldo = 500
        konto_drugie = Konto('Tomasz', 'Kowalski', '50123456789')
        konto_drugie.saldo = 1000

        konto_drugie.wykonaj_przelew_ekspresowy(500, konto_pierwsze)

        self.assertEqual(konto_pierwsze.historia, [500, -1])
        self.assertEqual(konto_drugie.historia, [-500, -1])

    def test_historia_po_przelewie_ekspresowym_nieudany(self):
        konto_pierwsze = Konto('Adam', 'Nowak', '99123456789')
        konto_pierwsze.saldo = 500
        konto_drugie = Konto('Tomasz', 'Kowalski', '50123456789')
        konto_drugie.saldo = 1000

        konto_drugie.wykonaj_przelew_ekspresowy(1500, konto_pierwsze)

        self.assertEqual(konto_pierwsze.historia, [])
        self.assertEqual(konto_drugie.historia, [])

    def test_historia_po_przelewie_ekspresowym_konta_firmowe(self):
        konto_pierwsze = KontoFirmowe('Testowanie ltd.', '1234567890')
        konto_pierwsze.saldo = 1000
        konto_drugie = KontoFirmowe('Testowanie sp. z o.o.', '9876543210')
        konto_drugie.saldo = 1000

        konto_drugie.wykonaj_przelew_ekspresowy(500, konto_pierwsze)

        self.assertEqual(konto_pierwsze.historia, [500, -5])
        self.assertEqual(konto_drugie.historia, [-500, -5])

    def test_historia_po_przelewie_ekspresowym_konta_firmowe_nieudany(self):
        konto_pierwsze = KontoFirmowe('Testowanie ltd.', '1234567890')
        konto_pierwsze.saldo = 1000
        konto_drugie = KontoFirmowe('Testowanie sp. z o.o.', '9876543210')
        konto_drugie.saldo = 1000

        konto_drugie.wykonaj_przelew_ekspresowy(1500, konto_pierwsze)

        self.assertEqual(konto_pierwsze.historia, [])
        self.assertEqual(konto_drugie.historia, [])
