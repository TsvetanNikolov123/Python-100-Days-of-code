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

COFFEE_ESPRESSO = "espresso"
COFFEE_LATTE = "latte"
COFFEE_CAPPUCCINO = "cappuccino"
TURN_OFF_MACHINE = "off"
REPORT_MACHINE = "report"

money_in_coffee_machine = 0


def print_coffee_machine_report(resources, money_in_coffee_machine):
    """Print the current status of the coffee machine resources and money."""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money_in_coffee_machine}")


def is_resource_sufficient(order_ingredients, available_resources):
    """Check if there are enough resources to make the drink."""
    for item in order_ingredients:
        if order_ingredients[item] > available_resources.get(item, 0):
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def sum_inserted_coins():
    """Calculate the total amount of money inserted by the user."""
    try:
        quarters = float(input("How many quarters?: "))
        dimes = float(input("How many dimes?: "))
        nickles = float(input("How many nickles?: "))
        pennies = float(input("How many pennies?: "))
        return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    except ValueError:
        print("Please enter valid numbers.")
        return 0


def process_coins_and_payment(drink_cost):
    """Handle coin insertion and payment processing."""
    global money_in_coffee_machine
    
    money = sum_inserted_coins()
    
    if money >= drink_cost:
        change = round(money - drink_cost, 2)
        money_in_coffee_machine += drink_cost
        
        if change > 0:
            print(f"Here is ${change} in change.")
        
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def update_resources(drink_ingredients):
    """Update the machine resources after making a drink."""
    for ingredient, amount in drink_ingredients.items():
        resources[ingredient] -= amount


def make_coffee(drink_name):
    """Process a coffee order from start to finish."""
    drink_info = MENU[drink_name]
    ingredients_needed = drink_info["ingredients"]
    
    # Check if resources are sufficient
    if not is_resource_sufficient(ingredients_needed, resources):
        return
    
    print("Please insert coins.")
    
    # Process payment
    if process_coins_and_payment(drink_info["cost"]):
        # Update resources
        update_resources(ingredients_needed)
        print(f"Here is your {drink_name}. Enjoy!")


def main():
    """Main program loop."""
    print("Welcome to the Coffee Machine!")
    
    while True:
        user_prompt = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower().strip()
        
        if user_prompt in [COFFEE_ESPRESSO, COFFEE_LATTE, COFFEE_CAPPUCCINO]:
            make_coffee(user_prompt)
            
        elif user_prompt == REPORT_MACHINE:
            print_coffee_machine_report(resources, money_in_coffee_machine)
            
        elif user_prompt == TURN_OFF_MACHINE:
            print("Turning off the coffee machine. Goodbye!")
            break
            
        else:
            print("Invalid selection. Please choose espresso, latte, cappuccino, report, or off.")


if __name__ == "__main__":
    main()