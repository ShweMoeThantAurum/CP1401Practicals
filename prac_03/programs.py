# Tax

"""
get income
if income <100
    total_tax= 0
else if income <=500
    total_tax= income*2%
else if income <=1000
    total_tax= income*5%
else
    total_tax= income*10%
take_home_pay= income-total_tax
print total_tax is
print take_home_pay is
"""
print("Python Party Tax Program - Where Tax is a Party")
TAX_RATE_LOW = 0.05  # 5%
TAX_RATE_MIDDLE = 0.02  # 2%
TAX_RATE_HIGH = 0.1  # 10%
TAX_THRESHOLD_LOW = 100
TAX_THRESHOLD_MIDDLE = 500
TAX_THRESHOLD_HIGH = 1000
income = float(input("Income: $"))
if income < TAX_THRESHOLD_LOW:
    total_tax = 0
elif income <= TAX_THRESHOLD_MIDDLE:
    total_tax = income * TAX_RATE_MIDDLE
elif income <= TAX_THRESHOLD_HIGH:
    total_tax = income * TAX_RATE_LOW
else:
    total_tax = income * TAX_RATE_HIGH
take_home_pay = income - total_tax
print(f"Total tax is: $ {total_tax}.")
print(f"Take home pay is: $ {take_home_pay}.")

# Car Insurance

"""
get applicant's age
if age<18
    result = "Hire refused"
else if age<25
    result = "Insurance required"
else 
    result = "Insurance not required"
print result
"""

age = int(input("What is your age?"))
if age < 18:
    result = "Hire refused"
elif age < 25:
    result = "Insurance required"
else:
    result = "Insurance not required"
print(result)

# Simple Password Checker

"""
get password
if password = secret password
    message = "Access granted"
else
    message = "Access denied"
print message
"""

SECRET_PASSWORD = "Python"
password = (input("Please type your password: "))
if password == SECRET_PASSWORD:
    message = "Access granted"
else:
    message = "Access denied"
print(message)

# Dog Years

"""
get age in human years
if age in human years<=2
    age in dog years= age in human years*10.5
else
    age in dog years= 21 + (age in human years-2)*4
print age in dog years is
"""

HUMAN_YEARS_TO_DOG_YEARS_CONVERSION_RATE_FOR_FIRST_TWO_YEARS = 10.5  # Each year of the first two human years is equal
# to 10.5 dog years.
HUMAN_YEARS_TO_DOG_YEARS_CONVERSION_RATE_AFTER_FIRST_TWO_YEARS = 4  # After first two years, each human year equals 4
# dog years.
HUMAN_YEARS_TO_DOG_YEARS_CONVERTED_VALUE_FOR_FIRST_TWO_YEARS = 21  # The converted value of human years to dog years
# for first two years.
FIRST_TWO_YEARS = 2
age_in_human_years = int(input("Age in human years: "))
if age_in_human_years <= 2:
    age_in_dog_years = age_in_human_years * HUMAN_YEARS_TO_DOG_YEARS_CONVERSION_RATE_FOR_FIRST_TWO_YEARS
else:
    age_in_dog_years = HUMAN_YEARS_TO_DOG_YEARS_CONVERTED_VALUE_FOR_FIRST_TWO_YEARS + (
                age_in_human_years - FIRST_TWO_YEARS) * HUMAN_YEARS_TO_DOG_YEARS_CONVERSION_RATE_AFTER_FIRST_TWO_YEARS
print(f"Age in dog years is {age_in_dog_years}")

# Rock of Ages

"""
get age
if age <0 or age>120
    message = "Invalid age"
else if age <18
    message = "Think big about your future
else if age <60
    message = "Work hard for your retirement
else if age <80
    message = "Keep healthy, Stay Strong"
else
    message = "Wow, such an amazing age! Stay healthy"
print message
"""

age = int(input("Please type your age here: "))
if age < 0 or age > 120:
    message = "Invalid age"
elif age < 18:
    message = "Think big about your future"
elif age < 60:
    message = "Work hard for your retirement"
elif age < 80:
    message = "Keep healthy, Stay Strong"
else:
    message = "Wow, such an amazing age! Stay healthy"
print(message)

# Speeding fines

"""
get speed_in_kilometers and speed_limit_in_kilometers
speed_over_the_limit= speed_limit_in_kilometers-speed_in_kilometers
if speed_over_the_limit_in_kilometers<0
    penalty_amount = 0
else if speed_over_the_limit_in_kilometers<13
    penalty_amount = 177
else if speed_over_the_limit_in_kilometers<=20
    penalty_amount = 266
else if speed_over_the_limit_in_kilometers<=30
    penalty_amount = 444
else if speed_over_the_limit_in_kilometers<=40
    penalty_amount = 622
else speedlimit-speed_in_kilometers>40
    penalty_amount = 1245
print penalty_amount
"""

speed_in_kilometers = float(input("Please type your speed in kilometers: "))
speed_limit_in_kilometers = float(input("Please type your speed limit in kilometers: "))
speed_over_the_limit_in_kilometers = speed_in_kilometers - speed_limit_in_kilometers
if speed_over_the_limit_in_kilometers < 0:
    penalty_amount = 0
elif speed_over_the_limit_in_kilometers < 13:
    penalty_amount = 177
elif speed_over_the_limit_in_kilometers <= 20:
    penalty_amount = 266
elif speed_over_the_limit_in_kilometers <= 30:
    penalty_amount = 444.
elif speed_over_the_limit_in_kilometers <= 40:
    penalty_amount = 622
else:
    penalty_amount = 1245
print(f"Your penalty amount is ${penalty_amount}.")

