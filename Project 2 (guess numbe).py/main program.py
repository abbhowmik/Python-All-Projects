import random
randNumber = random.randint(1, 100)

userGuess = None
guesses = 0
while userGuess != randNumber:

    userGuess = int(input("Please Enter a number : "))
    guesses += 1
    if(userGuess == randNumber):
        print("Wow! you guess the right number")

    else:
        if userGuess > randNumber:
            print("You guessed it wrong ! Enter a smaller number")
        else:
            print("You guessed it wrong ! Enter a larger number")

print(f"You guessed the number in {guesses} guesses")
