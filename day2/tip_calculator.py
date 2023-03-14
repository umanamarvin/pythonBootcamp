print ("Welcome to the tip calculator.\n")
bill = float(input("What was the total bill? "))
tip = float(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

split = ((bill * (1 + (tip/100))))/people
split = round (split, 2)

print (f"\nEach people should pay: ${split}\n")

input("Press the enter key to exit")



