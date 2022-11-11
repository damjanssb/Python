#unos
stranice = []
while True:
    stranica = input('Unesi dužinu stranice (bez elementa za kraj). ')
    if stranica == '':
        break
    stranice.append(float(stranica))
stranice.sort()
x = float(input(' Unesi dolju granicu x. '))
y = float(input('Unesi gornju granicu y. '))

#pravljenje svih kombinacije klase 3
import itertools as it
tri_stranice = it.combinations(stranice, 3)

#izdvajanje odgovarajučih trouglova
trouglovi = []
for b in tri_stranice:
    if b[0] + b[1] > b[2]:
        s = (b[0] + b[1] + b[2])/2
        p = (s*(s-b[0])*(s-b[1])*(s-b[2]))**0.5
        if  x < p and p < y:
            trouglovi.append((b, p))

#test
for t in trouglovi:
    print(t)
