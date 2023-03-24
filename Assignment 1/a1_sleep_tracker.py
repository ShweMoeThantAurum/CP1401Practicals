"""
CP1401 2022-3 Assignment 1
Program 1 - Pay Calculator
Student Name: <Shwe Moe Thant>
Date Started: <6.12.2022>
"""
# Sleep Tracker

"""
MINIMUM_HOURS_SLEEP = 0
MAXIMUM_HOURS_SLEEP = 24
PERIODS = 5
DESIRABLE_HOURS_PER_DAY = 8
TOTAL_DESIRABLE_HOURS_OF_SLEEP = PERIODS * DESIRABLE_HOURS_PER_DAY
total_hours_sleep = 0
for i in range(1, PERIODS+1)
    get hours_sleep_per_day
    while hours_sleep_per_day < MINIMUM_HOURS_SLEEP or hours_sleep_per_day > MAXIMUM_HOURS_SLEEP
        print "Invalid number of hours."
        get hours_sleep_per_day
    total_hours_sleep =total_hours_sleep + hours_sleep_per_day
print total_hours_sleep
if total_hours_sleep <40
    sleep_debt= TOTAL_DESIRABLE_HOURS_OF_SLEEP - total_hours_sleep
    print sleep_debt
else
    print "You are getting enough sleep. Keep it up!"
"""

# I choose to use "for loop" because the count for the period is definite. I used "nested while loop" to check error.

print("Sleep Tracker")
MINIMUM_HOURS_OF_SLEEP = 0.00
MAXIMUM_HOURS_OF_SLEEP = 24.00
PERIODS = 5
DESIRABLE_HOURS_SLEEP_PER_DAY = 8
TOTAL_DESIRABLE_HOURS_OF_SLEEP = PERIODS*DESIRABLE_HOURS_SLEEP_PER_DAY  # 5*8
total_hours_sleep = 0
for i in range(1, PERIODS+1):
    hours_sleep_per_day = float(input(f"Night {i} hours sleep: "))
    while hours_sleep_per_day < 0 or hours_sleep_per_day > 24:
        print("Invalid number of hours.")
        hours_sleep_per_day = float(input(f"Night {i} hours sleep: "))
    total_hours_sleep = total_hours_sleep + hours_sleep_per_day
print(f"Recommended total sleep is: {TOTAL_DESIRABLE_HOURS_OF_SLEEP}")
print(f"Your total hours of sleep : {total_hours_sleep}")
if total_hours_sleep < 40:
    sleep_debt = TOTAL_DESIRABLE_HOURS_OF_SLEEP - total_hours_sleep
    print(f"Your sleep debt over this time is: {sleep_debt}")
else:
    print(f"You are getting enough sleep. Keep it up!")
