#za unete vrednosti n i m proverava koji od brojeva
#iz intervala [n,m] ima naduži niz nula u binarnom zapisu

n=int(input('Unesi donju granicu. '))
m=int(input('Unesi gornju granicu. '))

def naj_podniz(x):
    '''Vraća dužinu najdužeg podniza nula u binarnom zapisu broja x.'''
    d,maxd=0,0
    
    while x!=0:
        if x%2==0:
            d+=1
        elif x%2==1:
            if d>maxd:
                maxd=d
            d=0
        x//=2
        
    return maxd

if n<=m and n>0:
    max_duzina=-1
    for i in range(n,m+1):
        d=naj_podniz(i)
        if d>max_duzina:
            max_duzina=d
            resenje=i
    print('Broj', resenje, 'ima najduži podnis nula koji iznosi', max_duzina)
else:
    print('Nisi dobro uneo vrednosti.')
