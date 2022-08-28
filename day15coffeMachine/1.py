from inspect import walktree
from msilib.schema import ReserveCost


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
}

profit=0
def is_resource_sufficient(order_ingredients):
    """returns true when roder can be made, false if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """returns the total calculated from coins inserted."""
    print("please insert coins.")
    total=int(input("how many quarters?: "))*0.25
    total+=int(input("how many dimes?: "))*0.1
    total+=int(input("how many nickles?: "))*0.05
    total+=int(input("how many pennies?: "))*0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """return true when the payment is accepted, or false if money is insufficient."""
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"here is ${change} şn change.")
        global profit
        profit+=drink_cost
        return True
    else:
        print("sorry that's not enough money. money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    """deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"here is your {drink_name}")         

is_on=True
while is_on:
    choice=input("what would you like(espresso/latte/cappuccino): ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit}")
    else:
        drink=MENU[choice]
        print(drink)
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])