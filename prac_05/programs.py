# 1.Percentage change
"""get original, change
result= original + (original*change)
print result
"""

original = float(input("Original: "))
change = float(input("Change (eg. 5%= 0.05): "))
result = original + (original * change)
print(f"Result: {result}")

# 2. Time of day
"""
START_HOUR = 0
NOON_HOUR = 11
END_HOUR = 23
get time and coming or going
if time <= NOON_HOUR
    result_for_time = "before noon"
else
    result_for_time = "after noon"
if choice = "C"
    result_for_choice = "coming. Hi!"
else
    result_for_choice = "going. Bye!"
"""

START_HOUR = 0
NOON_HOUR = 11
END_HOUR = 23
time = int(input(f"The time of day ({START_HOUR}-{END_HOUR} hours): "))
choice = input(f"(C)oming or (G)oing: ").upper()
if time <= NOON_HOUR:
    result_for_time = "before noon"
else:
    result_for_time = "after noon"
if choice == "C":
    result_for_choice = "coming. Hi!"
else:
    result_for_choice = "going. Bye!"
print(f"It is {result_for_time} and you are {result_for_choice}")

# 3.Coffee orders
"""
COST_FOR_SMALL_SIZE = 3
COST_FOR_MEDIUM_SIZE = 4
COST_FOR_LARGE_SIZE = 5
COST_FOR_WRONG_SIZE = 5
get type_of_coffee and size
if size == "S"
    cost = COST_FOR_SMALL_SIZE
else if size == "M"
    cost = COST_FOR_MEDIUM_SIZE
else if size == "L"
    cost = COST_FOR_LARGE_SIZE
else
    cost = COST_FOR_WRONG_SIZE

if type_of_coffee == "B"
    print "You have to pay $cost."
else if type_of_coffee == "W"
    print "You have to pay $cost+1."
else
    print "You have to pay $cost+1."
"""

COST_FOR_SMALL_SIZE = 3
COST_FOR_MEDIUM_SIZE = 4
COST_FOR_LARGE_SIZE = 5
COST_FOR_WRONG_SIZE = 5
type_of_coffee = input(f"(W)hite or (B)lack coffee: ").upper()
size = input(f"(S)mall, (M)edium, (L)arge: ").upper()
if size == "S":
    cost = COST_FOR_SMALL_SIZE
elif size == "M":
    cost = COST_FOR_MEDIUM_SIZE
elif size == "L":
    cost = COST_FOR_LARGE_SIZE
else:
    cost = COST_FOR_WRONG_SIZE

if type_of_coffee == "B":
    print(f"You have to pay ${cost}.")
elif type_of_coffee == "W":
    print(f"You have to pay ${cost+1}.")
else:
    print(f"You have to pay ${cost+1}.")

# 4.Coffee orders with error-checking
"""
COST_FOR_SMALL_SIZE = 3
COST_FOR_MEDIUM_SIZE = 4
COST_FOR_LARGE_SIZE = 5
get type_of_coffee
while type_of_coffee != "B" and type_of_coffee != "W"
    print "There is no such coffee"
    get type_of_coffee
get size
while size != "S" and size != "M" and size != "L"
    print "Invalid size"
    get size
if size == "S"
    cost = COST_FOR_SMALL_SIZE
else if size == "M"
    cost = COST_FOR_MEDIUM_SIZE
else if size == "L"
    cost = COST_FOR_LARGE_SIZE

if type_of_coffee == "B"
    print "You have to pay $cost."
else if type_of_coffee == "W"
    print "You have to pay $cost+1."
"""

COST_FOR_SMALL_SIZE = 3
COST_FOR_MEDIUM_SIZE = 4
COST_FOR_LARGE_SIZE = 5
type_of_coffee = input(f"(W)hite or (B)lack coffee: ").upper()
while type_of_coffee != "B" and type_of_coffee != "W":
    print("There is no such coffee")
    type_of_coffee = input(f"(W)hite or (B)lack coffee: ").upper()
size = input(f"(S)mall, (M)edium, (L)arge: ").upper()
while size != "S" and size != "M" and size != "L":
    print("Invalid size")
    size = input(f"(S)mall, (M)edium, (L)arge: ").upper()

if size == "S":
    cost = COST_FOR_SMALL_SIZE
elif size == "M":
    cost = COST_FOR_MEDIUM_SIZE
elif size == "L":
    cost = COST_FOR_LARGE_SIZE
if type_of_coffee == "B":
    print(f"You have to pay ${cost}.")
else:
    print(f"You have to pay ${cost+1}.")

# 5. Accumulation
"""
total = 0
get low_value and high_value
while high_value < low_value
    print error message
    get high_value
for i in range (low_value, high_value +1)
    total = total + i
    print(i, end=" ")
print total
"""

total = 0
low_value = int(input("Low value: "))
high_value = int(input("High value: "))
while high_value < low_value:
    print("Type the high value that is actually higher than the low value.")
    high_value = int(input("High value: "))
for i in range(low_value, high_value+1,):
    total = total + i
    print(i, end=" ")
print(f"total: {total}")






