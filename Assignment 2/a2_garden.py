"""
CP 1401 2023-1 Assignment 2
Market Garden Simulator
Student Name: Shwe Moe Thant
Date started: 21/01/2023

Pseudocode:

import random

MINIMUM_RAINFALL = 0
MAXIMUM_RAINFALL = 128
RAINFALL_THRESHOLD_FOR_PLANT_DEATH = 32
MENU = (W)ait, (D)isplay plants, (A)dd new plant, (Q)uit


function main()
    all_plants_in_garden = []
    daily_food_produced_by_each_plant = []
    total_food_produced_per_day = 0
    days_simulated = 0
    display_greetings()  
    get_decision(all_plants_in_garden)  
    print MENU
    get choice 
    while choice != "Q"
        if choice == "W"
            days_simulated, total_food_produced_per_day = wait_plants(all_plants_in_garden,
                                                                      daily_food_produced_by_each_plant, days_simulated,
                                                                      total_food_produced_per_day)
        else if choice == "D"
            display_plants(all_plants_in_garden)  
        else if choice == "A"
            total_food_produced_per_day = add_new_plant(all_plants_in_garden, total_food_produced_per_day)
        else:
            print error message 
        print After {days_simulated} days, you have {len(all_plants_in_garden)} plants and your total food is 
              {total_food_produced_per_day}.
        print MENU 
        get choice
    quit_program(all_plants_in_garden, days_simulated, total_food_produced_per_day)


function display_greetings()
    print "Welcome to my garden.Plants cost and generate food according to their name length (e.g., Sage plants cost "
          "4).You can buy new plants with the food your garden generates.You get up to 128 mm of rain per day. Not "
          "all plants can survive with less than 32.Enjoy :)


function get_decision(all_plants_in_garden)
    get load_existing_plants 
    if load_existing_plants == "Y"
        open "plants.txt" for reading as in_file 
        for line in in_file
            append line in all_plants_in_garden
        print loaded
        print existing plants
        close in_file
    else:
        open "plants.txt" for reading as in_file 
        for line in in_file
            append line in all_plants_in_garden
        print existing plants
        close in_file


function wait_plants(all_plants_in_garden, daily_food_produced_by_each_plant, days_simulated, total_food_produced_per_day)
    days_simulated = days_simulated + 1
    clear daily_food_produced_by_each_plant list
    rainfall = get_random_rainfall()
    if rainfall < RAINFALL_THRESHOLD_FOR_PLANT_DEATH
        removed_plant = random.choice(all_plants_in_garden)
        all_plants_in_garden.remove(removed_plant)
        print Sadly, your {removed_plant} plant has died. 
    else
        percent = get_percent(rainfall)
        for plant in all_plants_in_garden
            total_food_produced_per_day = get_total_food_produced_per_day(daily_food_produced_by_each_plant,
                                                                          percent, plant,
                                                                          total_food_produced_per_day)
        print daily_food_produced_by_each_plant
    return days_simulated, total_food_produced_per_day


function get_random_rainfall()
    rainfall = random.randint(MINIMUM_RAINFALL, MAXIMUM_RAINFALL)
    print rainfall
    return rainfall


function get_percent(rainfall)
    percent = (random.uniform(rainfall / 3, rainfall)) / MAXIMUM_RAINFALL
    return percent


function get_total_food_produced_per_day(daily_food_produced_by_each_plant, percent, plant,
                                    total_food_produced_per_day)
    food_produced_by_each_plant = int(percent * len(plant))
    daily_food_produced_by_each_plant.append(f"{plant} produced {food_produced_by_each_plant}")
    total_food_produced_per_day += food_produced_by_each_plant
    return total_food_produced_per_day


function display_plants(all_plants_in_garden)
    print all_plants_in_garden


function add_new_plant(all_plants_in_garden, total_food_produced_per_day)
    new_plant = validate_new_plant(all_plants_in_garden)
    if len(new_plant) > total_food_produced_per_day
        print {new_plant} would cost {len(new_plant)} food. With only {total_food_produced_per_day}, "
              f"you can't afford it.
    else
        open plants.txt for appending out_file 
        write new_plant in out_file
        close out_file
        total_food_produced_per_day = total_food_produced_per_day - len(new_plant)
        append new_plant in all_plants_in_garden
    return total_food_produced_per_day


function validate_new_plant(all_plants_in_garden)
    get new_plant 
    while new_plant == ""
        print error message
        get new_plant 
    while new_plant in all_plants_in_garden
        print You already have a {new_plant} plant.
        get new_plant 
    return new_plant


function quit_program(all_plants_in_garden, days_simulated, total_food_produced_per_day)
    print all_plants_in_garden
    print After {days_simulated} days, you have {len(all_plants_in_garden)} plants and your total food is
          {total_food_produced_per_day}.
    get save_plants_file 
    if save_plants_file == "Y"
        print Saved.Thank you for simulating. Now enjoy some real plants. 
    else
        print Saved.Thank you for simulating. Now enjoy some real plants. 


main()
"""

import random

MINIMUM_RAINFALL = 0
MAXIMUM_RAINFALL = 128
RAINFALL_THRESHOLD_FOR_PLANT_DEATH = 32
MENU = "(W)ait\n(D)isplay plants\n(A)dd new plant\n(Q)uit"


