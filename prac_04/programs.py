# Error Checking
"""
SALARY_RATE= 5000
get worker_level
while worker_level <1 or worker_level >10
    print "Invalid worker level"
    get worker_level
salary= worker_level*SALARY_RATE
print "With your worker lever, your salary is "
"""

SALARY_RATE = 5000
worker_level = int(input("Worker level: "))
while worker_level < 1 or worker_level > 10:
    print("Invalid worker level")
    worker_level = int(input("Worker level: "))
salary = worker_level*SALARY_RATE
print(f"With worker level {worker_level}, your salary is ${salary:,.2f}.")

# Number Sequences

# a

for i in range(1, 101, 2):
    print(i)

# b

for i in range(1896, 2023, 4):
    print(i, end=" ")

# c

for i in range(0, 201, 2):  # This range is the even number between 1 and 200.
    print(i)

# Menus
"""
get choice
while choice != Q
    if choice== S
        print " :') "
    else if choice == F
        print " :'(
    else
        print "invalid choice"
print "Farewell"
"""

MENU = "(S)miley\n(F)rowny\n(Q)uit"
print(MENU)
choice = input("Please choose one of them: ").upper()
while choice != "Q":
    if choice == "S":
        print(" :') ")
    elif choice == "F":
        print(" :'( ")
    else:
        print("Invalid choice")
    choice = input("Please choose one of them: ").upper()
print("Farewell")

# Accumulation
# Average age
"""
SENTINEL = -1
total_age= 0
total_number_of_people= 0
while age != SENTINEL:
    get age
    total_age= total_age+age
    total_number_of_people= total_number_of_people + 1
if total_number_of_people != 0:
    print "The average is "
else:
    print "There is no age information."
"""

SENTINEL = -1
total_age = 0
total_number_of_people = 0
age = ""
while age != SENTINEL:
    age = int(input("Enter age: "))
    total_age = total_age + age
    total_number_of_people = total_number_of_people+1
    print("Please press (-1) to calculate the average. ")
if total_number_of_people != 0:
    print(f"The average is {total_age/total_number_of_people}. ")
else:
    print("There is no age information.")


# Smileys count
"""
get choice
count_for_smiley= 0
count_for_frowny= 0
while choice != Q
    if choice== S
        count_for_smiley= count_for_smiley+ 1
        print " :') "
    else if choice == F
        count_for_frowny= count_for_frowny+ 1
        print " :'(
    else
        print "invalid choice"
print "farewell"
"""

MENU = ["(S)miley", "(F)rowny", "(Q)uit"]
print(MENU)
count_for_smiley = 0
count_for_frowny = 0
choice = input("Please choose one of them: ").upper()
while choice != "Q":
    if choice == "S":
        count_for_smiley = count_for_smiley+1
        print(" :') ")
        print(f"The number for smiley is {count_for_smiley}.")
    elif choice == "F":
        count_for_frowny = count_for_frowny+1
        print(" :'( ")
        print(f"The number for frowny is {count_for_frowny}.")
    else:
        print("Invalid choice")
    choice = input("Please choose one of them: ").upper()
print("Farewell")

# Total numbers
"""
total= 0
get times
for i in range(1,times+1)
    get numbers
    total= total+numbers
print(The total of those numbers is )
"""
total = 0
times = int(input("How many numbers do you want to add up?"))
for i in range(1, times+1):
    numbers = int(input(f"Enter number {i}: "))
    total = total+numbers
print(f"The total of those {times} numbers is {total}.")

# Guessing game
"""
SECRET_NUMBER=6
GUESS_COUNT= 0
get guess
guess_count= guess_count+1
while guess != SECRET
    if guess <6
        print Higher
    else
        print Lower
    get guess
    guess_count= guess_count+1
print you got it in guess_count guess!
"""

SECRET = 6
GUESS_COUNT = 0
guess = int(input("Guess a number: "))
GUESS_COUNT = GUESS_COUNT+1
while guess != SECRET:
    if guess < 6:
        print("Higher")
    else:
        print("Lower")
    guess = int(input("Guess a number: "))
    GUESS_COUNT = GUESS_COUNT + 1
print(f"You got it in {GUESS_COUNT} guesses!")

# Nested Loops
"""
get number_of_rows and number_of_columns
for i in range (number_of_rows)
    for j in range (number_of_columns)
        print (j, end=" ")
    print()
"""

number_of_rows = int(input("Rows: "))
number_of_columns = int(input("Columns: "))
for i in range(number_of_rows):
    for j in range(number_of_columns):
        print(j, end=" ")
    print()
