from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

choice = input(f"What would you like: {menu.get_items()}? ")
drink = menu.find_drink(choice)
if coffee.is_resource_sufficient(drink):
    if money.make_payment(drink.cost):
        coffee.make_coffee(drink)
