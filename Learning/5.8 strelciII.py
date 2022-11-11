# Prikuplja podatke o pogodcima za svakog strelca pojedinačno u togu takmičenja

# Unos pogodaka
strelci, pogoci = {}, {}
while True:
    ime = input('Unesi ime strelca  (0 za kraj): ')
    if ime=='0':
        break
    krug = int(input('Unesi vrednost pogođenog kruga: '))
    strelci[ime] = strelci.get(ime, []) + [krug] #Kreira listu i popunjava je
    pogoci[krug] = pogoci.get(krug, 0) + 1 #Prebrojavanje ponavljanja

# Ispis rezultata
for k in strelci:
    print(k, 'je pogodio', strelci[k])
for j in pogoci:
    print('Krug vrednosi', j, 'je pogođen', pogoci[j], 'puta.')
