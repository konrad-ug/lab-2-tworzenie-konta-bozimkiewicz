from app.Konto import Konto

class KontoFirmowe(Konto):

    def __init__(self, nazwa_firmy, nip):
        self.nazwa_firmy = nazwa_firmy
        self.saldo = 0
        self.business_acc = True
        self.historia = []

        self.obsluga_nipu(nip)

    def obsluga_nipu(self, nip):
        self.nip = nip if len(nip) == 10 else 'Niepoprawny NIP!'
