# Calculate salary for worker level
"""
function main
    get worker level
     print calculate_salary(worker_level)
function calculate_salary(worker_level)
    SALARY_RATE = 5000
    salary = worker_level * SALARY_RATE
    return salary
"""


def main():
    worker_level= int(input("Worker level: "))
    while worker_level < 1 or worker_level > 10:
        print("Invalid worker level")
        worker_level = int(input("Worker level: "))
    print(calculate_salary(worker_level))


def calculate_salary(worker_level):
    SALARY_RATE = 5000
    salary = worker_level * SALARY_RATE
    return f"With worker level {worker_level}, your salary is ${salary:,.2f}."


# main()


# Print grid(rows, columns)
"""
function main 
    get number_of_rows
    get number_of_columns
    for i in range(number_of_rows)
        for j in range(number_of_columns)
            print(j, end=" ")
        print()
"""


def main():
    number_of_rows = int(input("Rows: "))
    number_of_columns = int(input("Columns: "))
    for i in range(number_of_rows):
        for j in range(number_of_columns):
            print(j, end=" ")
        print()


# main()
