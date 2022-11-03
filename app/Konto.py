class Konto:
    def __init__(self, imie, nazwisko, pesel, kupon_rabatowy = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.business_acc = False
        self.historia = []
        
        self.obsluga_peselu(pesel)
        if (self.obsluga_kuponu_rabatowego_kupon(kupon_rabatowy) 
        and self.obsluga_kuponu_rabatowego_wiek()):
            self.saldo = 50

    def obsluga_peselu(self, pesel):
        if len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel"

    def obsluga_kuponu_rabatowego_kupon(self, kupon):
        if (kupon != None and kupon[:5] == 'PROM_' and len(kupon) == 8):
            return True
        
    def obsluga_kuponu_rabatowego_wiek(self):
        if (int(self.pesel[2:4]) > 20 or int(self.pesel[:2]) > 60):
            return True

    def zaksieguj_przelew_przychodzacy(self, kwota: int):
        self.saldo += kwota
        self.historia.append(kwota)
    
    def zaksieguj_przelew_wychodzacy(self, kwota: int):
        if kwota > self.saldo:
            return 'Za mało środków na koncie'
        else:
            self.saldo -= kwota
            self.historia.append(-kwota)
    
    def wykonaj_przelew_ekspresowy(self, kwota: int, otrzymujacy: 'Konto'):
        if kwota > self.saldo:
            return False
        else:
            self.zaksieguj_przelew_wychodzacy(kwota)
            self.oplata_za_zaksiegowanie()
            otrzymujacy.zaksieguj_przelew_przychodzacy(kwota)
            otrzymujacy.oplata_za_zaksiegowanie()
            
    def oplata_za_zaksiegowanie(self):
        if self.business_acc:
            self.saldo -= 5
            self.historia.append(-5)
        else:
            self.saldo -= 1
            self.historia.append(-1)

    def metoda_bez_testow(self):
        pass
