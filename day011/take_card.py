import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Choosing cards fot computer

def choosing_for_pc():
    computer = []
    computer_total = 0 
    computer += [random.choice(cards)]
    print (f"\nComputer = {computer} + ???")
    computer += [random.choice(cards)]
    for item in computer:
        computer_total += item
    return computer, computer_total

# Choosing cards for player
def choosing_for_player():
    player = []
    player_total = 0
    player += [random.choice(cards)]
    player += [random.choice(cards)]

    for item in player:
        player_total += item

    print (f"Player: {player} = {player_total}")
    return player, player_total


# player taking more cards

def player_takes_card(player, player_total):
    more = True
    other_card = ""
    while more == True and not player_total > 21:
        other_card = input("Do you want to take other card? y or n? ")
        if other_card == "n":
            more = False
        elif other_card == "y":
            player += [random.choice(cards)]
            player_total = 0
            for item in player:
                player_total += item
            print (f"Player: {player} = {player_total}")
    return player, player_total

# player is greater than 21

def greater_than_21(player, player_total):

    if player_total > 21:
        for position in range(len(player)):
            if player[position] == 11:
                player[position] = 1
            player_total = 0
            for item in player:
                player_total += item
        print (f"Your As becomes 1, now you have {player} = {player_total}")
    player, player_total = player_takes_card(player, player_total)
    return player, player_total
            
            
# computer is less than 17


def say_hello():
    print (''' _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/  '''
     )  
    input ("\nWelcome to the BlackJack game. Press the enter key to start.")
         