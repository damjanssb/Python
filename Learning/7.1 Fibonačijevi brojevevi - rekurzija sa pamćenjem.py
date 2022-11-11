import time

def fibonači(n):
    '''Izračunava vrednost Fibonačijevog broja za n>=0'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonači(n-1) + fibonači(n-2)
    
memorija = {}
def fibonači_memo(n):
    '''Izračunava vrednost Fibonačijevog broja za n>=0'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in memorija:
        return memorija[n]
    else:
        memorija[n] = fibonači(n-1) + fibonači(n-2)
        return memorija[n]

n = int(input('Unesi n. '))

start = time.perf_counter()
fib = fibonači(n)
t1 = time.perf_counter() - start
print('F({})={}\tVreme bez memorije je {}'.format(n, fib, t1))

start = time.perf_counter()
fib = fibonači_memo(n)
t2 = time.perf_counter() - start
print('F({})={}\tVreme sa memorijom je {}'.format(n, fib, t2))

print('Postupak sa memorijom je brži {} puta.'.format(t1/t2))
