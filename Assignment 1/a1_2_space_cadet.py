"""
CP1401 2022-3 Assignment 1
Program 1 - Pay Calculator
Student Name: <Shwe Moe Thant>
Date Started: <6.12.2022>
"""
# Space Cadet Results

"""
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 50
TOTAL_SCORE = 100
get practical_score and exam_score
total_score= practical_score+exam_score
print total_score
if total_score<50
    print "You failed. Please try again next year."
else if practical_score >= exam_score
    print "You will become a field agent.
else if exam_score >= practical_score
    print "You will become a desk officer.
if total_score >= 90
    print "Congratulations on making the honour roll!
"""
print("Welcome Trainee Space Cadet. How did you do?")
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 50
TOTAL_SCORE = 100
practical_score = int(input(f"Practical score ({MINIMUM_SCORE}-{MAXIMUM_SCORE}): "))
exam_score = int(input(f"Exam score ({MINIMUM_SCORE}-{MAXIMUM_SCORE}): "))
total_score = practical_score+exam_score
print(f"Your total score is {total_score} out of {TOTAL_SCORE}.")
if total_score < 50:
    print("You failed. Please try again next year.")
elif practical_score >= exam_score:
    print("You will become a field agent.")
elif exam_score >= practical_score:
    print("You will become a desk officer.")
if total_score >= 90:
    print("Congratulations on making the honour roll!")
