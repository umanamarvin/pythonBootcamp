import random
from game_data import data
from art import logo
from art import vs

# function to print logo
def show_logo():
    print (logo)
    
# function to print vs
def show_vs():
    print (vs)
    
# show the score
def show_score(punts):
    print (f"Current score: {punts}")

# function to assing characters

def pick_random():
    random_number1 = random.randint(0,49)
    person1 = data[random_number1]   
    return (person1)


    
def show_person1(person1):
    print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}")

def show_person2(person2):
    print(f"Compare B: {person2['name']}, a {person2['description']}, from {person2['country']}")


def make_choice(a, b):
    choice_input = ""
    while not choice_input == "a" or not choice_input == "b":
        choice_input = (input ("Who has more followers? Type 'A' or 'B' ")).lower()
        #print (choice_input)
        if choice_input == "a":
            return a,b
        elif choice_input == "b":
            return b,a
        else:
            print ("Please input a correct selection 'A' or 'B'")
        
def compare_followers(a,b):
    if a['follower_count'] > b['follower_count']:
        return a
    else:
        return b
