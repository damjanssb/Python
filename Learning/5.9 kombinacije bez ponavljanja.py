#kombinacije bez ponavljanja treće klase za elemente liste

boje = ['crvena', 'plava', 'zelena', 'braon']
k = int(input('Unesi klasu kombinacije: '))
n = len(boje)
sito = []
sito1 = []
kombinacija = []
kombinacije =[]

for i in range(2**n):
    bin_broj_i=''
    while i>0:
        bin_broj_i=str(i%2)+bin_broj_i
        i=i//2
    while len(bin_broj_i)<n:
        bin_broj_i='0'+bin_broj_i
    sito.append(bin_broj_i)

for j in sito:
    if j.count('1')!=k:
        sito.remove(j)
print(sito)
'''for j in sito:
    if j.count('1')==k:
        sito1.append(j)

for e in sito1:
    for i in range(n):
        if e[i]=='1':
            kombinacija.append(boje[i])
    kombinacije.append(kombinacija)
    print(kombinacija)
    kombinacija = []'''
