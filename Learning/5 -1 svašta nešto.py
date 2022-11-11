# poruka za dešifrovanje ïÕËÕÝáCéÍCËÅβÅéCíCm

poruka=input('Unesi poruku koju želiš da šifruješ. \n')
a=int(input('Unesi koeficijent a. '))
b=int(input('Unesi koeficijent b. '))
sifruj=input('Unesi slovo š za šifrovanje ili d za dešifrovanje. ')
poruka1=poruka
if sifruj=='š':
    for i in range(len(poruka)):
        poruka1[i]=chr(a*ord(poruka[i])+b)
    print('Šifrovana poruka glasi: \n', poruka1)
elif sifruj=='d':
    for i in range(len(poruka)):
        poruka1[i]=chr((ord(poruka[i])-b)//a)
    print('Dešifrovana poruka glasi: \n', poruka1)
else:
    print('Mora se uneti slovo š za šifrovanje ili d za dešifrovanje.')

#poruka=input('Unesi poruku koju želiš da šifruješ. \n')
#a=int(input('Unesi koeficijent a. '))
#b=int(input('Unesi koeficijent b. '))
#sifruj=input('Unesi slovo š za šifrovanje ili d za dešifrovanje. ')

#if sifruj=='š':
#    print('Šifrovana poruka glasi:')
#    for i in range(len(poruka)):
#        print(chr(a*ord(poruka[i])+b), end='')
#elif sifruj=='d':
#    print('Dešifrovana poruka glasi:')
#    for i in range(len(poruka)):
#        print(chr((ord(poruka[i])-b)//a), end='')
#else:
#    print('Mora se uneti slovo š za šifrovanje ili d za dešifrovanje.')
