# kreira listu prostih brojeva do unete vrednosti n

n=int(input('Unesu granicnu vrednost. '))
prosti=[2]

for i in range(3,n+1,2):
    kontrola=True
    for j in range (2,i//2):
        if i%j==0:
            kontrola=False
    if kontrola:
        prosti.append(i)

print('Prosti brojevi do n su:', prosti)

#II nacin
print('\nII nacin (koristeci sito)')

def eratosten(n):
    '''Generise listu prostih brojeva do n.'''
    prosti=[]
    sito=[False, False]+(n-1)*[True]

    for i in range(2,int(n**0.5)+2):
        if sito[i]:
            for j in range (i*2,n+1,i):
                sito[j]=False

    for i in range(2,n+1):
        if sito[i]:
            prosti.append(i)
    return prosti

n=int(input('Unesu granicnu vrednost. '))
print('Prosti brojevi do n su:', prosti)