def main():
    all_plants_in_garden = []
    daily_food_produced_by_each_plant = []
    total_food_produced_per_day = 0
    days_simulated = 0
    display_greetings()  # Display instructions and greetings.
    get_decision(all_plants_in_garden)  # Get the user's input to decide whether to load existing plants or not.
    print(MENU)
    choice = input("Choose: ").upper()
    while choice != "Q":
        if choice == "W":
            days_simulated, total_food_produced_per_day = wait_plants(all_plants_in_garden,
                                                                      daily_food_produced_by_each_plant, days_simulated,
                                                                      total_food_produced_per_day)
        elif choice == "D":
            display_plants(all_plants_in_garden)  # Display all plants in garden.
        elif choice == "A":
            total_food_produced_per_day = add_new_plant(all_plants_in_garden, total_food_produced_per_day)
        else:
            print("Invalid choice")
        print(f"After {days_simulated} days, you have {len(all_plants_in_garden)} plants and your total food is "
              f"{total_food_produced_per_day}.")
        print(MENU)
        choice = input("Choose: ").upper()
    quit_program(all_plants_in_garden, days_simulated, total_food_produced_per_day)


def display_greetings():
    """Show the instructions and the greetings"""
    print("Welcome to my garden.\nPlants cost and generate food according to their name length (e.g., Sage plants cost "
          "4).\nYou can buy new plants with the food your garden generates.\nYou get up to 128 mm of rain per day. Not "
          "all plants can survive with less than 32.\nEnjoy :)")


def get_decision(all_plants_in_garden):
    """Get the user's decision whether he wants to load existing plants from plants.txt file or not."""
    load_existing_plants = input("Would you like to load your plants from plants.txt (Y/n)? ").upper()
    if load_existing_plants == "Y":
        in_file = open("plants.txt", "r")
        for line in in_file:
            all_plants_in_garden.append(line.strip())
        print("Loaded.")
        print("You start with these plants:\n{}".format(', '.join(all_plants_in_garden)))
        in_file.close()
    else:
        in_file = open("plants.txt", "r")
        for line in in_file:
            all_plants_in_garden.append(line.strip())
        print("You start with these plants:\n{}".format(', '.join(all_plants_in_garden)))
        in_file.close()


def wait_plants(all_plants_in_garden, daily_food_produced_by_each_plant, days_simulated, total_food_produced_per_day):
    """Wait plants to generate daily food_produced by each plant and total food produced per day."""
    days_simulated = days_simulated + 1
    daily_food_produced_by_each_plant.clear()
    rainfall = get_random_rainfall()
    if rainfall < RAINFALL_THRESHOLD_FOR_PLANT_DEATH:
        removed_plant = random.choice(all_plants_in_garden)
        all_plants_in_garden.remove(removed_plant)
        print(f"Sadly, your {removed_plant} plant has died.")
    else:
        percent = get_percent(rainfall)
        for plant in all_plants_in_garden:
            total_food_produced_per_day = get_total_food_produced_per_day(daily_food_produced_by_each_plant,
                                                                          percent, plant,
                                                                          total_food_produced_per_day)
        print(','.join(daily_food_produced_by_each_plant))
    return days_simulated, total_food_produced_per_day


def get_random_rainfall():
    """Get random number for rainfall."""
    rainfall = random.randint(MINIMUM_RAINFALL, MAXIMUM_RAINFALL)
    print(f"Rainfall: {rainfall}mm")
    return rainfall


def get_percent(rainfall):
    """Calculate the percent."""
    percent = (random.uniform(rainfall / 3, rainfall)) / MAXIMUM_RAINFALL
    return percent


def get_total_food_produced_per_day(daily_food_produced_by_each_plant, percent, plant,
                                    total_food_produced_per_day):
    """Calculate the total food produced per day by all plants and daily food produced by each plant."""
    food_produced_by_each_plant = int(percent * len(plant))
    daily_food_produced_by_each_plant.append(f"{plant} produced {food_produced_by_each_plant}")
    total_food_produced_per_day += food_produced_by_each_plant
    return total_food_produced_per_day


def display_plants(all_plants_in_garden):
    """Show all plants in garden."""
    print(",".join(all_plants_in_garden))


def add_new_plant(all_plants_in_garden, total_food_produced_per_day):
    """Add a new plant, determine whether the new plant already existed or not."""
    new_plant = validate_new_plant(all_plants_in_garden)
    if len(new_plant) > total_food_produced_per_day:
        print(f"{new_plant} would cost {len(new_plant)} food. With only {total_food_produced_per_day}, "
              f"you can't afford it.")
    else:
        out_file = open("plants.txt", "a")
        out_file.write("\n" + new_plant)
        out_file.close()
        total_food_produced_per_day = total_food_produced_per_day - len(new_plant)
        all_plants_in_garden.append(new_plant)
    return total_food_produced_per_day


def validate_new_plant(all_plants_in_garden):
    """Validate new plants."""
    new_plant = input("Enter plant name: ").title()
    while new_plant == "":
        print("Invalid plant name")
        new_plant = input("Enter plant name: ").title()
    while new_plant in all_plants_in_garden:
        print(f"You already have a {new_plant} plant.")
        new_plant = input("Enter plant name: ").title()
    return new_plant


def quit_program(all_plants_in_garden, days_simulated, total_food_produced_per_day):
    """Quit the program and print parting messages."""
    print("You start with these plants:\n{}".format(', '.join(all_plants_in_garden)))
    print(f"After {days_simulated} days, you have {len(all_plants_in_garden)} plants and your total food is"
          f" {total_food_produced_per_day}.")
    save_plants_file = input("Would you like to save your plants to plants.txt (Y/n)? ")
    if save_plants_file == "Y":
        print("Saved.\nThank you for simulating. Now enjoy some real plants.")
    else:
        print("Saved.\nThank you for simulating. Now enjoy some real plants.")


main()
