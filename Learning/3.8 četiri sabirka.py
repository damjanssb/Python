# Program ispisuje sve kombinacije suma od četiri sabirka koje su manje on z

s1=int(input('Unesi 1. sabirak. '))
s2=int(input('Unesi 2. sabirak. '))
s3=int(input('Unesi 3. sabirak. '))
s4=int(input('Unesi 4. sabirak. '))
z=int(input('Unesi gornju granicu (z). '))

for i1 in (0,1):
    for i2 in (0,1):
        for i3 in (0,1):
            for i4 in (0,1):
                suma=i1*s1+i2*s2+i3*s3+i4*s4
                if suma<z and (i1!=0 or i2!=0 or i3!=0 or i4!=0):
                    if i1==1:
                        print(s1,end='')
                    if i2==1:
                        if i1==1:
                            print(' + ', end='')
                        print(s2,end='')
                    if i3==1:
                        if i1==1 or i2==1:
                            print(' + ', end='')
                        print(s3,end='')
                    if i4==1:
                        if i1==1 or i2==1 or i3==1:
                            print(' + ', end='')
                        print(s4,end='')
                    print(' =', suma, '<', z)
