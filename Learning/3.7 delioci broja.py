# Program ispisuje sve delioce učitanog broja.
n=int(input('Unesi prirodan broj čije delioce želiš da izlistam. '))
if n<=0:
    print('Broj mora biti veći od 0.')
else:
    print('Delioci broja', n, 'su: 1',end='')
    for i in range(2,n//2+1):
            if n%i==0:
                print(',',i, end='')
    print(' i', n, end='')
    print('.')
