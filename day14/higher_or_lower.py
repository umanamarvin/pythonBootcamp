from functions import show_logo
from functions import show_vs 
# from functions import pick_one_random
from functions import pick_random
from functions import show_score
from functions import show_person1
from functions import show_person2
from functions import make_choice
import os

def compare(selected_person, no_selected_person, score):
    if selected_person['follower_count'] > no_selected_person['follower_count']:
        score += 1
        print (f"You are right! Current score {score}")
        return selected_person, score
    else:
        print (f"Sorry you're wrong. Final score {score}.")
        return {
        'name': 'x',
        'follower_count': 0,
        'description': 'x',
        'country': 'x'
    }, score

person_a = {}
person_b = {}
score = 0
selected_person = {}
no_selected_person = {}
continue_playing = True

    
person_a = pick_random()
person_b = pick_random()

show_logo()
show_score(score)

show_person1(person_a)
show_vs()
show_person2(person_b)

selected_person, no_selected_person = make_choice(person_a, person_b)

right_person, score = compare(selected_person, no_selected_person, score)

# print (right_person)
# print (score)
input ("Press enter key to continue>")
os.system('cls')

while continue_playing:
    
    if right_person == {
            'name': 'x',
            'follower_count': 0,
            'description': 'x',
            'country': 'x'
        }:
        
        continue_playing = False
    else:
        person_a = right_person
        person_b = pick_random() 

        # print (person_a)
        # print (person_b)

        show_logo()
        print (f"Current score {score}")

        show_person1(person_a)
        show_vs()
        show_person2(person_b)
                    
        selected_person, no_selected_person = make_choice(person_a, person_b)

        right_person, score = compare(selected_person, no_selected_person, score)

        input ("Press enter key to continue>")

        os.system('cls')
        
os.system('cls')
show_logo()   
print (f"Final score {score}.")
input ("Thanks for playing, press the enter key to exit.")
os.system('cls')