# Klasa Razlomak kreira razlomak oblika x/y za argumente (x,y)
# Razlomci se kreiraju u nesvodljivoj formi (x i y su uzajamno prosti)
# Sadrži metode za obavljanje osnovnih operacija nad razlomcima

class Razlomak:
    '''Pretstavlja razlomak za unete argumente x i y'''

    # poziva se iz konstruktora prilikom kreiranja objekta
    # Za vrednosti x i y kreira ne svodljiv razlomak
    def __init__(self, x, y):
        try:
            x, y = int(x), int(y)
        except:
            raise Exception ('Uneti brojevi nisu celobrojni.')

        if y == 0:
            raise Exception ('Imenilac je 0.')
        else:
            if (x < 0 and y > 0) or (x > 0 and y < 0):
                x, y = -abs(x), abs(y)
            else:
                x, y = abs(x), abs(y)

        a, b = x, y 
        while b != 0:
            a, b = b, a % b
            
        self.x = x // a
        self.y = y // a
    
    # tekstuala reprezentacija razlomka
    def __str__(self):
        return '{:<d}/{:<d}'.format(self.x, self.y)

    # vraća realnu vrednost razlomka
    def vrednost(self):
        return self.x / self.y
    
    # sabira razlomak nad kojom se poziva metoda sa zadatim razlomkom
    def __add__(self, r):
        return Razlomak(self.x * r.y + r.x * self.y, self.y * r.y)
        
    # od razlomka nad kojom se poziva metoda oduzima zadat razlomak
    def __sub__(self, r):
        return Razlomak(self.x * r.y - r.x * self.y, self.y * r.y)
        
    # množi razlomak nad kojom se poziva metoda sa zadatim razlomkom
    def __mul__(self, r):
        return Razlomak(self.x * r.x, self.y * r.y)

    # razlomak nad kojom se poziva metoda deli zadatim razlomkom
    def __truediv__(self, r):
        return Razlomak(self.x * r.y, self.y * r.x)

    # proverava da li je razlomak nad kojom se poziva metoda jednaka sa zadatim
    def __eq__(self, r):
        if isinstance(r, Razlomak):
            return self.x == r.x and self.y == r.y
        return False

# test programa
if __name__ == '__main__':
    try:
        X = Razlomak(input('Unesi prvi brojilac: '),input('Unesi prvi imenilac: '))
        print('Vrednost prvog razlomka: {} = {}'.format(X, X.vrednost()))
        Y = Razlomak(input('Unesi drugi brojilac: '),input('Unesi drugi imenilac: '))
        print('Vrednost drugog razlomka: {} = {}'.format(Y, Y.vrednost()))
        print('{} + {} = {}'.format(X, Y, X + Y))
        print('{} - {} = {}'.format(X, Y, X - Y))
        print('{} * {} = {}'.format(X, Y, X * Y))
        print('{} / {} = {}'.format(X, Y, X / Y))
        if X == Y:
            print('{} = {}'.format(X,Y))
        else:
            print('{} != {}'.format(X,Y))
    except Exception as e:
        print(e)
