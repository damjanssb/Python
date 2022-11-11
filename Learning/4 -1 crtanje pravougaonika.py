#crta pravougaonik dimenzija 2x3 počevši od 10

a=2
b=3
k=10

for i in range(a):
    print((k-1)*' ', end='')
    print(b*'*')

#crta ostatak čiča Gliše
#trup
a,b,k=4,7,8

for i in range(a):
    print((k-1)*' ', end='')
    print(b*'|')

#noge
a,b,k=4,3,10

for i in range(a):
    print((k-1)*' ', end='')
    print(b*'+')
