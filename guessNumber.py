import random 
# Pick a random number
random_number = random.randint(1,10)

#Input from the user
user_guess = int(input("Insert your guess number: "))

if random_number == user_guess:
    print("Well done. Your number was correct!")
else:
    print("Sorry, you didnt guess the number")

