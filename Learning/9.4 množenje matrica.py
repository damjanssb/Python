# Učitava matrice A i B iz CSV datoteke, računa C=AxB 
# i rešenje ispisuje u novoj CSV datoteci
# adresa A: 'D:\\Programi\\New folder\\Python\\A.csv'
# adresa B: 'D:\\Programi\\New folder\\Python\\B.csv'
# adresa C: 'D:\\Programi\\New folder\\Python\\C.csv'

import csv

def učitaj_matricu(put):
    try:
        with open(put) as m:
            M = list(csv.reader(m, delimiter = ';'))
        return M
    except:
        raise Exception('Problem sa učitavanjem ' + put)
        
def zapiši_matricu(put, M):
    try:
        with open(put, 'w', newline = '') as m:
            csv.writer(m, delimiter = ';').writerows(M)
    except:
        raise Exception('Problem pri upisu ' + put)

def množenje_matrica(A, B):
    m, kb = len(A), len(B)
    if m == 0 or kb == 0:
        raise Exception('Matrice moraju da imaju barem po jedan element.')

    ka, n = len(A[0]), len(B[0])
    if ka != kb:
        raise Exception('Matrice nisu saglasne.')

    try:
        C = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                for k in range(kb):
                    C[i][j] += float(A[i][k])*float(B[k][j])
        return C
    except:
        raise Exception('Problem pri množenu matrica.')
        
#test
try:
    putanja = input('Adresa matrice A? ')
    A = učitaj_matricu(putanja)
    putanja = input('Adresa matrice B? ')
    B = učitaj_matricu(putanja)
    putanja = input('Adresa matrice C? ')
    C = množenje_matrica(A, B)
    zapiši_matricu(putanja, C)
    print('Uspešno je obavljeno množenje matrica i upisivanje rezultata.')
except Exception as e:
    print(e)
