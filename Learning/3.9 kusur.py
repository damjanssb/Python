#vraća kusur sa najmanje novčanica
#u knjizi i u završnom radu postoje drugačija rešenja

#unos vrednosti a, b, c, n
n=int(input('Koliko je novca dao kupac? '))
a=int(input('Vrednost 1. novčanice. '))
b=int(input('Vrednost 2. novčanice. '))
c=int(input('Vrednost 3. novčanice. '))

#sortiranje da bude a>b>c
if b>a:
    a,b=b,a
if c>b:
    b,c=c,b
if b>a:
    a,b=b,a

#obračunavanje kusura
kusur=n-1000
print('Ukupan kusur je', kusur, 'dinara.')
ak,bk,ck=0,0,0
while kusur>=a:
    ak+=1
    kusur=kusur-a
while kusur>=b:
    bk+=1
    kusur=kusur-b
while kusur>=c:
    ck+=1
    kusur=kusur-c
print('Treba vratiti:')
print(ak, 'novčanica od', a, 'dinara')
print(bk, 'novčanica od', b, 'dinara')
print(ck, 'novčanica od', c, 'dinara')
if kusur>0:
    print('Preostalih', kusur, 'dinara ti ne mogu vratiti.')
