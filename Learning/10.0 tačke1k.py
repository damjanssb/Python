# kreiranje klase
# Klasa Tačka pretstavlja tačke u I kvadrantu koordinatnog sistema
# sadrži metode __init__ , __str__ , __eq__ , __add__ i rastojanje_do()
# statička metoda statistika i klasni atributi br_tačaka i t_kreiranja
# skrivene informacije atributi _x i _y i metode daj() i postavi()

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
    def __init__(self, x, y):
        if x > 0 and y > 0:
            self.__x, self.__y = x, y # _x i _y su privatni atributi
        else:
            raise Exception('x i/ili y pogrešni.')

        Tačka.br_tačaka += 1
        Tačka.t_kreiranja = t.asctime(t.localtime())

    # pristup atributima _x i _y
    def daj_x(self):
        return self.__x
    def daj_y(self):
        return self.__y

    # upisivanje atributa _x i _y
    def postavi_x(self, b):
        if b > 0:
            self.__x = b
        else:
            raise Exception('Argument mora biti pozitivan broj.')
    def postavi_y(self, b):
        if b > 0:
            self.__y = b
        else:
            raise Exception('Argument mora biti pozitivan broj.')

    # vraća rastoanje od tačke nad kojom se poziva metoda do zadate tačke
    def rastojanje_do(self, t):
        import math
        dx, dy = self.__x - t.__x, self.__y - t.__y
        return math.sqrt(dx**2 + dy**2)

    # vraća string sa koordinatama tačke nad kojom se poziva metoda
    def __str__(self):
        return '({:<f}, {:<f})'.format(self.__x, self.__y)

    # proverava da li je tačka nad kojom se poziva metoda jednaka sa zadatom
    def __eq__(self, t):
        if isinstance(t, Tačka):
            return self.__x ==t.__x and self.__y == t.__y
        return False

    # vektorski sabira tačku nad kojom se poziva metoda sa zadatom tačkom
    def __add__(self, t):
        return Tačka(self.__x + t.__x, self.__y + t.__y)

# test program
# zaštita od pokretanja testa programa ako se uvede kao modul u drugi modul
if __name__ == '__main__':
    Tačka.statistika('s')
    a = Tačka(1,2)
    print(a)
    a.statistika('e')
