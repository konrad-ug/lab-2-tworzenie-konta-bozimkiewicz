class RejestrKont():
    konta = []

    @classmethod
    def dodaj_konto(cls, konto):
        RejestrKont.konta.append(konto)

    @classmethod
    def zwroc_ilosc_kont(cls):
        return len(RejestrKont.konta)

    @classmethod
    def wyszukaj_konto_osobiste(cls, pesel):
        for konto in RejestrKont.konta:
            if konto.pesel == pesel:
                return konto

    @classmethod
    def usun_konto_osobiste(cls, pesel):
        for konto in RejestrKont.konta:
            if konto.pesel == pesel:
                cls.konta.remove(konto)
