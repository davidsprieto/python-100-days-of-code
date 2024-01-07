# Day 16/100 - Object-Oriented Programming (OOP)

# Coffee machine project classes
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Formats tabular data
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokémon name", 'Type']
table.add_rows([
    ["Pikachu", "Electric"],
    ["Squirtle", "Water"],
    ["Charmander", "Fire"]
])
table.align = "l"
print(table)

# Coffee Project refactored using OOP
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_is_on = True

while machine_is_on:

    user_coffee_choice = input("What would you like:\nEspresso - $1.50\nLatte - $2.50\nCappuccino - $3.00\n---> ").lower().strip()

    if user_coffee_choice == "off":
        machine_is_on = False
    elif user_coffee_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_coffee_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)