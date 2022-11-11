# definiše apstraktne tipove koji pretstavlja zgrade, stanove i vlasnike

class Vlasnik:
    '''Defini apstraktni tip koji postavlj vlasnike stanova (osobe).'''

    def __init__(self, ime, prezime, jmbg):
        self._prez_ime = prezime + ' ' + ime
        if jmbg.isdigit() and len(jmbg) == 13:
            self.__jmbg = jmbg
        else:
            raise Exception('JMBG nije validan.')

    def __str__(self):
        return '{}\t{}'.format(self._prez_ime, self.__jmbg)

    def jmbg(self):
        return self.__jmbg

    def ime(self):
        return self._prez_ime

    def sadrži(self, upit):
        '''Vraća True ako je upit sastavni deo (prez)imena'''
        return self._prez_ime.find(upit) != -1

class Stan:
    '''Definiše apstraktni tip koji pretstavlja stanove.'''

    def __init__(self, m2, sprat, vlasnik = None):
        self._m2, self.__sprat, self._vlasnik = m2, sprat, vlasnik

    def __str__(self):
        return '{}.spr,\t{}m2\nVl. {}'.format(self.__sprat,
                                            self._m2, self._vlasnik)

    def vlasnik(self):
        return self._vlasnik

    def promeni_vlasnika(self, novi_vlasnik):
        self._vlasnik = novi_vlasnik

    def površina(self):
        return self._m2

class Zgrada:
    '''Definiše apstraktni tip koji pretstavlja zgradu'''
        
    def __init__(self, adresa, stanovi):
        self._adresa, self._stanovi = adresa, stanovi

    def __str__(self):

        opis = [self._adresa + '\n' + '-'*len(self._adresa)]
        for stan in self._stanovi:
            opis.append(str(stan))
        return '\n\n'.join(opis)+'\n\n'
        
    def dodaj_stan(self, stan):
        self._stanovi.append(stan)

    def stanovi_vlasnika(self, upit):
        '''Vraća rečnik sa ključ: vlasnic čije ime sadrži upit i
            vrednost: stanovi vlasnika.'''

        vlasnik_stanovi = {}
        for stan in self._stanovi:
            v = stan.vlasnik()
            if v != None and v.sadrži(upit):
                v_stanovi = vlasnik_stanovi.get(v.jmbg, [])
                v_stanovi.append(stan)
                vlasnik_stanovi[v.jmbg] = v_stanovi
                
        return vlasnik_stanovi
    
# test program

# Kreiranje vlasnike
try:
    raja = Vlasnik('Raja', 'Patković', '0901985123456')
    gaja = Vlasnik('Gaja', 'Patković', '0901985123457')
    vlad = Vlasnik('Vlad', 'Patković', '0901985123458')
except Exception as e:
    print(e)

# Kreiranje stanova i zgrade
s0_1 = Stan(50, 0, raja)
s0_2 = Stan(100, 0, gaja)
s1_1 = Stan(75, 1, vlad)
s1_2 = Stan(75, 1, gaja)
zgrada1 = Zgrada('Kneza Miloša 15', [s0_1, s0_2, s1_1, s1_2])

# Promena vlasnika
s1_2.promeni_vlasnika(raja)

# Dodavanje stana
s2_1 = Stan(150, 2)
zgrada1.dodaj_stan(s2_1)

# Ispis podataka o zgradi
print(zgrada1)

# Vlasnici u zgradi koji u imenu imaju 'aja'
print('Vlasnici sa "aja" u imenu i njihovi stanovi: \n')
for stanovi in zgrada1.stanovi_vlasnika('aja').values():
    v = stanovi[0].vlasnik()
    total = 0
    for stan in stanovi:
        print(stan, '\n')
        total += stan.površina()        
    print('{} ima {} stanova, ukupne površine {}m2.\n'.format(v,
                                        len(stanovi), total))
