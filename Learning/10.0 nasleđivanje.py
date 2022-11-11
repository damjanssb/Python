# Predstavlja sve osobe u informacionom sistemu fakulteta
class Osoba:

    def __init__(self, ime, prezime, jmbg):
        self._ime, self._prezime, self._jmbg = ime, prezime, jmbg

    def __str__(self):
        return '{} {}, {}'.format(self._ime, self._prezime, self._jmbg)

    def prdstavi_se(self):
        print('Ja sam', self._ime, self._prezime)

# Predstavlja osobu zaposlenu na fakultetu
class Zaposleni(Osoba): # izvođenje (nasleđivanje) iz klase Osoba

    def __init__(self, ime, prezime, jmbg, plata, soba, telefon):
        super().__init__(ime, prezime, jmbg) #priroda osobe
        self._plata, self._soba, self._telefon = plata, soba, telefon

    def __str__(self):
        return super().__str__() + '\nplata: ' + str(self._plata) + \
               '\tsoba: ' + self._soba + '\ttel:' + self._telefon

    def promeni_platu(self, nova):
        self._plata = nova

# predstavlja studente na fakultetu
class Student(Osoba): # izvođenje (nasleđivanje) iz klase Osoba

    def __init__(self, ime, prezime, jmbg, indeks, smer):
        super().__init__(ime, prezime, jmbg) #priroda osobe
        self._indeks, smer._godine, self._smer = indeks, 1, smer        

    def __str__(self):
        return super().__str__() + '\nindeks: ' + self._indeks + \
               '\tgodina: ' + str(self._godina) + '\tsmer:' + self._smer

    def upiši_godinu(self, godina):
        if godina < 6 and (self._godina == godina or self._godina + 1 == godina):
            self._godina = godina
