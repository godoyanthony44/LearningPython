from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()


coffee_machine_on = True
while coffee_machine_on:
    coffee_choice = input(f"What would you like? ({menu.get_items()}): ")
    if coffee_choice == 'off':
        coffee_machine_on = False
        break
    elif coffee_choice == 'report':
        coffeeMaker.report()
        moneyMachine.report()
    else:
        coffee = menu.find_drink(coffee_choice)
        if coffeeMaker.is_resource_sufficient(coffee) and moneyMachine.make_payment(coffee.cost):
                coffeeMaker.make_coffee(coffee)







