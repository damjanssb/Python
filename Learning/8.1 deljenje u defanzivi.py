# Defanzivno programiranje
# Proverava da li je uneta vrednost ceo broj

def je_ceo(x):
    if len(x) == 0:
        return False
    elif x[0] == '-':
        return x[1:].isdigit()
    else:
        return x.isdigit()

def podeli(x, y):
    return x / y

while True:
    x = input('x = ')
    y = input('y = ')
    if je_ceo(x) and je_ceo(y):
        x, y = int(x), int(y)
        if y != 0:
            print('x / y =', podeli(x, y))
            break
        else:
            print('Delilac nesme biti nula.')
            print('Pokušaj ponovo.')
    else:
        print('Unete vrednost moraju biti celi brojevi.')
        print('Pokušaj ponovo.')
