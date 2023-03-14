from menu_dictionary import MENU
from menu_dictionary import VALID_SELECTIONS
from menu_dictionary import resources

# TODO: 1 - Prompt user by asking “What would you like? (espresso/latte/cappuccino):"


def greeting():
    select = ""
    while select not in VALID_SELECTIONS:
        select = input("\nWhat would you like? (espresso/latte/cappuccino):")
        if select not in VALID_SELECTIONS:
            print("\nPlease input one of the three available options")
    return select


# TODO: 2 - Turn off the Coffee Machine by entering “off” to the prompt.


def turn_off(choosing):
    if choosing == "turn off":
        return False
    else:
        return True

# TODO: 3 - When the user enters “report”, a report should be generated that shows the current resource values


def report(choosing, current_resources):
    if choosing == "report":
        print(f"Water: {current_resources['water']} ml")
        print(f"Milk: {current_resources['milk']} ml")
        print(f"Coffe: {current_resources['coffee']} gr")


# TODO: 4 - Check resources sufficient?


def check_resources(real_resources, to_use_resources):

    if real_resources["water"] < to_use_resources["water"]:
        print("There is not enough water.")
        return False
    elif real_resources["milk"] < to_use_resources["milk"]:
        print("There is not enough milk.")
        return False
    elif real_resources["coffee"] < to_use_resources["coffee"]:
        print("There is not enough coffee.")
        return False
    else:
        return True


# TODO: 5 - Process coins. If sufficient resources then the program should prompt the user to insert coins


def payment(price):
    print(f"The cost of your selection is {price}")
    quarters = int(input("how many quarters do you want to insert? "))
    dimes = int(input("How many dimes do you want to insert? "))
    inserted_money = (quarters * 0.25) + (dimes * 0.10)

    # TODO: 6 - Check transaction successful?

    if inserted_money >= price:
        return True, inserted_money
    else:
        print("Sorry that's not enough money, Money refunded.")
        return False, inserted_money

# TODO: 8 - Update the resources afther making a coffee


def update_resources(real_resources, to_use_resources):
    u_water = real_resources["water"] - to_use_resources["water"]
    u_milk = real_resources["milk"] - to_use_resources["milk"]
    u_coffee = real_resources["coffee"] - to_use_resources["coffee"]
    updated_resources = {'water': u_water, 'milk': u_milk, 'coffee': u_coffee}
    return updated_resources


# ---------------------MAIN area----------------------


power = True
actual_resources = resources

while power:
    choose = greeting()
    report(choose, actual_resources)
    power = turn_off(choose)

    if choose in MENU:
        selection = MENU[choose]
        needed_resources = selection["ingredients"]
        cost = selection["cost"]
        check_sufficient = check_resources(actual_resources, needed_resources)

        if check_sufficient:
            payment_ok, change = payment(cost)

            # TODO: 7 - Make Coffee. If transaction OK and resources OK then make the selected coffee

            if payment_ok:
                actual_resources = update_resources(actual_resources, needed_resources)
                print(f"Here is your {choose}. Enjoy!")
                if change > cost:
                    change = change - cost
                    print(f"Change ${round(change, 2)}")