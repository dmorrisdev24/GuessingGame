# Derrick Morris CIS 261 Guessing Game
import random as ran

def displayHeading():
    print("Guess the Number:")    

displayHeading()

while True:
    limit = int(input("Enter the limit: "))
    def guessNumber(limit):
        random_number = ran.randint(1, limit)
        print(f"I'm thinking of a number from 1 to {limit}")
        while True:
            guess =  int(input("enter your number: "))
            if guess < random_number:
                print("Too low")
            elif guess > random_number:
                print("Too high")
            else:
                print("You guessed it")
                break
    guessNumber(limit)        
    play_again = input("Would you like to play again? (y/n): ").lower()
    if play_again != "y":
        print("Bye!")
        break
        

        
    










