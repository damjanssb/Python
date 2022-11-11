# Binarno pretraživanje
import time as t

def bin_pretraga(L, x):
    start, stop = 0, len(L)-1
    while start <= stop:
        sredina = (start + stop) // 2
        if L[sredina] > x:
            stop = sredina - 1
        elif L[sredina] < x:
            start = sredina + 1
        else:
            return sredina
    return None

#testiranje za najnepovoljniji slučaj
print('{:8}\t{}'.format('n', 'Tnajnep'))
for i in range(1, 8):
    n = 10 ** i
    L = [k for k in range(n)]
    t_start = t.perf_counter()
    bin_pretraga(L, n)
    t_najnep = t.perf_counter() - t_start
    print('{:<8d}\t{:<8.6f}'.format(n, t_najnep))
