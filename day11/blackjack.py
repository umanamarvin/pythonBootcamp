import random
from take_card import player_takes_card
from take_card import choosing_for_pc
from take_card import choosing_for_player
from take_card import greater_than_21
from take_card import say_hello
import os

other_game = True

while other_game == True:

    # warm welcome
    say_hello()


    # list with cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # variables to use
    computer = []
    computer_total = 0 
    player = []
    player_total = 0

    # Choosing cards fot computer
    computer, computer_total = choosing_for_pc()

    # Choosing cards for player
    player, player_total = choosing_for_player()

    # player taking more cards           
    player, player_total = player_takes_card(player, player_total)

        
    # the player's total is greater than 21
    if player_total >= 22:
        while 11 in player:
            player, player_total = greater_than_21(player, player_total)
        # player taking more cards 
              

    # if computer less than 
    while not computer_total > 13 and player_total < 21:

        if computer_total < 13:
            print ("\nComputer total was less than 13, computer takes other card")
            computer += [random.choice(cards)]
            computer_total = 0
            for item in computer:
                computer_total += item
            print (f"Computer: {computer} = {computer_total}")

    # showing the results of the game

    print ("\nResults:")
    print (f"Computer: {computer} = {computer_total}")   
    print (f"Player: {player} = {player_total}")

    # deciding who is the winner

    if player_total == computer_total:
        print ("Game is a draw!")
    elif player_total > computer_total and not player_total > 21 or computer_total > 21:
        print ("Player wins!")
    else:
        print ("Computer wins!")
        
    if input ("Do you want to play again? y or n: ") == "n":
        other_game = False
        
    os.system('cls')
    
    
input ("\nThanks for playing, press the enter key to exit.")


        
