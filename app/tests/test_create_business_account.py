import unittest

from ..KontoFirmowe import KontoFirmowe

class TestCreateBusinessBankAccount(unittest.TestCase):
    
    nazwa = 'Testowanie sp. z o.o.'
    nip = '9876543210'

    def test_tworzenie_konta(self):
        konto = KontoFirmowe(self.nazwa, self.nip)
        self.assertEqual(konto.nazwa_firmy, self.nazwa)
        self.assertEqual(konto.nip, self.nip)
        self.assertEqual(konto.saldo, 0)

    def test_nip_za_krotki(self):
        niepoprawny_nip = '123'
        konto = KontoFirmowe(self.nazwa, niepoprawny_nip)
        self.assertEqual(konto.nip, 'Niepoprawny NIP!')

    def test_nip_za_dlugi(self):
        niepoprawny_nip = '12345678901'
        konto = KontoFirmowe(self.nazwa, niepoprawny_nip)
        self.assertEqual(konto.nip, 'Niepoprawny NIP!')
