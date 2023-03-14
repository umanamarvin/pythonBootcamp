# The CoffeeMachine Program
from data import MENU
from art import logo
from art import cup
from functions import check_resources_and_price
from functions import insert_coins

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
used_resources = {}
machine_on = True

while machine_on:
    print(logo)
    choice = ""
    # loop for enter a correct choice
    while choice not in MENU:
        choice = input("What would you like? Type espresso / latte / capuccino ")
        # This will give a report of the actual resources value
        if choice == "report":
            print(resources)
        # This will refill the resources
        elif choice == "refill":
            resources = {
                "water": 300,
                "milk": 200,
                "coffee": 100,}
        # This loop is going to repeat until user input a valid option
        elif choice not in MENU:
            print("Type a correct selection.")

    # When user input 'off' machine will turn off
    if choice == "off":
        machine_on = False
        choice = {""}
    # if choice of the user is in the menu, then we take the item from the list MENU
    elif choice in MENU:
        # Choice will be the dictionary with ingredients and price
        choice = MENU[choice]
        # Here we call just the ingredients
        resources_to_use = choice["ingredients"]

    if machine_on:
        coins = insert_coins()
        result_compare = (check_resources_and_price(choice, resources, coins))
        result_compare = str(result_compare)

        # Sorry will be always present when resources or money are not enough
        if "Sorry " in result_compare:
            print(result_compare)
            coins = 0
        # If everything okay we will receive just the price of our selection
        else:
            result_compare = (float(result_compare)).__round__(2)
            change = (coins - result_compare).__round__(2)
            print("Here you have! Enjoy.")
            print(f"Your change {coins} - {result_compare} = {change}")

            used_resources["water"] = resources["water"]-resources_to_use["water"]
            used_resources["milk"] = resources["milk"]-resources_to_use["milk"]
            used_resources["coffee"] = resources["coffee"]-resources_to_use["coffee"]

            # resources will be discounted and the other items will be emptied
            resources = used_resources
            change = 0
            coins = 0
            result_compare = 0






