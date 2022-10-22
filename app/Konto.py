import re

class Konto:
    def __init__(self, imie, nazwisko, pesel, kupon_rabatowy = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        
        self.obsluga_peselu(pesel)
        self.obsluga_kuponu_rabatowego(kupon_rabatowy)

    def obsluga_peselu(self, pesel):
        if len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel"

    def obsluga_kuponu_rabatowego(self, kupon):
        if kupon != None and re.search("PROM_", kupon) != None and len(kupon) == 8:
            self.saldo = 50
