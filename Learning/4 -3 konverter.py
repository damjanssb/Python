#konvertuje kmu miljei obrnuto

def konvertuj(x,km):
    '''Konvertuje vrednost x iz kilometara u mulje (km = True)
    ili iz milja u kilometre (km = False)'''
    if km:
        x/=1.609344 #km>mi
    else:
        x*=1.609344 #mi>km
    return x

#testiranje funkcije
print('Konvertovanje km u mi.')
for i in range(1,6):
    print(10*i, 'km =', konvertuj(10*i,1), 'mi')

print('Konvertovanje mi u km.')
for i in range(1,6):
    print(10*i, 'mi =', konvertuj(10*i,0), 'km')
