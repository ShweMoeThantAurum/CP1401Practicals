# 1.Print a line
NUMBER_OF_HYPHENS = 40


def question_1():
    print("-" * NUMBER_OF_HYPHENS)


question_1()


# 2.Is it even?
def question_2():
    some_number = int(input("Number: "))
    if is_even(some_number):
        print(f"{some_number} is even")
    else:
        print(f"{some_number} is odd")


def is_even(some_number):
    """Determine whether some number is even or not."""
    return some_number % 2 == 0


question_2()


# 3.Get Non-empty String
def question_3():
    name = input("Name: ").title()
    birthplace = input("Birthplace: ").title()
    while name != "" and birthplace != "":
        print(f"Hi {name} from {birthplace}!")
        name = input("Name: ").title()
        birthplace = input("Birthplace: ").title()


question_3()


# 4.Number List
def question_4():
    numbers = []
    minimum_number = int(input("Minimum number: "))
    maximum_number = int(input("Maximum number: "))
    while maximum_number <= minimum_number:
        print(f"Your maximum must be greater than {minimum_number}")
        maximum_number = int(input("Maximum number: "))
    for i in range(minimum_number, maximum_number + 1):
        numbers.append(i)
    print(numbers)


question_4()


# 5.Subject List
def question_5():
    subject_codes = []
    subject_code = input("Enter subject code: ").upper()
    while subject_code != "":
        validation = validate_subject_code(subject_code)
        if validation is not False:
            subject_codes.append(subject_code)
        subject_code = input("Enter subject code: ").upper()
    if "CP1401" in subject_codes:
        result = "You are cool"
    else:
        result = ""
    print("You do these {} subjects:\n{}".format(len(subject_codes), '\n'.join(sorted(subject_codes))))
    print(f"{result}")


def validate_subject_code(subject_code):
    """Validate the subject code not to be invalid."""
    if len(subject_code) != 6:
        print("Invalid subject code")
        return False
    elif not subject_code[0].isalpha() and subject_code[1].isalpha():
        print("Invalid subject code")
        return False
    elif not subject_code[2:-1].isdigit():
        print("Invalid subject code")
        return False


question_5()
