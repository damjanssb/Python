# Prikuplja podatke o pogodcima za svakog strelca pojedinačno u togu takmičenja

strelci={}

def pogoci(ime_strelca, broj_kruga):
    '''Sortira pogotke strelaca u zajednički rečnik.'''
    global strelci
    if ime_strelca in strelci:
        strelci[ime_strelca] = strelci[ime_strelca]+[broj_kruga]
    else:
        strelci[ime_strelca] = [broj_kruga]

# Unos pogodaka    
while True:
    ime = input('Unesi ime strelca  (0 za kraj): ')
    if ime=='0':
        break
    krug = int(input('Unesi vrednost pogođenog kruga: '))
    pogoci(ime,krug)

# Daje krajnje rezultate
#svi_pogodci = tuple()
#for k in strelci:
#    print(k, 'je pogodio', strelci[k])
#    svi_pogodci = svi_pogodci + tuple(strelci[k])

#for k in svi_pogodci:
#    print('Krug vrednosi', k, 'pogođen je', svi_pogodci.count(k),'puta.')

# Daje krajnje rezultate
svi_pogoci = {}
for k in strelci:
    print(k, 'je pogodio', strelci[k])
    for i in range(len(strelci[k])):
        if strelci[k][i] in svi_pogoci:
            svi_pogoci[strelci[k][i]] = svi_pogoci[strelci[k][i]] + 1
        else:
            svi_pogoci[strelci[k][i]] = 1

for j in svi_pogoci:
    print('Krug vrednosi', j, 'pogođen je', svi_pogoci[j])
print(svi_pogoci)
''' k je strelac (ime)
    strelci[k] su pogodci strelca k (lista)
    i je pogodak strelca k (broj, krug)
    strelci[k][i] je i-ti pogodak strelca k
'''
