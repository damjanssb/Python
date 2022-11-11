import površine_4_2

while True:
    slika= int(input('Unesi: 1 za paralelogram, 2 za trapez, 3 za krug. '))
    if slika==površine_4_2.paralelogram:
        a=float(input('a='))
        h=float(input('h='))
        print('P =', površine_4_2.p_paralelogram(a,h))
    elif slika==površine_4_2.trapez:
        a=float(input('a='))
        b=float(input('b='))
        h=float(input('h='))
        print('P =', površine_4_2.p_trapez(a,b,h))
    elif slika==površine_4_2.krug:
        r=float(input('r='))
        print('P =', površine_4_2.p_krug(r))
    else:
        break
