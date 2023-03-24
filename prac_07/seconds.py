# Seconds Display
"""
SECONDS_PER_MINUTE = 60
function main()
    for number_of_seconds in range(0, 3176, 635)
        minutes, seconds = convert_minutes_and_seconds(number_of_seconds)
        print minutes, seconds
    number_of_seconds = get_valid_number("Favorite duration in seconds: ", 0, 3176)
    minutes, seconds = convert_minutes_and_seconds(number_of_seconds)
    print minutes, seconds

function get_valid_number(prompt, low, high)
    number = int(input(prompt))
    while number < low or number > high
        print error massage
        number = int(input(prompt))
    return number

function convert_minutes_and_seconds(number_of_seconds)
    minutes = number_of_seconds // SECONDS_PER_MINUTE
    seconds = number_of_seconds % SECONDS_PER_MINUTE
    return minutes, seconds
"""


SECONDS_PER_MINUTE = 60


def main():
    for number_of_seconds in range(0, 3176, 635):
        minutes, seconds = convert_minutes_and_seconds(number_of_seconds)
        print(f"{number_of_seconds} seconds is {minutes}m {seconds}s")
    number_of_seconds = get_valid_number("Favorite duration in seconds: ", 0, 3176)
    minutes, seconds = convert_minutes_and_seconds(number_of_seconds)
    print(f"You love {minutes}m {seconds}s.")


def get_valid_number(prompt, low, high):
    """Validate the number so that the number is in the range of 0 and 3176."""
    number = int(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = int(input(prompt))
    return number


def convert_minutes_and_seconds(number_of_seconds):
    """Calculate minutes and seconds."""
    minutes = number_of_seconds // SECONDS_PER_MINUTE
    seconds = number_of_seconds % SECONDS_PER_MINUTE
    return minutes, seconds


main()
