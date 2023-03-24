# 1. Processing Strings

data_strings = ["Result = 95%", "Final Score = 8%", "Relative Value = 178%",
                "Something else that's very important = 9.2%", "x = 42%"]
for string in data_strings:
    value = float(string[string.find("=") + 1: -1])
    print(value)

# 2. Date Strings

CURRENT_YEAR = 2023
date_of_birth = input("DOB: ")
birth_year = int(date_of_birth[-4:len(date_of_birth)])
print(f"You were born in {birth_year}.")
print(f"You will turn {CURRENT_YEAR - birth_year} in {CURRENT_YEAR}.")

# 3. Subject Code Strings

subject_code = input("Enter subject code: ").upper()
while subject_code != "":
    if subject_code[2] == "1":
        year_level = "first"
    elif subject_code[2] == "2":
        year_level = "second"
    elif subject_code[2] == "3":
        year_level = "third"
    else:
        year_level = "Masters or other"

    if subject_code[0:2] == "CP":
        subject_type = "IT"
    elif subject_code[0:2] == "MA":
        subject_type = "Maths"
    else:
        subject_type = " "
    print(f"This is a {year_level}-year {subject_type} subject.")
    subject_code = input("Enter subject code: ").upper()

