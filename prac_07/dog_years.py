# Dog Years

"""
HUMAN_YEARS_TO_DOG_YEARS_CONVERSION_RATE_FOR_FIRST_TWO_YEARS = 10.5
HUMAN_YEARS_TO_DOG_YEARS_CONVERSION_RATE_AFTER_FIRST_TWO_YEARS = 4
HUMAN_YEARS_TO_DOG_YEARS_CONVERTED_VALUE_FOR_FIRST_TWO_YEARS = 21
FIRST_TWO_YEARS = 2
SENTINEL = -1
function main()
    age_in_human_years = int(input("Age in human years: "))
    while age_in_human_years != SENTINEL
        age_in_dog_years = get_age_in_dog_years(age_in_human_years)
        print age_in_dog_years
        age_in_human_years = int(input("Age in human years: "))

function get_age_in_dog_years(age_in_human_years)
    if age_in_human_years <= 2
        age_in_dog_years = age_in_human_years * HUMAN_YEARS_TO_DOG_YEARS_CONVERSION_RATE_FOR_FIRST_TWO_YEARS
    else
        age_in_dog_years = HUMAN_YEARS_TO_DOG_YEARS_CONVERTED_VALUE_FOR_FIRST_TWO_YEARS + (
                age_in_human_years - FIRST_TWO_YEARS) * HUMAN_YEARS_TO_DOG_YEARS_CONVERSION_RATE_AFTER_FIRST_TWO_YEARS
    return age_in_dog_years
"""


HUMAN_YEARS_TO_DOG_YEARS_CONVERSION_RATE_FOR_FIRST_TWO_YEARS = 10.5  # Each year of the first two human years is equal
# to 10.5 dog years.
HUMAN_YEARS_TO_DOG_YEARS_CONVERSION_RATE_AFTER_FIRST_TWO_YEARS = 4  # After first two years, each human year equals 4
# dog years.
HUMAN_YEARS_TO_DOG_YEARS_CONVERTED_VALUE_FOR_FIRST_TWO_YEARS = 21  # The converted value of human years to dog years
# for first two years.
FIRST_TWO_YEARS = 2
SENTINEL = -1


def main():
    age_in_human_years = int(input("Age in human years: "))
    while age_in_human_years != SENTINEL:
        age_in_dog_years = get_age_in_dog_years(age_in_human_years)
        print(f"Age in dog years is {age_in_dog_years}")
        age_in_human_years = int(input("Age in human years: "))


def get_age_in_dog_years(age_in_human_years):
    """Calculate age in dog years from age in human years."""
    if age_in_human_years <= 2:
        age_in_dog_years = age_in_human_years * HUMAN_YEARS_TO_DOG_YEARS_CONVERSION_RATE_FOR_FIRST_TWO_YEARS
    else:
        age_in_dog_years = HUMAN_YEARS_TO_DOG_YEARS_CONVERTED_VALUE_FOR_FIRST_TWO_YEARS + (
                age_in_human_years - FIRST_TWO_YEARS) * HUMAN_YEARS_TO_DOG_YEARS_CONVERSION_RATE_AFTER_FIRST_TWO_YEARS
    return age_in_dog_years


main()
