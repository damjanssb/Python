#I način
#n=int(input('Unesi neparan broj.'))

#if n%2==0:
#    print('Uneta vrednost mora biti neparan broj.')
#else:
#    sredina=int((n+1)/2)
#    zvezdice=-1

#    for i in range(1,sredina+1):
#        zvezdice+=2
#        for j in range(n-zvezdice):
#            print(' ', end='')
#        for j in range(zvezdice):
#            print('*', end='')
#        print('')

#    for i in range(1,sredina):
#        zvezdice-=2
#        for j in range(zvezdice):
#            print('*', end='')
#        for j in range(n-zvezdice):
#            print(' ', end='')
#        print('')

#II način
n=int(input('Unesi neparan broj.'))

if n%2==0:
    print('Uneta vrednost mora biti neparan broj.')
else:
    sredina=int((n+1)/2)
    zvezdice=-1
    

    for i in range(1,sredina+1):
        zvezdice+=2
        razmak=n-zvezdice
        print(razmak*' ', end='')
        print(zvezdice*'*')

    for i in range(1,sredina):
        zvezdice-=2
        razmak=n-zvezdice
        print(zvezdice*'*', end='')
        print(razmak*' ')
