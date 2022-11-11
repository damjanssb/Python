# server: deli_server.py
# poziva se iz 8.1.1 deli_klijent
# proverava da li je tekst validan ceo broj

def je_ceo(tekst):
    '''Proverava da li je argument tekst validan ceo broj.'''
    if tekst == '':
        return False
    elif tekst[0] == '-':
        return tekst[1:].isdigit()
    else:
        return tekst.isdigit()

def deli(x, y):
    ''' Funkcija vraća (status, x/y) za validno x i y.
        status: 0 - sve je ok, 1 - deljenje sa 0
                2 - x ne valja, 3 - y ne valja'''
    if je_ceo(x):
        if je_ceo(y):
            x, y = int(x), int(y)
            if y == 0:
                return (1, 0)
            else:
                return (0, x/y)
        else:
            return (3, 0)
    else:
        return (2, 0)
