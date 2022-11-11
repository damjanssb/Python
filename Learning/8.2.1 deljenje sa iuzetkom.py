# simulacija serveta
# obrada izuzetka
import time as t
def deli(x, y):
    ''' #Funkcija vraća količnik x/y za validno x i y.
'''
    try:
        return int(x) / int(y)
    except ValueError:
        print('Dnevnik servera:', t.asctime(), 'greška, ValueError!')
        raise ValueError
    except ZeroDivisionError:
        print('Dnevnik servera:', t.asctime(), 'greška, ZeroDivisionError!')
        raise ZeroDivisionError
    except:
        print('Dnevnik servera:', t.asctime(), 'greška, Nepoznata greška')
        raise

# test klijent
try:
    while True:
        x, y = input('x = '), input('y = ')
        try:
            print('x / y =', deli(x, y))
        except ValueError:
            print('program: x i y moraju biti celi brojevi.')
        except ZeroDivisionError:
            print('program: y ne sme biti 0.')
        except:
            print('program: Nepoznata greška.')
except KeyboardInterrupt:
    print('Aj zdravo.')
