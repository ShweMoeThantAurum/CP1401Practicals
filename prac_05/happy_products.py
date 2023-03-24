# All Together Now
"""
DISCOUNT_RATE = 0.1 # 10%
display menu
get choice
while choice != "Q"
    if choice == "I"
        print instructions
    else if choice == "C"
        get number_of_products
        while number_of_products <= 0
            print "Invalid input"
            get number_of_products
        get price
        if number_of_products <=5
            total_cost = number_of_products * price
        else:
            total_cost = number_of_products * (price-(price * DISCOUNT_RATE)
        print total_cost
    else
        print "Invalid Choice"
    print menu
    get choice
print "Farewell"
"""
DISCOUNT_RATE = 0.1  # 10%
MENU = "Menu:\n(I)nstructions\n(C)alculate\n(Q)uit"
print(MENU)
choice = input("Choice: ").upper()
while choice != "Q":
    if choice == "I":
        print("Enter the number of products you want to buy and your chosen price.\nIf you buy 0-5 items, "
              "they're full price, over 5 items and each one is 10% off!")
    elif choice == "C":
        number_of_products = int(input("Number of products: "))
        while number_of_products < 0:
            print("Invalid input")
            number_of_products = int(input("Number of products: "))
        price = float(input("Price: "))
        if number_of_products <= 5:
            total_cost = number_of_products*price
        else:
            total_cost = number_of_products * (price - (price * DISCOUNT_RATE))
        print(f"{number_of_products} * ${price} products = {total_cost:,.2f}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input("Choice: ").upper()
print("Farewell")
