import words as w

def put_letter(letter, hidden_word, word):
    
    start = 0
    
    for j in range(word.count(letter)):
        index = word.find(letter, start)
        hidden_word[index] = letter
        start = index + 1

    return hidden_word

def play():
    
    word = w.word().upper()
    hidden_word = ['-' for i in range(len(word))]
    lives = 6
    used_letters = []
    print('\nLet\'s play. You need to guess hidden word.\n', ' '.join(hidden_word))

    while True:
        
        letter = input('\nGuess a letter: ').upper()

        if letter in used_letters:
            print('Letter is already used. Try again.')
            continue
        
        used_letters.append(letter)
        
        if letter in word:
            print(f'Letter {letter} is in the word.')
            hidden_word = put_letter(letter, hidden_word, word)

            if '-' not in hidden_word:
                print(f'\nWell done dude. U hit the word {word}.')
                break
        
        else:
            lives -= 1
            print(f'Letter {letter} is not in the word.')

            if lives == 0:
                print(f'\nHaha. U R loser. The word was {word}.')
                break
        
        print(f'You have {lives} lives left.')
        print('You have used these letters: ', ' '.join(used_letters))
        print(' '.join(hidden_word))

# test program    
if __name__ == '__main__':
    again = 'Y'
    while again == 'Y':
        play()
        again = input('\nDo you whana play again. Y for yes, N for no: ').upper()
        
