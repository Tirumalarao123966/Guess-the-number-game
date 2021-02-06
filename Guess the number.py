import random

number = random.randrange(1,50)
guess = int(input("Guess a number between 1 and 50: "))

while guess != number:
    if guess < number:
        print("you need to guess higher. Try again")
        guess = int(input("\nGuess a number between 1 and 50: "))
    else:
        print("you need to guess lower. Try again")
        guess = int(input("\nGuess a number between 1 and 50: "))

print("you guessed the number correctly")        
