MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def print_report():
    """Prints report on current resources"""
    print(f"Water  : {resources['water']}ml")
    print(f"Milk   : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money  : ${resources['money']}")


def process_coins():
    """Accepts coins and returns total payment"""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)


def check_transaction(payment, beverage_type):
    """Checks if payment is sufficient and returns otherwise"""
    if MENU[beverage_type]['cost'] > payment:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        resources['money'] += MENU[beverage_type]['cost']
        change = round(payment - MENU[beverage_type]['cost'], 2)
        if change > 0:
            print(f"Here is ${change} dollars in change.")
        return True


def make_coffee(beverage_type):
    """Makes coffee and reduces existing resources"""
    resources['water'] -= MENU[beverage_type]['ingredients']['water']
    resources['milk'] -= MENU[beverage_type]['ingredients'].get('milk', 0)
    resources['coffee'] -= MENU[beverage_type]['ingredients']['coffee']
    print(f"here is your {beverage_type} ☕️. Enjoy your day.")


def check_resources(beverage_type):
    """Checks existing resources for selected beverage"""
    if MENU[beverage_type]['ingredients']['water'] > resources['water']:
        print("Sorry there is not enough water.")
    elif MENU[beverage_type]['ingredients'].get('milk', 0) > resources['milk']:
        print("Sorry there is not enough milk.")
    elif MENU[beverage_type]['ingredients']['coffee'] > resources['coffee']:
        print("Sorry there is not enough coffee.")
    else:
        total_payment = process_coins()
        if check_transaction(total_payment, beverage_type):
            make_coffee(beverage_type)


stay_on = True
while stay_on:
    user_input = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if user_input == "off":
        stay_on = False
    elif user_input == "report":
        print_report()
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        check_resources(user_input)
    else:
        print("Invalid input. Turning off machine.")
        stay_on = False