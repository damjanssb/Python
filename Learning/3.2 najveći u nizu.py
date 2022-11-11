# I način
#unos=float(input("Unesi vrednost niza (ili inf za kraj unosa). "))
#najveci=unos
    
#while unos!=float('inf'):
#    if unos>najveci:
#        najveci=unos
#    unos=float(input("Unesi sledeću vrednost niza (ili inf za kraj unosa). "))

#print("Najveći broj koji si uneo je", najveci)

# II način
najveci=-float('inf')
    
while 1:
    unos=float(input("Unesi vrednost niza (ili inf za kraj unosa). "))
    if unos==float('inf'):
        break
    elif unos>najveci:
        najveci=unos
if najveci==-float('inf'):
    print('Nisi uneo ni jednu vrednost.')
else:
    print("Najveći broj koji si uneo je", najveci)
