# The Secret Auction Program

import os 

auctions = {}
other_bid = True
bid1 = 0
bid2 = 0
bid_winner = 0

while other_bid == True:
    name = input ("What is your name? ")
    bid = int(input ("What's your bid? "))
    
    auctions[name] = bid
    
    more = input ("If there is not other bidder type 'not' ")
    if more == "not":
        other_bid = False
    
    os.system('cls')
    
print (auctions)

max_bid = (max(auctions.values()))

for key in auctions:
    if auctions[key] == max_bid:
        bid_winner = key
        
print (f"The max bid was {max_bid}, {bid_winner} is the winner.")

input ("Press the enter key to exit")