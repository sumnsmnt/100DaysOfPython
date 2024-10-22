# Program Requirements
# 1. Print Report.
# 2. Check if the resources are sufficient?
# 3. Process the Money.
# 4. Check if the transaction are successful?
# 5. Make the Coffee.

# I have added 3 modules - menu.py, coffee_maker.py & money_machine.py
# Created Menu, MenuItem, CoffeeMaker & MoneyMachine classes and 
# imported them inside this file.

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
my_menu = Menu()

is_on = True

my_money_machine.report()
my_coffee_maker.report()

while is_on:
    options = my_menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        drink = my_menu.find_drink(choice)
        if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            my_coffee_maker.make_coffee(drink)