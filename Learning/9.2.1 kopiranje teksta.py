# kopira tekst datoteke uz adekvatnu obradu mogućih izuzetaka

def kopija(ulaz, izlaz, kodiranje = 'UTF-8'):
    '''Kopira tekst iz ulazne datoteke u izlaznu datoteku
        koristeći Unicode standard zadat opcionim argumentom kodiranje'''
    try:
        with open(ulaz, encoding = kodiranje) as in_put, \
             open(izlaz, 'w', encoding = kodiranje) as out_put:
            out_put.write(in_put.read())
            print('Uspešno je kopirano.')
        
    except FileNotFoundError:
        print('Pogrešna putanja.')
    except UnicodeDecodeError:
        print('Pogrešno kodiranje.')
    except:
        print('Greška pri kopiranju.')

# test: korisnik funkcije kopija
# kopiranje: 'D:\\Programi\\New folder\\Python\\AgonijaSrpski.txt'
#    kopija: 'D:\\Programi\\New folder\\Python\\AgonijaSrpski_kopi.txt'
ulaz = input('adresa kopirane datoteke: ')
izlaz = input('adresa  kopije  datoteke: ')
kodiranje = input('standard kodiranja (ništa za UTF-8): ')
if kodiranje == '':
    kopija(ulaz, izlaz)
else:
    kopija(ulaz, izlaz, kodiranje)
