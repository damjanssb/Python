# Generiše lozinku ne kraću od 8 karaktera, među kojima su mala, velika slova i brojevi
import random as r

mala_slova = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
              'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
              's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
velika_slova = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
brojevi = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

odabir = list(r.choice(mala_slova))
odabir.append(r.choice(velika_slova))
odabir.append(r.choice(brojevi))
svi_karakteri = mala_slova + velika_slova + brojevi

for k in odabir:
    svi_karakteri.remove(k)

n = int(input('Unesi dužinu lozinke. '))
odabir = odabir + r.sample(svi_karakteri, n-3)
r.shuffle(odabir)

lozinka = ''.join(odabir)
print('Vaša lozinka je:', lozinka)
