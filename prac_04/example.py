MINIMUM_MONTH = 1
MAXIMUM_MONTH = 10
MIDDLE_MONTH = 5
birth_month = int(input(f"Enter the month number ({MINIMUM_MONTH}-{MAXIMUM_MONTH}): "))
while birth_month < MINIMUM_MONTH or birth_month > MAXIMUM_MONTH:
    print("Invalid month")
    birth_month = int(input("Enter your birth month: "))

if birth_month <= MIDDLE_MONTH:
    result = "the first half of the year"
else:
    result = "the second half of the year"
print(f"The birth month is in {result}.")

for count in range(1, birth_month + 1):
    print(count, end=" ")
print()
