import time

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
memorija = {}
def fib_memo(n):
    if n == 0 or n == 1:
        return 1
    elif n in memorija:
        return memorija[n]
    else:
        memorija[n] = fib(n-1) + fib(n-2)
        return memorija[n]

n = int(input('Unesi n. '))

start = time.perf_counter()
f = fib(n)
t1 = time.perf_counter() - start
print('F({})={} za {:6.3e}'.format(n, f, t1))

start = time.perf_counter()
f = fib_memo(n)
t2 = time.perf_counter() - start
print('F({})={} za {:6.3e}'.format(n, f, t2))

print('Postupak sa memorijom je brži {:6.3f} puta.'.format(t1/t2))
