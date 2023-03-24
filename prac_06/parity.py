# Parity
"""
function main
    get number
    calculate print_parity(number)
    calculate get_parity(number)
    calculate is_odd
function print_parity(number)
    print "Parity of number"
function get_parity(number)
    return "Parity of number"
function is_odd(number)
    return "True" or "False"
"""


def main():
    number = int(input("Number: "))
    print_parity(number)
    reply = get_parity(number)
    odd_numbers = is_odd(number)
    print(reply)
    print(odd_numbers)


def print_parity(number):
    print(f"Parity of {number}: {number % 2}")


def get_parity(number):
    return number % 2


def is_odd(number):
    return number % 2 != 0


main()
