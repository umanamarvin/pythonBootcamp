from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()

# TODO: 2 Turn off the Coffe Machine by entering "off" to the prompt

machine_on = True
while machine_on:

    # TODO: 1 Prompt user by asking "What would you like?"
    items = menu.get_items()
    selection = input(f"What would you like? {items} ")

    if selection == "off":
        machine_on = False
    # TODO: 3 print report by entering "report" to the prompt
    elif selection == "report":
        money_machine.report()
        coffe_maker.report()
    elif selection in items:
        # TODO: 4 Check resources sufficient if there is not enought print "Sorry there is not enough X"
        drink = menu.find_drink(selection)
        sufficient_resource = coffe_maker.is_resource_sufficient(drink)
        if sufficient_resource:
            # TODO: 5 process coins
            # TODO: 6 check transaction successful?
            # TODO: 7 Make coffee and give the change
            price = drink.cost
            money_machine.make_payment(price)
            coffe_maker.make_coffee(drink)







