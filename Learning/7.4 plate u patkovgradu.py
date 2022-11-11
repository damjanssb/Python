# Counting sort metoda
# plate su [20, 15, 10, 20, 25, 30, 50, 30, 50, 1000, 950]

def counting_sort(L, maks):
    '''Sortira listu L, Counting sort metodom.
       maks je najveća očekivana vrednost unutar liste.'''
    B = [0 for i in range(maks + 1)]
    for i in L:
        B[i] += 1
    k = 0
    for i in range(maks + 1):
        for j in range(B[i]):
            L[k] = i
            k += 1

def medijana(L):
    '''Vraća medijamu za učitanu listu L'''
    n = len(L)       
    if n % 2 == 0:
        return (L[n//2-1] + L[n//2])/2
    else:
        return L[n//2]

#Test: plate u Patkovgradu
plate = [20, 15, 10, 20, 25, 30, 50, 30, 50, 1000, 950]
maks_plata = max(plate)
print('Pre sortiranja', plate)
counting_sort(plate, maks_plata)
print('Posle sortiranja', plate)
print('Prosečna plata u Patkovgradu je', medijana(plate))
