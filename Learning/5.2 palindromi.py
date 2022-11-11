# proverava da li je neki string palindrom iteracijom

def palindromI(tekst):
    for i in range(len(tekst)//2):
        if tekst[i]!=tekst[-1-i]:
            return False
    return True

def palindromR(tekst):
    if tekst=='':
        return True
    elif tekst[0]!=tekst[-1]:
        return False
    else:
        return palindromR(tekst[1:-1])

tekst=input('Unesi tekst: ')
if palindromR(tekst):
    print('rekurzijom:', tekst)
if palindromI(tekst):
    print('iteracijom:', tekst)
else:
    print('Uneti tekst nije palindrom.')
