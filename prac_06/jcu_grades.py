# JCU grades
"""
function main
    SENTINEL = -1
    get score
    while score > SENTINEL
        print function get_grade(score)
        get score
    get random_scores
    import random
    for i in range(random_scores)
        get score (random)
        print function get_grade(score)
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
    return f"The score {score} is {result}."
"""


def main():
    SENTINEL = -1
    score = float(input("Score: "))
    while score > SENTINEL:
        print(get_grade(score))
        score = float(input("Score: "))
    random_scores = int(input("How many random scores: "))
    import random
    for i in range(random_scores):
        score = random.randint(1, 100)
        print(get_grade(score))


def get_grade(score):
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
    return f"The score {score} is {result}."


main()
