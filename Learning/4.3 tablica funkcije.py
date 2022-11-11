#tablica funkcije

def tablica_funkcije(a,b,k,f):
    '''Ispisuje tablicu funkcije f(x) u intervalu [a,b] sa korakom k.'''
    if a<=b and k>0:
        x=a
        print('x || f(x)')
        while x<=b:
            print(x, '||', f(x))
            x+=k
    else:
        print('Mora biti a<b i k>0.')

import math
print('f(x)=cos(x)')
tablica_funkcije(0, 2*math.pi, math.pi/6, math.cos)
print('\nf(x)=exp(x)')
tablica_funkcije(0, 5, 0.5, math.exp)
