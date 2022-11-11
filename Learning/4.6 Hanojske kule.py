#računa poteze koje treba povući da bi se u najmanje koraka prebacilo
#n diskova na ciljani štap i računa koliko poteza je potrebno povući.

def min_poteza(n):
    '''Računa minimalan broj poteza za
       prebacivanje Hanojeva kula sa n diskova.'''
    if n==1:
        return 1
    else:
        return 2*min_poteza(n-1)+1
        #može i izrazom min_poteza=2**n-1

def hanoj(n, A='A', B='B', C='C'):
    '''n - broj diskova
       A , B i C ne treba unositi, služe samo za kreiranje rekurzije'''
    if n>0:
        hanoj(n-1, A, C, B)
        print('Disk', n, 'sa', A,'na', C)
        hanoj(n-1, B, A, C)

n=int(input('Unesi broj diskova. '))
hanoj(n)
print('Prebačeno je u', min_poteza(n), 'poteza.')
