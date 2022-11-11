import random as r
import tačke as t
# definiše apstraktni tip koji pretstavlja sve krugove u ravni

class Krug:
    '''Definiše krug u ravni pretstavljen centrom i poluprečnikom.'''

    PI =3.14159265359 # klasni atribut, konstanta
        
    # poziva se iz konstruktora prilikom kreiranja objekta
    def __init__(self, x = 0, y = 0, r = 1):
        self._c = t.Tačka(x, y) #definiše centar kruga kao tačku
        self._r = r             #definiše poluprečnik kruga

    # vraća string sa koordinatama tačke nad kojom se poziva metoda
    def __str__(self):
        return 'c = {}, r = {:<f}'.format(str(self._c), self._r)

    # proverava da li se data tačka nalazi u krugu
    def unutra(self, t):
        return self._c.rastojanje_do(t) <= self._r

    # računa površinu kruga
    def površina(self):
        return self._r**2 * Krug.PI
    
    # računa obim kruga
    def obim(self):
        return 2 * self._r * Krug.PI

    ''' Ovo funkcioniše ali profesor procenjuje da ne treba
    # pristup atributima _x, _y i _r
    def daj_x(self):
        return self._c.daj_x()
    def daj_y(self):
        return self._c.daj_y()
    def daj_r(self):
        return self._r

    # upisivanje atributa _x, _y i _r
    def postavi_x(self, b):
        self._c.postavi_x(b)
    def postavi_y(self, b):
        self._c.postavi_y(b)
    def postavi_r(self, b):
        self._r = b'''

# test program: zaštita od pokretanja testa programa kada se uvodi kao modul
if __name__ == '__main__':

    # pravi jedinični krug k i ispisuje njegove karakteristike
    k = Krug()
    print(k)
    o, p = k.obim(), k.površina()
    print('O = {:<f}\tP = {:<f}'.format(o, p))
    # generiše 7 slučajnih tačaka i ispisuje da li su u k ili nisu
    for i in range(7):
        tt = t.Tačka(r.uniform(-2, 2), r.uniform(-2, 2))
        po = 'van kruga.'
        if k.unutra(tt):
            po = 'u krugu.'
        print ('Tačka {:>22} je {}'.format(str(tt), po))
