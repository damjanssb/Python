# kreirati klasu koja hipotetički prodaje viceve
# cene viceva su 5, 10 i 20 din. Vraća kusur
# vicomat se puni vicevima iz tekstualne datoteke
# vicevi se biraju slučajno

class Vicomat:

    @staticmethod
    def uplata(unos):
        if unos in {5, 10, 20}:
            return unos
        else:
            raise Exception('Unos mora da bude 5, 10 ili 20')
        
    # poziva se iz konstruktora prilikom kreiranja objekta
    def __init__(self, cena):
        
        self.__iznos = 0
        self.__cena = Vicomat.uplata(cena)
        
        try:
            with open('D:\\Programi\\New folder\\Python\\vicevi.txt') as vicevi:
                self.__vicevi = vicevi.read().split('\n\n')
        except:
            raise Exception('problem sa učitavanjem viceva')

    # unosi novu cenu vica
    def cena_vica(self):
        print('cena vica je', self.__cena)

    def ubaci_novac(self, uplata):
        self.__iznos += Vicomat.uplata(uplata)
        print('na stanju je', self.__iznos)

    def kupi_vic(self):
        if self.__iznos >= self.__cena:
            import random as r
            print(r.choice(self.__vicevi))
            self.__iznos -= self.__cena
            print('ostalo je još', self.__iznos)
        else:
            raise Exception('Nije uplaćeno dovoljno novca.')

    def vrati_kusur(self):
        if self.__iznos > 0:
            print('Vraćam kusur u iznosu od', self.__iznos)
            self.__iznos = 0
        else:
            print('Nema kusura')
        return True

    def __str__(self):
        return '{}'.format(self.__vicevi)

# test program
# zaštita od pokretanja testa programa ako se uvede kao modul u drugi modul
if __name__ == '__main__':
    A = Vicomat(10)
    izlaz = False
    while not izlaz:
        try:
            proces = input('unesi: c (za cenu), u (za uplatu), v (za vic) ili k (za kusur): ')
            if proces == 'c':
                A.cena_vica()
            elif proces == 'u':
                uplata = int(input('Koliko upaćuješ? '))
                uplata = A.uplata(uplata)
                A.ubaci_novac(uplata)
            elif proces == 'v':
                A.kupi_vic()
            elif proces == 'k':
                izlaz = A.vrati_kusur()
        except Exception as e:
            print(e)
