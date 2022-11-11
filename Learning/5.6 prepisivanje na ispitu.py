#Proverava broj poklapajućih reči u sastavima dva studenta

def sličnost(t1, t2):
    '''Vraća meru sličnosti dva teksta putem
       Jaccard-ovog indeksa slčnosti skupova reči'''
    w1 = set(t1.lower().split())
    w2 = set(t2.lower().split())
    n=len(w1|w2)
    if n==0:
        return 1.0
    else:
        return len(w1&w2)/n

def detektor_sličnosti(radovi):
    '''Vraća listu parova sortiranu na osnovu
       sličnosti tekstova u listi radova'''
    parovi=[]
    n=len(radovi)
    for i in range(n-1):
        for j in range(i+1,n):
            ri, rj=radovi[i], radovi[j]
            parovi.append((sličnost(ri[1],rj[1]),ri,rj))
    parovi.sort(reverse = True)
    return parovi

radovi=[ (1, 'Ide Mile lajkovačkom prugom'),
         (2, 'Ide Mile prugom ka svojoj supruzi'),
         (3, 'Kaži Mile supruzi šta te to muči'),
         (4, "Al' je lep ovaj svet")]

print('Mera sličnosti\tIndeks 1\tIndeks2')
for par in detektor_sličnosti(radovi):
    print('{:<14.3}\t{:^8}\t{:^8}'.format(par[0],par[1][0],par[2][0]))
