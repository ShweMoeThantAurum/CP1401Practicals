"""CP1401 - Practical 8 - Debugging."""

# Debug program 1 - friends' names
names = ["Abby", "Jerome", "Olivia", "Monique"]
print("My friends' names: ")
for i in range(1, len(names)):
    print(f"{i}. {names[i]}")
last_number = len(names)
print(f"The last name (number {last_number}) is {names[last_number]}")

# Problem(s) for program 1:
# ?
# In the names list, there are four names but the code is showing only three names. So, to display all the list, the
# parameter "1" in the range function should be deleted. On the other hand, to show the numbers in order, +1 should be
# added after "i" in the line 7 print statement.
# For the last print statement, to print the last number name which matches with the last number, -1 is added after last
# number because the system will show "index out of range" if -1 is not added.
# Fixed code for program 1:
# names = ["Abby", "Jerome", "Olivia", "Monique"]
# print("My friends' names: ")
# for i in range(len(names)):
#     print(f"{i + 1}. {names[i]}")
# last_number = len(names)
# print(f"The last name (number {last_number}) is {names[last_number - 1]}")

# Debug program 2 - title-casing country names
countries = ("australia", "new zeaLAND", "India")
for i in range(len(countries)):
    countries[i] = countries[i].title()
print(countries)  # country names should be in title-case now

# Problem(s) for program 2:
# The countries is a tuple. The following codes are correct if the countries, which is the tuple type, is replaced with
# the list.

# Fixed code for program 2:
# countries = ["australia", "new zeaLAND", "India"]
# for i in range(len(countries)):
#     countries[i] = countries[i].title()
# print(countries)
