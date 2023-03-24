# 1. Jerry the Driver

"""
MILE_TO_KILOMETERS_CONVERSION_RATE = 1.60934  # 1 mile = 1.60934 kilometres
function main
    speed_in_mph = get_valid_number("speed in mph")
    speed_limit_in_kph = get_valid_number("speed limit in kph")
    speed_in_kph = convert_miles_to_km(speed_in_mph)
    speed_over_the_limit_in_kph = speed_in_kph - speed_limit_in_kph
    fine = determine_fine(speed_in_km, speed_limit_in_kph)
    print fine

function get_valid_number(prompt, low)
    number = float(input(prompt))
    while number < low
        print error message
        number = float(input(prompt))
    return number

function convert_miles_to_km(speed_in_mph)
    return speed_in_mph * MILE_TO_KILOMETERS_CONVERSION_RATE

function determine_fine(speed_over_the_limit_in_kph)
    if speed_over_the_limit_in_kph < 0
        fine_amount = 0
    else if speed_over_the_limit_in_kph < 13
        fine_amount = 177
    else if speed_over_the_limit_in_kph <= 20
        fine_amount = 266
    else if speed_over_the_limit_in_kph <= 30
        fine_amount = 444
    else if speed_over_the_limit_in_kph <= 40
        fine_amount = 622
    else
        fine_amount = 1245
    return fine_amount
"""


MILE_TO_KILOMETERS_CONVERSION_RATE = 1.60934  # 1 mile = 1.60934 kilometres


def main():
    speed_in_mph = get_valid_number("Speed in mph: ", 0)
    speed_limit_in_kph = get_valid_number("Speed limit in kph: ", 0)
    speed_in_kph = convert_miles_to_km(speed_in_mph)
    speed_over_the_limit_in_kph = speed_in_kph - speed_limit_in_kph
    fine = determine_fine(speed_over_the_limit_in_kph)
    print(f"Your fine is ${fine}.")


def get_valid_number(prompt, low):
    """Determine whether the input numbers are valid or not."""
    number = float(input(prompt))
    while number < low:
        print("Invalid input")
        number = float(input(prompt))
    return number


def convert_miles_to_km(speed_in_mph):
    """Convert speed in miles per hour to speed in kilometers per hour"""
    return speed_in_mph * MILE_TO_KILOMETERS_CONVERSION_RATE


def determine_fine(speed_over_the_limit_in_kph):
    """Determine the fine amount based on the speed over the limit."""
    if speed_over_the_limit_in_kph < 0:
        fine_amount = 0
    elif speed_over_the_limit_in_kph < 13:
        fine_amount = 177
    elif speed_over_the_limit_in_kph <= 20:
        fine_amount = 266
    elif speed_over_the_limit_in_kph <= 30:
        fine_amount = 444
    elif speed_over_the_limit_in_kph <= 40:
        fine_amount = 622
    else:
        fine_amount = 1245
    return fine_amount


main()
