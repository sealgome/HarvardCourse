import random

guessrandomnumber = random.randint(1,25)



for _ in range(5):

    user_input = int(input("Insert your guess between 1 and 25: "))

    if user_input > guessrandomnumber:
        print("Your number is to high, try again")
    elif user_input < guessrandomnumber:
        print("Your number is too low, try again")
    else:
        print("Congratulations, you guessed the number!")
        break
