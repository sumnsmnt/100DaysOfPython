########## COFFEE MACHINE ##########
# All the steps are described in the notes

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "cost": 150,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 200,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


revenue = 0

def is_resources_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_money():
    """Calculate the the total money paid by the user."""
    print("Please pay the bill.")
    total = int(input("How many notes of Rs.10? ")) * 10
    total += int(input("How many notes of Rs.20? ")) * 20
    total += int(input("How many notes of Rs.50? ")) * 50
    total += int(input("How many notes of Rs.100? ")) * 100
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is Rs.{change} in change.")
        global revenue
        revenue += drink_cost
        return True
    else:
        print("Sorry that's not enough money, money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}.")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gm")
        print(f"Total Revenue: {revenue}rs")
    else:
        drink = menu[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_money()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])