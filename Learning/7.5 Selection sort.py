# Selection sort metoda

def selection_sort(L):
    '''Sortira listu L, Selection sort metodom.'''
    n = len(L)
    for i in range(n-1):
        '''L.insert(i, min(L[i:]))
        del L[L[i+1:].index(min(L[i+1:])) + i+1]'''
        j = L[i:].index(min(L[i:]))
        L[i], L[j+i] = L[j+i], L[i]

#Test
import time as t
L = [10, 20, 1, 2, 3, 5, 1, 15, 0, -10]
print('Pre  sortiranja ', L)
selection_sort(L)
print('Posle sortiranja', L)

print('{:6}\t{:8}'.format('n', 'Tnajnep'))
for i in range(1,7):
    n = 500*i
    l = [k for k in range(n, 0, -1)]
    start = t.perf_counter()
    selection_sort(l)
    t_nnep = t.perf_counter() - start
    print('{:<6}\t{:8.6f}'.format(n, t_nnep))
