a=float(input('Unesi broj a. '))
n=int(input('Unesi prirodan broj n. '))
delta=float(input('Unesi preciznost do koje se raćuna koren.'))

if n<=0:
    print('n mora biti veće od nula.')
elif a<0 and n%2==0:
    print('Ne postoji realni paran koren iz negativnog broja.')
else:
    x=a/n
    while abs(x**n-a)>delta:
        x=x-((x**n-a)/(n*x**(n-1)))

print(n, end='')
print('. koren broja', a, 'je', x, end='.')
