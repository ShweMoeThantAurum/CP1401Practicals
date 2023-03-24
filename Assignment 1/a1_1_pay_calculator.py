"""
CP1401 2022-3 Assignment 1
Program 1 - Pay Calculator
Student Name: <Shwe Moe Thant>
Date Started: <6.12.2022>
"""
# Pay Calculator

"""
LEVEL_ZERO_PAY_RATE = 45.00
PAY_RATE_PER_LEVEL= 5%
get number_of_hours_worked and experience_level
hourly_pay_rate= LEVEL_ZERO_PAY_RATE + (LEVEL_ZER0_PAY_RATE * experience_level)
total_pay= number_of_hours_worked * hourly_pay_rate
print total_pay
"""

LEVEL_ZERO_PAY_RATE = 45.00
PAY_RATE_PER_LEVEL = 0.05 # 5%
number_of_hours_worked = int(input("Number of hours worked: "))
experience_level = int(input("Experience level: "))
hourly_pay_rate = LEVEL_ZERO_PAY_RATE + ((experience_level * LEVEL_ZERO_PAY_RATE) * PAY_RATE_PER_LEVEL)
total_pay = number_of_hours_worked*hourly_pay_rate
print(f"Based on your experience level ({experience_level}): ")
print(f"Your hourly pay rate is ${hourly_pay_rate}")
print(f"Your total pay is ${total_pay:,.2f}.")
