# kopira tekst datoteke uz adekvatnu obradu mogućih izuzetaka

def kopija(ulaz, izlaz, kodiranje = 'UTF-8'):
    '''Kopira tekst iz ulazne datoteke u izlaznu datoteku
        koristeći Unicode standard zadat opcionim argumentom kodiranje'''
    try:
        in_put = open(ulaz, encoding = kodiranje)
    except:
        print('Pogrešna putanja.')
        return

    try:
        out_put = open(izlaz, 'w', encoding = kodiranje)
    except:
        print('Pogrešna putanja.')
        return
        
    try:
        out_put.write(in_put.read())
        print('Uspešno je kopirano.')
    except UnicodeDecodeError:
        print('Pogrešno kodiranje.')
    except:
        print('Greška u kopiranju.')
    finally:
        in_put.close(), out_put.close()

# test: korisnik funkcije kopija
# kopiranje: 'D:\\Programi\\New folder\\Python\\Agonija.txt'
#    kopija: 'D:\\Programi\\New folder\\Python\\AgonijaSrpski_kopi.txt'
ulaz = input('adresa kopirane datoteke: ')
izlaz = input('adresa  kopije  datoteke: ')
kodiranje = input('standard kodiranja (ništa za UTF-8): ')
if kodiranje == '':
    kopija(ulaz, izlaz)
else:
    kopija(ulaz, izlaz, kodiranje)
