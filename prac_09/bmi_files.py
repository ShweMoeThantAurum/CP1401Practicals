# BMI Files
"""
function main
    number_of_people = get_valid_number("Number of people: ", 0, 1000)
    open "bmis.txt" for appending as out_file
    for i in range(int(number_of_people)):
        height = get_valid_number("Height(m): ", 0, 3)
        weight = get_valid_number("Weight(kg): ", 0, 300)
        bmi = calculate_bmi(height, weight)
        write bmi in out_file
    close out_file
    open "bmis.txt" for reading as in_file
    for line in in_file
        bmi = line as float
        weight_category = determine_weight_category(bmi)
        print(f"BMI {bmi:,.1f}, considered {weight_category}")
    close in_file

function get_valid_number(prompt, low, high)
    number = float(input(prompt))
    while number < low or number > high
        print("Invalid input")
        number = float(input(prompt))
    return number

function calculate_bmi(height, weight)
    return weight / (height ** 2)


function determine_weight_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"
"""


def main():
    number_of_people = get_valid_number("Number of people: ", 0, 1000)
    out_file = open("bmis.txt", "a")
    for i in range(int(number_of_people)):
        height = get_valid_number("Height(m): ", 0, 3)
        weight = get_valid_number("Weight(kg): ", 0, 300)
        bmi = calculate_bmi(height, weight)
        out_file.write("{:.1f} \n".format(bmi))
    out_file.close()
    in_file = open("bmis.txt", "r")
    for line in in_file:
        bmi = float(line)
        weight_category = determine_weight_category(bmi)
        print(f"BMI {bmi:,.1f}, considered {weight_category}")
    in_file.close()


def get_valid_number(prompt, low, high):
    """Validate the input numbers."""
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number


def calculate_bmi(height, weight):
    """Calculate the bmi from the weight."""
    return weight / (height ** 2)


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


main()
