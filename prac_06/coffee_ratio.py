# Coffee ratio
"""
function main
    get ground_coffee(dose) and brewed_coffee(yield)
    calculate brew ratio
    determine coffee style
function calculate_brew_ratio
    return ground_coffee / brewed_coffee
function get_valid_number
    get number
    while number < low or number > high
        print "Invalid input"
        get number
    return number
function determine_coffee_style
    if brew_ratio <= 1/4 or brew_ratio <= 1/3
        return "lungo"
    else if brew_ratio <= 1/2:
        return "normale"
    else if brew_ratio >= 1/1:
        return "ristretto"
function def check_coffee():
    style = determine_coffee_style(1.01)
    print(style)
    style = determine_coffee_style(0.5)
    print(style)
    style = determine_coffee_style(0.01)
    print(style)
"""


def main():
    ground_coffee = get_valid_number("Dose(g): ", 0, 100)
    brewed_coffee = get_valid_number("Yield(g): ", 0, 100)
    brew_ratio = calculate_brew_ratio(ground_coffee, brewed_coffee)
    style = determine_coffee_style(brew_ratio)
    print(f"This coffee is considered as {style}.")


def calculate_brew_ratio(ground_coffee, brewed_coffee):
    return ground_coffee / brewed_coffee


def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number


def determine_coffee_style(brew_ratio):
    if brew_ratio <= 1/4 or brew_ratio <= 1/3:
        return "lungo"
    elif brew_ratio <= 1/2:
        return "normale"
    elif brew_ratio >= 1/1:
        return "ristretto"


# def check_coffee():
#     style = determine_coffee_style(1.01)
#     print(style)
#     style = determine_coffee_style(0.5)
#     print(style)
#     style = determine_coffee_style(0.01)
#     print(style)
#
#
# check_coffee()


main()
