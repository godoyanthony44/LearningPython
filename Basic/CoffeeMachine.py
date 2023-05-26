from os import system as sys
from time import sleep
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coffee_machine_on = True


def is_resources_sufficient(coffee):
    if coffee == "espresso":
        if (MENU[f'{coffee}']['ingredients']['water'] <= resources['water']) and (
                MENU[f'{coffee}']['ingredients']['coffee'] <= resources['coffee']):
            return True
        else:
            return False
    elif coffee =="latte" or coffee == "cappuccino":
        if (MENU[f'{coffee}']['ingredients']['water'] <= resources['water']) and (
                MENU[f'{coffee}']['ingredients']['coffee'] <= resources['coffee']) and (
                MENU[f'{coffee}']['ingredients']['milk'] <= resources['milk']):
            return True
        else:
            return False
    else:
        print("You did not input a coffee on the menu!")
        return False


def money_machine(coffee):
    global profit
    print("Please insert coins. ")
    dollars = int(input("How many dollars?: "))
    quarters = int(input("How many quarters?: "))
    total = dollars + (quarters*.25)
    if MENU[f'{coffee}']['cost'] == total:
        profit += total
        return True
    elif MENU[f'{coffee}']['cost'] > total:
        print("Sorry their is not enough money")
        print(f"${total} will be returned to you")
        return False
    elif MENU[f'{coffee}']['cost'] < total:
        change = (total - int(MENU[f'{coffee}']['cost']))
        profit += MENU[f'{coffee}']['cost']
        print(f"Here is ${change} in change.")
        return True
    else:
        print("You did not input a number.")
        return False


def deplete_resources(coffee):
    if coffee == "latte" or coffee == "cappuccino":
        resources['water'] -= MENU[f'{coffee}']['ingredients']['water']
        resources['milk'] -= MENU[f'{coffee}']['ingredients']['milk']
        resources['coffee'] -= MENU[f'{coffee}']['ingredients']['coffee']
    elif coffee == 'espresso':
        resources['coffee'] -= MENU[f'{coffee}']['ingredients']['coffee']
        resources['water'] -= MENU[f'{coffee}']['ingredients']['water']


while coffee_machine_on:
    sys('clear')
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_choice == 'off':
        coffee_machine_on = False
        break
    elif coffee_choice == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}\n")
        sleep(3)
    else:
        enough_resources = is_resources_sufficient(coffee_choice)
        if enough_resources:
            enough_money = money_machine(coffee_choice)
            sleep(3)
            if enough_money:
                deplete_resources(coffee_choice)
                print(f"Here is your {coffee_choice} ☕️ Enjoy!")
                sleep(3)
        else:
            print("Sorry there is not enough resources")
            sleep(3)

            break

