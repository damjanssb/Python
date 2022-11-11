#linijska grafika

#kreiranje funkcije za crtanje pravougaonika
def pravougaonik(a, b, k, sim):
    '''Crta pravougaonik dimenzija axb,
    počevši od k-te kolone, koristeći simbol sim'''
    for i in range(a):
        print((k-1)*' ', end='')
        print(b*sim)

#testiranje funkcije crtanjem čiča Gliše iz "vežbe" 4-1
pravougaonik(2,3,10,'*') #glava
pravougaonik(4,7,8,'|') #trup
pravougaonik(4,3,10,'+') #noge

#kreiranje funkcije za crtanje fiksnog čiča Gliše
def glisa():
    '''Crta glišu fiksnih dimenzija'''
    pravougaonik(2,3,10,'*') #glava
    pravougaonik(4,7,8,'|') #trup
    pravougaonik(4,3,10,'+') #noge

print('') #razmak
glisa() #pozivanje funkcije za crtanje čiča Gliše
