import random
import os

# global constants
EASY = 10
HARD = 5

# Functions
def choosing_difficulty():
    choose_difficulty = ""
    while choose_difficulty != "easy" or choose_difficulty != "hard":

        choose_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if choose_difficulty == "easy":
            return EASY
        elif choose_difficulty == "hard":
            return HARD
        else:
            print("That is not a valid difficulty please choose again.")

def remaining (tries):
    print (f"You have {tries} attempts remaining.")

def play_game(number_to_guess, tries_remaining):
    guess = 0
    while guess != number_to_guess and tries_remaining > 0:
        
        guess = int (input ("Make a guess: "))
        if guess < 0 or guess > 100:
            print ("Please input a valid number between 1 and 100.")
            remaining(tries_remaining)
        elif guess > number_to_guess:
            print ("Too high.")
            tries_remaining -= 1
            remaining(tries_remaining)
        elif guess < number_to_guess:
            print ("Too low.")
            tries_remaining -= 1
            remaining(tries_remaining)
        elif guess == number_to_guess:
            return ("You guessed it! You win.")
        
    if tries_remaining == 0:
            return (f"You lose. The number was {number_to_guess}")

# GAME ON
more = True
while more == True:

    print ("Welcome to the Number Guessing Game")
    print ("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)
    #print (f"The number is {number}")

    difficulty_tries = choosing_difficulty()
    print (f"You have {difficulty_tries} attempts remaining to guess the number.")

    result = play_game(number, difficulty_tries)

    print (result)
    
    if input("Play again? y or n: ") == "n":
        more = False
    os.system ('cls')
