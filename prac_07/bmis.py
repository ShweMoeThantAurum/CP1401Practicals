# BMIs
"""
HEIGHT = 1.75
function main_1()
    for weight in range(50, 101, 2)
        bmi = calculate_bmi(weight)
        category = determine_weight_category(bmi)
        print HEIGHT, weight, bmi, weight category

function calculate_bmi(weight)
    return weight / (HEIGHT ** 2)

function determine_weight_category(bmi)
    if bmi < 18.5
        return "underweight"
    else if bmi < 25
        return "normal"
    else if bmi < 30
        return "overweight"
    else
        return "obese"
"""


HEIGHT = 1.75


def main_1():  # I know main_1 is not a good variable name but there are 2 main functions in one py file.
    for weight in range(50, 101, 2):
        bmi = calculate_bmi(weight)
        category = determine_weight_category(bmi)
        print(f"Height {HEIGHT}m, Weight {weight}kg = BMI {bmi:,.1f}, considered {category}")


def calculate_bmi(weight):
    """Calculate the bmi from the weight."""
    return weight / (HEIGHT ** 2)


def determine_weight_category(bmi):
    """Determine weight category based on bmi."""
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"


main_1()


"""
function main_2()
    for height in range(150, 191, 10)
        for weight in range(50, 101, 10)
            bmi = calculate_bmi(weight, height)
            category = determine_weight_category(bmi)
            print Height, weight, bmi, weight category     

function calculate_bmi(weight, height)
    return weight / ((height/100) ** 2)

function determine_weight_category(bmi)
    if bmi < 18.5
        return "underweight"
    else if bmi < 25
        return "normal"
    else if bmi < 30
        return "overweight"
    else
        return "obese"
"""


def main_2():
    for height in range(150, 191, 10):
        for weight in range(50, 101, 10):
            bmi = calculate_bmi(weight, height)
            category = determine_weight_category(bmi)
            print(f"Height {height/100}m, Weight {weight}kg = BMI {bmi:,.1f}, considered {category}")


def calculate_bmi(weight, height):
    """Calculate bmi based on weight and height."""
    return weight / ((height/100) ** 2)


def determine_weight_category(bmi):
    """Determine weight category based on bmi."""
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"


main_2()
