# 1. Random numbers

"""
import random
numbers = empty list
random_number = int(input("How many random numbers: "))
maximum_number = int(input("Maximum number: "))
for i in range(random_number)
    numbers.append(random.randint(0, maximum_number))
print(f"The numbers are: {numbers}")
print(f"The minimum is {min(numbers)}")
print(f"The maximum is {max(numbers)}")
print(f"A randomly chosen number is {random.choice(numbers)}")
print(f"The numbers reversed are {list(reversed(numbers))}")
print(f"The numbers sorted are {sorted(numbers)}")
"""

import random
numbers = []
random_number = int(input("How many random numbers: "))
maximum_number = int(input("Maximum number: "))
for i in range(random_number):
    numbers.append(random.randint(0, maximum_number))
print(f"The numbers are: {numbers}")
print(f"The minimum is {min(numbers)}")
print(f"The maximum is {max(numbers)}")
print(f"A randomly chosen number is {random.choice(numbers)}")
print(f"The numbers reversed are {list(reversed(numbers))}")
print(f"The numbers sorted are {sorted(numbers)}")

