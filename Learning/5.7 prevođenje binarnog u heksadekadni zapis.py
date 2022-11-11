# Prevodi binarni broj u heksadekadni zapis koristeći rečnik

recnik = {'0000':'0', '0001':'1', '0010':'2', '0011':'3',
          '0100':'4', '0101':'5', '0110':'6', '0111':'7',
          '1000':'8', '1001':'9', '1010':'A', '1011':'B',
          '1100':'C', '1101':'D', '1110':'E', '1111':'F'}

print("Validan unos: bin2hex('binaran_broj')")

def bin2hex(broj_b):
    '''Prebacuje binarnu vrednost unosa 'broj_b' u heksadekadni zapis.'''
    
    n = len(broj_b)
    if broj_b.count('0')+broj_b.count('1')!=n:
        return print('Dozvoljene vrednosti za unosu su: 0 i 1')
    elif n%4!=0:
        broj_b='0'*(4-n%4)+broj_b

    broj_h=''
    for i in range (0,n,4):
        broj_h = broj_h + recnik[broj_b[i:i+4]]

    return broj_h
