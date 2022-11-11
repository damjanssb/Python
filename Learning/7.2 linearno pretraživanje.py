# Linearno pretraživanje
import random as r
import time as t

def lin_pretraga(L, x):
    i, n = 0, len(L)
    while i < n and L[i] != x:
        i += 1
    if i < n:
        return i
    else:
        return None

#testiranje
print('{:6}\t{:8}\t{:8}\t{:8}'.
      format('n', 'Tnnep', 'Tpros', 'Tnpov'))
for i in range(1, 8):
    n = 1000 * i
    L = [k for k in range(n)]

    #najnepovoljniji slučaj
    t_start = t.perf_counter()
    lin_pretraga(L, n)
    t_najnep = t.perf_counter() - t_start

    #najpovoljniji slučaj
    t_start = t.perf_counter()
    lin_pretraga(L, 0)
    t_najpov = t.perf_counter() - t_start

    #prosečan slučaj
    t_pros = 0
    for j in range (100):
        r.shuffle(L)
        t_start = t.perf_counter()
        lin_pretraga(L, 1)
        t_pros += t.perf_counter() - t_start

    print('{:<6}\t{:<8.6f}\t{:<8.6f}\t{:<8.6f}'.
          format(n, t_najnep, t_pros/100, t_najpov))
