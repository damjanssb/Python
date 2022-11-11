# Igra pogađanja broja iz intervala [1,n] u m pokušaja
import random as r

def partija(n, m):
    '''Organizuje igru pogađanja broja iz intrvala [1,n] u m pokušaja.
        Ukoliko se ne pogodi broj iz m pokušaja, igra se nastavlja
        sa novim brojem i nivih m pokušaja. Na kraju vraća broj pokušaja'''

    slučajan_broj = r.randint(1,n)
    print('Računar je zamislio broj.')
    broj_pokušaja = 0
    while True:
        pokušaj = int(input('Unesi novi pokušaj. '))
        broj_pokušaja += 1
        if pokušaj > n or pokušaj < 1:
            return 0
        elif pokušaj == slučajan_broj:
            return broj_pokušaja
        elif broj_pokušaja % m == 0:
            slučajan_broj = r.randint(1,n)
            print('Računar je zamislio novi broj.')

while True:
    n = int(input('Unesi gornju granicu n. '))
    m = int(input(' Unesi broj pokušaja m. '))
    if m < 1 or n < m:
        print('Izlaz iz igre usled ne validnog unosa.')
        break
    broj_pokušaja = partija(n, m)
    if broj_pokušaja == 0:
        print('Izlaz iz igre usled ne validnog unosa.')
        break
    else:
        print('Pogodio si iz {} pokušaja'.format(broj_pokušaja))
