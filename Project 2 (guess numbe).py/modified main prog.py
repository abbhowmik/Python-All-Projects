import random
randNo = random.randint(1, 100)
# print(randNo)

try:
    a = input('***Press q to quit, or enter any key to start the game:  ')
    userGuess = None
    guesses = 0

    while userGuess != randNo:

        if a == 'q':
            print('Exiting the game:')
            print('Thanks for playing with us*')
            break

        userGuess = int(input('Please Enter a number : '))
        guesses += 1

        if userGuess == randNo:
            print('Wow It guessed it right ')
        elif userGuess > randNo:
            print('You guessed it wrong , Please select a **Smaller Number')
        else:
            print('You guessed it wrong , Please select a **Larger Number')

    print(f'You guessed it right in {guesses} guesses')

except Exception as e:
    print(f'Please enter a valid value,error is--> {e}')


with open('gamescore.txt') as f:
    score = int(f.read())

if guesses < score:
    print('You have just broke the high score')
    with open('gamescore.txt', 'w') as f:
        f.write(str(guesses))
