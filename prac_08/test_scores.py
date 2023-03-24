# 2. Test Scores

"""
NUMBER_OF_SCORES = 4

function main()
    scores = empty list
    for i in range(1, NUMBER_OF_SCORES+1)
        score = get_valid_number(f"Score {i}: ", 0, 100)
        add score to score
        grade = get_grade(score)
        print(f"Score {i}, which is {grade}.")
    average_score = calculate_average(scores)
    last_score = scores[3]
    print(f"The average score was {average_score}")
    print(f"The trend is {calculate_trend(last_score, average_score)}")

function get_valid_number(prompt, low, high)
    number = float(input(prompt))
    while number < low or number > high
        print("Invalid input")
        number = float(input(prompt))
    return number

function get_grade(score)
    if score < 50
        result = "F"
    else if score < 65
        result = "P"
    else if score < 75
        result = "C"
    else if score < 85
        result = "D"
    else
        result = "HD"
    return result

function calculate_average(scores)
    return sum(scores)/len(scores)

function calculate_trend(last_score, average_score)
    if last_score > average_score
        return "positive"
    else
        return "negative"

main()
"""

NUMBER_OF_SCORES = 4


def main():
    scores = []
    for i in range(1, NUMBER_OF_SCORES+1):
        score = get_valid_number(f"Score {i}: ", 0, 100)
        scores.append(score)
        grade = get_grade(score)
        print(f"Score {i}, which is {grade}.")
    average_score = calculate_average(scores)
    last_score = scores[3]
    print(f"The average score was {average_score}")
    print(f"The trend is {calculate_trend(last_score, average_score)}")


def get_valid_number(prompt, low, high):
    """Determine whether the input numbers are valid or not."""
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number


def get_grade(score):
    """Determine grades based on scores."""
    if score < 50:
        result = "F"
    elif score < 65:
        result = "P"
    elif score < 75:
        result = "C"
    elif score < 85:
        result = "D"
    else:
        result = "HD"
    return result


def calculate_average(scores):
    """Calculate average of the scores."""
    return sum(scores)/len(scores)


def calculate_trend(last_score, average_score):
    """Calculate trend based on last_score and average_score."""
    if last_score > average_score:
        return "positive"
    else:
        return "negative"


main()
