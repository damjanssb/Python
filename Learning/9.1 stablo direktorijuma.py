#stablo direktorijuma
import os
import os.path as osp
import time as t

def datoteke(ul_dir, dubina = 0):
    '''Izlistava datoteke, njihovu veličinu i vreme kreiranja
        u i ispod navedenog direktorijuma.'''
    os.chdir(ul_dir)
    print('+{}'.format('---'*dubina), ul_dir)
    for e in os.listdir(ul_dir):
        if osp.isfile(e):
            print('+{} {:40}|{:12} bytes | {:25}'.format('---'*(dubina + 1),
                e, osp.getsize(e), t.asctime(t.localtime(osp.getctime(e)))))
    for e in os.listdir(ul_dir):
        if osp.isdir(e):
            datoteke(osp.join(ul_dir, e), dubina + 1)
            os.chdir(ul_dir)

#test: klijent funkcije datoteke
# Adresa za unos: D:\\Damjan\\Igre\\Instalacije
putanja = input('Unesi apsolutnu putanju: ')
print('{:42}|{:18}|{:25}'.format('Ime datoteke / adresa direktorijuma',
                                 'Veličina datoteke', 'Vreme kreiranja'))
if osp.exists(putanja) and osp.isdir(putanja):
    datoteke(putanja)
else:
    print('Greška prilikom unosa.')
