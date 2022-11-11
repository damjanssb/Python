#Raspoređuje osam dama na šahovsku tablu tako da se međusobno ne napadaju
import itertools as it

def dame(n):
    '''Pravi kombinacije za postavljanje n dama na tabli nxn.'''

    def provera(p):
        '''Za potencijalno rešenje p, proverava da li je i pravo.'''
        n = len(p)
        for i in range(n-1):
            for j in range(i+1, n):
                 if abs(i - j) == abs(p[i] - p[j]):
                    return False
        return True

    def prikaz(rešenje):
        '''Prikazuje pozicije dama za pronađeno rešenje.'''
        for i in rešenje:
            print((i-1)*'#'+'d'+(n-i)*'#')
        print('')
        
    br_rešenja = 0
    for p in it.permutations(range(1, n+1)):
        if provera(p):
            prikaz(p)
            br_rešenja += 1
    return br_rešenja     
        
n = int(input('Unesi n za broj dama i table nxn. '))
br_rešenja = dame(n)
print('Za n = {} ima ukupno {} rešenja.'.format(n, br_rešenja))
