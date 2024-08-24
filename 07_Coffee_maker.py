MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
profit = 0


def process_coins():
    """Return the total calculated coins"""
    print("Please enter the coins:")
    total = int(input("How many Quarters? ")) * 0.25
    total += int(input("How many Dimes? ")) * 0.1
    total += int(input("How many Nickles? ")) * 0.05
    total += int(input("How many Pennies? ")) * 0.01
    return total


def is_transaction_successful(money_gained, drink_cost):
    global profit
    """Return True if the payment is enough, False otherwise."""
    if money_gained >= drink_cost:
        change = round(money_gained - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


def check_resources(choice):
    """Check if resources are sufficient to make the chosen coffee."""
    if choice in MENU.keys():
        required_ingredients = MENU[choice]["ingredients"]

        # Check if each required ingredient is available
        for item in required_ingredients:
            if required_ingredients[item] > resources.get(item, 0):
                print(f"Sorry, there is not enough {item}.")
                return False

        # Process payment
        amount = process_coins()
        if is_transaction_successful(amount, MENU[choice]["cost"]):
            make_coffee(choice, required_ingredients)
            return True
    else:
        print("Order not available")
        return False


machine = True

while machine:
    order = input("What would you like to order ('Espresso', 'Latte', 'Cappuccino')? ").lower()

    if order == "report":
        for key, value in resources.items():
            print(f"{key.capitalize()}: {value}ml")
        print(f"Money: ${profit}")
    elif order == "off":
        machine = False
    else:
        check_resources(order)
