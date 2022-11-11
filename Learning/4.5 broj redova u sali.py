#Koliko ima redova u sali, prvi red je najdalje od bine

def brojac(n):
    '''n: nepoznati broj tekućeg reda, vraća broj tekućeg reda.'''
    if n==1:
        return 1
    else:
        return brojac(n-1)+1

nepoznat_broj_redova=int(input('Unesi stvaran broj redova. '))
odgovor=brojac(nepoznat_broj_redova)
print('Sala ima', nepoznat_broj_redova, 'redova.')
print('Algoritam je prebrojao', odgovor, 'redova.')
