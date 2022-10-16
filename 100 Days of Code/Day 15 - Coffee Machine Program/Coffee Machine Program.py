"""
Coffee Machine Program
"""

menu = {
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


repeat = False

while not repeat:

    user_choice =input("What would you like? (espresso/latte/cappuccino): ")


    # def return_report(report):
    #     """
    #     If the user chooses "report", the function returns a string
    #     with the current amount of water, milk,and coffee.
    #     """
    #     return f"Water: {resources['water']} \nMilk: {resources['milk']} \
    #                 \nCoffee: {resources['coffee']}"

    # return_report(report=user_choice)

    def deplete_resources(menu_item):
        """
        If the user's choice is in the menu, then deplete the resources needed to make that choice.
        
        :param menu_item: the name of the menu item the user chose
        """
        if menu_item == "espresso" or menu_item == "latte" or menu_item == "cappuccino":
            for resource in ("water", "milk", "coffee"):
                needed = menu[menu_item]["ingredients"].get(resource, 0)
                resources[resource] -= needed
        elif menu_item == "report":
                print(f"Water: {resources['water']} \nMilk: {resources['milk']} \
                \nCoffee: {resources['coffee']}")


    deplete_resources(menu_item=user_choice)
