# šifruje i dešifruje poruke
# treba dešifrovati ïÕËÕÝáCéÍCËÅßÅéCíCm

def de_šifrovanje(š):
    poruka=input('Unesi poruku koju želiš da šifruješ. \n')
    a=int(input('Unesi koeficijent a. '))
    b=int(input('Unesi koeficijent b. '))
    izlaz=''

    if š=='š':
        for k in poruka:
            izlaz+=chr(a*ord(k)+b)
        print('Šifrovana poruka glasi: ', izlaz)
    elif š=='d':
        for k in poruka:
            izlaz+=chr((ord(k)-b)//a)
        print('Dešifrovana poruka glasi: ', izlaz)

š=input('''Unesi: \nš ako želiš da šifruješ, \nd ako želiš da dešifruješ
ili bilo koji drugi karakter za izlaz. ''')

while š=='š' or š=='d':
    de_šifrovanje(š)
    š=input('''\nUnesi: \nš ako želiš da šifruješ, \nd ako želiš da dešifruješ
ili bilo koji drugi karakter za izlaz. ''')
