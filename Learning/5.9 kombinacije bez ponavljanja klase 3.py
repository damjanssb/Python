#kombinacije bez ponavljanja treće klase za elemente liste

def kombinacije3k(lista):
    '''Pravi kombinaciju treće klase bez ponavljanja od elemenata iz liste'''

    rezultat = []
    n = len(lista)
    if n < 3:
        return rezultat

    for i in range(0,n-2):
        for j in range (i+1,n-1):
            for k in range (j+1,n):
                rezultat.append([lista[i],lista[j],lista[k]])
    return rezultat
    
boje = ['crvena', 'plava', 'zelena', 'žuta']
rezultat = kombinacije3k(boje)
for i in rezultat:
    print(i)
