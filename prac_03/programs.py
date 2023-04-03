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
    print "Hire refused"
if age<25
    print "Insurance required"
if age>=25
    print "Insurance not required"
"""

age = int(input("What is your age?"))
if age < 18:
    print("Hire refused")
if age < 25:
    print("Insurance required")
if age >= 25:
    print("Insurance not required")

# Simple Password Checker

"""
get password
if password = secret password
    print "Access granted"
else
    print "Access denied"
"""
SECRET_PASSWORD = "Python"
password = (input("Please type your password: "))
if password == SECRET_PASSWORD:
    print("Access granted")
else:
    print("Access denied")

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
    print "Invalid age"
else if age <18
    print "Think big about your future
else if age <60
    print "Work hard for your retirement
else if age <80
    print "Keep healthy, Stay Strong"
else if age <=120
    print "Wow, such an amazing age! Stay healthy"
"""

age = int(input("Please type your age here: "))
if age < 0 or age > 120:
    print("Invalid age")
elif age < 18:
    print("Think big about your future")
elif age < 60:
    print("Work hard for your retirement")
elif age < 80:
    print("Keep healthy, Stay Strong")
elif age <= 120:
    print("Wow, such an amazing age! Stay healthy")

# Speeding fines

"""
get speed_in_kilometers and speed_limit_in_kilometers
speed_over_the_limit= speed_limit_in_kilometers-speed_in_kilometers
if speed_over_the_limit_in_kilometers<13
    print "Your fine is $177."
else if speed_over_the_limit_in_kilometers<=20
    print "Your fine is $266."
else if speed_over_the_limit_in_kilometers<=30
    print "Your fine is $444."
else if speed_over_the_limit_in_kilometers<=40
    print "Your fine is $622."
else if speedlimit-speed_in_kilometers>40
    print "Your fine is $1245."
else:
    print "You are not fined."
"""

speed_in_kilometers = float(input("Please type your speed in kilometers: "))
speed_limit_in_kilometers = float(input("Please type your speed limit in kilometers: "))
speed_over_the_limit_in_kilometers = speed_in_kilometers - speed_limit_in_kilometers
if speed_over_the_limit_in_kilometers < 0:
    print("You are not fined.")
elif speed_over_the_limit_in_kilometers < 13:
    print("Your fine is $177.")
elif speed_over_the_limit_in_kilometers <= 20:
    print("Your fine is $266.")
elif speed_over_the_limit_in_kilometers <= 30:
    print("Your fine is $444.")
elif speed_over_the_limit_in_kilometers <= 40:
    print("Your fine is $622.")
else:
    print("Your fine is $1245.")

