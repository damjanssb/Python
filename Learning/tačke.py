# kreiranje klase
# Klasa Tačka pretstavlja tačke u dvodimenzionalnom kordinatnom sistemu
# sadrži metode __init__ , __str__ , __eq__ , __add__ i rastojanje_do()

import time as t

class Tačka:
    '''Pretstavlja tačke u ravni definisane sa x i y'''
    br_tačaka, t_kreiranja  = 0, ' - '
    
    @staticmethod
    def statistika(jezik):
        if jezik == 'e':
            p1, p2 = '# of created points: ', 'last point created: '
        else:
            p1, p2 = 'broj kreiranih tačaka', 'poslednja tačka kreirana: '

        print(p1, Tačka.br_tačaka)
        print(p2, Tačka.t_kreiranja, '\n')
        
    # poziva se iz konstruktora prilikom kreiranja objekta
    def __init__(self, x = 0, y = 0):
        self._x = x      # definiše atribut x za krirani objekat
        self._y = y      # definiše atribut y za krirani objekat

        Tačka.br_tačaka += 1
        Tačka.t_kreiranja = t.asctime(t.localtime())

    def daj_x(self):
        return self._x
    def daj_y(self):
        return self._y

    def postavi_x(self, b):
        self._x = b
    def postavi_y(self, b):
        self._y = b

    # vraća rastoanje od tačke nad kojom se poziva metoda do zadate tačke
    def rastojanje_do(self, t):
        import math
        dx, dy = self._x - t._x, self._y - t._y
        return math.sqrt(dx**2 + dy**2)

    # vraća string sa koordinatama tačke nad kojom se poziva metoda
    def __str__(self):
        return '({:<f}, {:<f})'.format(self._x, self._y)

    # proverava da li je tačka nad kojom se poziva metoda jednaka sa zadatom
    def __eq__(self, t):
        if isinstance(t, Tačka):
            return self._x == t._x and self._y == t._y
        return False

    # vektorski sabira tačku nad kojom se poziva metoda sa zadatom tačkom
    def __add__(self, t):
        return Tačka(self._x + t._x, self._y + t._y)

# test program
if __name__ == '__main__':
    Tačka.statistika('s')
    a = Tačka()
    print(a)
    a.statistika('e')
    t.sleep(1)
    print(Tačka(1, -1))
    Tačka.statistika('s')
