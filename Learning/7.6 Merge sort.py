# Merge sort metoda

def merge_sort(L):
    '''Sortira listu L, Merge sort metodom.'''
    n = len(L)
    if n > 1:
        L1 = merge_sort(L[:n//2])
        L2 = merge_sort(L[n//2:])
        return spajanje(L1, L2)
    else:
        return L

def spajanje(L1, L2):
    '''Spaja sortirane liste L1 i L2 u novoj listi'''    
    spoj, i, j = [], 0, 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            spoj.append(L1[i])
            i += 1
        else:
            spoj.append(L2[j])
            j += 1
            
    return spoj + L1[i:] + L2[j:]
        
#Test
import time as t
L = [10, 20, 1, 2, 3, 5, 1, 15, 0, -10]
print('Pre  sortiranja ', L)
L = merge_sort(L)
print('Posle sortiranja', L)

print('{:9}\t{:9}'.format('n', 'Tnajnep'))
for i in range(1,7):
    n = 10**i
    L = [k for k in range(n, 0, -1)]
    start = t.perf_counter()
    merge_sort(L)
    t_nnep = t.perf_counter() - start
    print('{:<9}\t{:<9.6f}'.format(n, t_nnep))
