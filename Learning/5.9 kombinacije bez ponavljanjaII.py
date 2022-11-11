# kombinacija bez ponavljanja klase k

def kombinacije(lista, k):
    '''Kreira kombinacije bez ponavljanja klase k za listu'''
    def formiraj(lista, brojač):
        '''Unosi novu kombinaciju u listu svih kombinacija'''
        return [lista[i] for i in brojač]
    def uvećaj_brojač (brojač, n):
        '''Kreira novi brojač koji će se koristiti kao sito
        za kreiranjenove nove kombinacije.'''
        for i in range(1, len(brojač) + 1):
            if brojač[-i] < n - i:
                brojač[-i] += 1
                for k in range (i-1, 0, -1):
                    brojač[-k] = brojač[-k-1] + 1
                return True
        return False
    
    kombinacije, n = [], len(lista)
    if n < k or k < 1:
        return kombinacije
    
    brojač = [i for i in range(k)]
    kombinacije.append(formiraj(lista, brojač))
    while uvećaj_brojač(brojač, n):
        kombinacije.append(formiraj(lista, brojač))

    return kombinacije
    
#unos
lista = []
k = int(input('Unesi klasu permutacija. '))
while True:
    element = input('Unesi element liste (bez elementa za kraj). ')
    if element == '':
        break
    lista.append(element)
    
#test   
kombinacije = kombinacije(lista, k)
for b in kombinacije:
    print(b)
