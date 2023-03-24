# Coffee orders
"""
import random

MENU = "(O)rder - (D)rink - (R)andom choice - (Q)uit"
COFFEE_CHOICES = ["Flat White", "Espresso", "Long Black", "Babyccino"]
INSTRUCTION = "- Insert portafilter into grinder\n- Press grind button to grind beans into portafilter\n- Distribute " \
              "grounds\n- Tamp grounds\n- Insert full portafilter into group head\n- Press shot button to pour " \
              "espresso into cup "
current_coffee_order as an empty string
print("Welcome to the IT@JCU Coffee Shop")
print menu
menu_choice = input(">>> ").upper()
while menu_choice != "Q"
    if menu_choice == "O"
        coffee_choice = input("Please choose from:\nFlat White - Espresso - Long Black - Babyccino - ? ").title()
        current_coffee_order = coffee_choice
        while coffee_choice not in COFFEE_CHOICES
            print error message
            coffee_choice = input("?").title()
            current_coffee_order = coffee_choice
        if coffee_choice == "Flat White"
            print(f"Here's how to make a/n Flat White:\n{INSTRUCTION}\n- Fill jug with milk\n- Steam milk until nice "
                  f"microfoam formed and milk up to temperature\n- Swirl milk gently in jug\n- Pour milk into cup... "
                  f"carefully, artistically :)")
        else if coffee_choice == "Espresso"
            print(f"Here's how to make a/n Espresso:\n{INSTRUCTION}")
        else if coffee_choice == "Long Black"
            print(f"Here's how to make a/n Long Black:\n{INSTRUCTION}\n- Add hot water to cup")
        else if coffee_choice == "Babyccino"
            print(f"Here's how to make a/n Babyccino:\n{INSTRUCTION}\n- Add milk and foam to cup")
    else if menu_choice == "D"
        if current_coffee_order == ""
            print("Oh...where's my coffee?")
        else
            print(f"Mmmm, nice {current_coffee_order}")
    else if menu_choice == "R"
        coffee_choice = random.choice(COFFEE_CHOICES)
        print(coffee_choice)
        if coffee_choice == "Flat White"
            print(f"Here's how to make a/n Flat White:\n{INSTRUCTION}\n- Fill jug with milk\n- Steam milk until nice "
                  f"microfoam formed and milk up to temperature\n- Swirl milk gently in jug\n- Pour milk into cup... "
                  f"carefully, artistically :)")
        else if coffee_choice == "Espresso"
            print(f"Here's how to make a/n Espresso:\n{INSTRUCTION}")
        else if coffee_choice == "Long Black"
            print(f"Here's how to make a/n Long Black:\n{INSTRUCTION}\n- Add hot water to cup")
        else if coffee_choice == "Babyccino"
            print(f"Here's how to make a/n Babyccino:\n{INSTRUCTION}\n- Add milk and foam to cup")
        current_coffee_order = coffee_choice
    else:
        print error message
    print menu
    menu_choice = input(">>> ").upper()
print("Thanks for drinking coffee")
"""

import random

MENU = "(O)rder - (D)rink - (R)andom choice - (Q)uit"
COFFEE_CHOICES = ["Flat White", "Espresso", "Long Black", "Babyccino"]
INSTRUCTION = "- Insert portafilter into grinder\n- Press grind button to grind beans into portafilter\n- Distribute " \
              "grounds\n- Tamp grounds\n- Insert full portafilter into group head\n- Press shot button to pour " \
              "espresso into cup "
current_coffee_order = ""
print("Welcome to the IT@JCU Coffee Shop")
print(MENU)
menu_choice = input(">>> ").upper()
while menu_choice != "Q":
    if menu_choice == "O":
        coffee_choice = input("Please choose from:\nFlat White - Espresso - Long Black - Babyccino - ? ").title()
        current_coffee_order = coffee_choice
        while coffee_choice not in COFFEE_CHOICES:
            print("Invalid order")
            coffee_choice = input("?").title()
            current_coffee_order = coffee_choice
        if coffee_choice == "Flat White":
            print(f"Here's how to make a/n Flat White:\n{INSTRUCTION}\n- Fill jug with milk\n- Steam milk until nice "
                  f"microfoam formed and milk up to temperature\n- Swirl milk gently in jug\n- Pour milk into cup... "
                  f"carefully, artistically :)")
        elif coffee_choice == "Espresso":
            print(f"Here's how to make a/n Espresso:\n{INSTRUCTION}")
        elif coffee_choice == "Long Black":
            print(f"Here's how to make a/n Long Black:\n{INSTRUCTION}\n- Add hot water to cup")
        elif coffee_choice == "Babyccino":
            print(f"Here's how to make a/n Babyccino:\n{INSTRUCTION}\n- Add milk and foam to cup")
    elif menu_choice == "D":
        if current_coffee_order == "":
            print("Oh...where's my coffee?")
        else:
            print(f"Mmmm, nice {current_coffee_order}")
    elif menu_choice == "R":
        coffee_choice = random.choice(COFFEE_CHOICES)
        print(coffee_choice)
        if coffee_choice == "Flat White":
            print(f"Here's how to make a/n Flat White:\n{INSTRUCTION}\n- Fill jug with milk\n- Steam milk until nice "
                  f"microfoam formed and milk up to temperature\n- Swirl milk gently in jug\n- Pour milk into cup... "
                  f"carefully, artistically :)")
        elif coffee_choice == "Espresso":
            print(f"Here's how to make a/n Espresso:\n{INSTRUCTION}")
        elif coffee_choice == "Long Black":
            print(f"Here's how to make a/n Long Black:\n{INSTRUCTION}\n- Add hot water to cup")
        elif coffee_choice == "Babyccino":
            print(f"Here's how to make a/n Babyccino:\n{INSTRUCTION}\n- Add milk and foam to cup")
        current_coffee_order = coffee_choice
    else:
        print("Invalid option")
    print(MENU)
    menu_choice = input(">>> ").upper()
print("Thanks for drinking coffee")
