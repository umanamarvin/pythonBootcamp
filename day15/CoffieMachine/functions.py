def check_resources_and_price(choice, resources, coins):
    to_check = choice
    ingredients = to_check["ingredients"]
    cost = to_check["cost"]

    if resources["water"] < ingredients["water"]:
        return "Sorry there is not enough water. Money refunded"
    elif resources["milk"] < ingredients["milk"]:
        return "Sorry there is not enough milk. Money refunded"
    elif resources["coffee"] < ingredients["coffee"]:
        return "Sorry there is not enough coffee. Money refunded"
    elif coins < cost:
        return "Sorry not enough money. Money refunded"
    return to_check["cost"]


def insert_coins():
    print("Please insert coins")
    quarters = 0.25 * int(input("How many quarters? "))
    dimes = 0.10 * int(input("How many dimes? "))
    nickles = 0.05 * int(input("How many nickles? "))
    pennies = 0.01 * int(input("How many pennies? "))

    inserted_coins = quarters + dimes + nickles + pennies
    inserted_coins.__round__(2)
    return inserted_coins
