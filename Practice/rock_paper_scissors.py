import random as r

def play(player):
    global l, d, w
    computer = r.choice(['r', 'p' , 's'])

    if computer == user:
        d += 1
        return f'It\'s drawn. Both choices are {user.upper()}.'
    elif (player == 'p' and computer == 'r') or (player == 'r' and computer == 's')\
       or (player == 's' and computer == 'p'):
        w += 1
        return f'Yay, U win. Comuter chose {computer.upper()}.'
    else:
        l += 1
        return f'Haha, U lose. Comuter chose {computer.upper()}.'

# test program
print('Press ENTER without letter for end the game.')
l, d, w = 0, 0, 0

while True:
    user = input('\nChoice one of rock (R), paper (P), scissors (S): ').lower()
    if user == '':
        break
    elif user not in ('r', 'p', 's'):
        print ('U must input R, P or S.')
    else:
        print(play(user))

print(f'U win {w} time, lose {l} time and {d} time it wase drawn.')
