class Konto:
    def __init__(self, imie, nazwisko, pesel, kupon_rabatowy = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        
        self.obsluga_peselu(pesel)
        if (self.obsluga_kuponu_rabatowego_kupon(kupon_rabatowy) 
        and self.obsluga_kuponu_rabatowego_wiek(kupon_rabatowy)):
            self.saldo = 50

    def obsluga_peselu(self, pesel):
        if len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel"

    def obsluga_kuponu_rabatowego_kupon(self, kupon):
        if (kupon != None and kupon[:5] == 'PROM_' and len(kupon) == 8):
            return True
        
    def obsluga_kuponu_rabatowego_wiek(self, kupon):
        if (int(self.pesel[2:4]) > 20 or int(self.pesel[:2]) > 60):
            return True
