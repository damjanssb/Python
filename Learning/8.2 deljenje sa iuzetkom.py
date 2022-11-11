# simulacija serveta
# obrada izuzetka
def deli(x, y):
    ''' Funkcija vraća količnik x/y za validno x i y.'''
    kol, poruka = 0, None
    try:
        kol = int(x) / int(y)
    except ValueError:
        poruka = 'x i y moraju biti celi brojevi.'
    except ZeroDivisionError:
        poruka = 'y ne sme biti 0.'
    except:
        poruka = 'Nepoznata greška.'
    return (poruka, kol)


# test klijent
try:
    while True:
        x, y = input('x = '), input('y = ')
        por, kol = deli(x, y)
        if por == None:
            print('x / y =', kol)
        else:
            print(por)
except KeyboardInterrupt:
    print('Aj zdravo.')
