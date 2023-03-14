from art import logo
from art import vs
from game_data import data
import random
import os

def pick_random():
    random_number = random.randint(0, 49)
    #print (random_number)
    return data[random_number]

def compare(a, b):
    followers_a = a['follower_count']
    followers_b = b['follower_count']

    if followers_a > followers_b:
        return a
    else:
        return b
    
def make_choice(a, b):
    choice_input = ""
    while not choice_input == "a" or not choice_input == "b":
        choice_input = (input ("Who has more followers? Type 'A' or 'B' ")).lower()
        #print (choice_input)
        if choice_input == "a":
            return a
        elif choice_input == "b":
            return b
        else:
            print ("Please input a correct selection 'A' or 'B'")

game_should_continue = True
score = 0
person2 = pick_random()

while game_should_continue:

    person1 = person2
    person2 = pick_random()
    
    more_followers = compare(person1, person2)
   
    print (logo)
    print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}")
    print (vs)
    print(f"Compare B: {person2['name']}, a {person2['description']}, from {person2['country']}")

    choice = make_choice(person1, person2)
    print (f"You choose {choice['name']}")

    if choice == more_followers:
        score += 1
        os.system('cls')
        print (f"You're right! Score is {score}")
        
    else:
        print (logo)
        os.system('cls')
        print (f"You are wrong, your final score is: {score}.")
        game_should_continue = False
    
print ("Thanks for playing.")        


