# Day 15/100 - The Coffee Machine Project

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

profit = 0
resources = {
    "water": 3000,
    "milk": 1000,
    "coffee": 500,
}


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${round_money(profit)}")


def is_resource_sufficient(order_ingredients):
    """Returns True when ingredients are sufficient and drink order can be made, or False when ingredients are insufficient"""
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins: ")
    total = float(input("How many quarters?: ")) * 0.25
    total += float(input("How many dimes?: ")) * 0.10
    total += float(input("How many nickels?: ")) * 0.05
    total += float(input("How many pennies?: ")) * 0.01
    return total


def round_money(money):
    money_to_string = str(money)
    if len(money_to_string) == 3:
        money_to_string += "0"
        return money_to_string
    else:
        round(money, 2)


def is_transaction_successful(money_inserted, drink_cost):
    """Returns True if enough money is inserted, or False if money inserted is insufficient"""
    if money_inserted >= drink_cost:
        change = round_money(money_inserted - drink_cost)
        print(f"Your change is: ${change}.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money...")
        print("Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required amount of ingredients from resources based on the drink the user ordered"""
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here is your {drink_name} ☕️")


machine_is_on = True

while machine_is_on:

    user_coffee_choice = input("What would you like:\nEspresso - $1.50\nLatte - $2.50\nCappuccino - $3.00\n---> ").lower().strip()

    if user_coffee_choice == "off":
        machine_is_on = False
    elif user_coffee_choice == "report":
        print_report()
    else:
        drink = MENU[user_coffee_choice]
        if is_resource_sufficient(drink["ingredients"]):
            user_payment = process_coins()
            if is_transaction_successful(user_payment, drink["cost"]):
                make_coffee(user_coffee_choice, drink["ingredients"])
