def kazi_zdravo(ime, koliko, jezik='sr'):
    zdravo= 'Zdravo'
    if jezik=='en':
        zdravo='Hello'
    elif jezik=='it':
        zdravo='Ciao'

    for i in range(koliko):
        print(zdravo,ime)
