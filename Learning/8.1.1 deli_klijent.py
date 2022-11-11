# test klijent: deli_klijent.py
import deli_server_8_1_1 as server

while True:
    x, y = input('x = '), input('y = ')
    status, z = server.deli(x, y)
    if status == 0:
        print('x / y =', z)
        break
    elif status == 1:
        print('y mora biti različito od 0')
    elif status == 2:
        print('x mora biti ceo broj')
    elif status == 3:
        print('y mora biti ceo broj')
