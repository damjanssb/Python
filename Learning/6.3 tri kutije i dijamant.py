# Izračunava površinu kruga ne koristeći pi,
# nego raguna po principu verovatnoće
# da se neka tačka iz kvadrata (-r,r)x(-r,r)
# nađe unutar kružnice x**2+y**2=r**2

import random as ran

def površina(r, n):
    '''Proverava da li slučajno izabrana tačka (x,y)
    ispunjava uslov jednačine kruga x**2+y**2<=r**2'''
    krug = 0
    for i in range (n):
        x, y = ran.uniform(-r, r), ran.uniform(-r, r)
        if x**2 + y**2 <= r**2:
            krug += 1
    return (krug/n)*((2*r)**2)

n = int(input('Unesi broj uzorka. '))
r = float(input('Unesi poluprečnik kruga. '))
p_kruga = površina(r, n)
print('Površina kruga je', p_kruga)

#print('{:<9}\t{:<9}'.format('n', 'Površina'))
#for i in range(7):
#    n = 10**i
#    print('{:<9}\t{:<9}'.format(n, površina(r, n)))
