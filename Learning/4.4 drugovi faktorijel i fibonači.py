#izračunava faktorijel i fibonačijev broj za uneto n
#poziva rekurzivne funkcije iz modula rekurzija.py

import rekurzija_4_4 as rekurzija

n=int(input('Unesi vrednost n. '))
print('\nZa unetu vrednost', n, 'faktorijel je', rekurzija.faktorijel(n),
      'a fibonačijev broj je', rekurzija.fibonaci(n), '.')

fak=rekurzija.faktorijel
fib=rekurzija.fibonaci

print('\nFaktorijel (od 0 do 10):')
for i in range(0,11):
    print(fak(i), end=' ')

print('\n\nFibonači (od 0 do 10):')
for i in range(0,11):
    print(fib(i), end=' ')    
