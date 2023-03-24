# Example

"""
get original_price and surcharge_rate
extra_charge = original_price * surcharge_rate
total_price = original_price + extra_charge
display total_price
"""

original_price = float(input("Original price: $"))
surcharge_rate = float(input("Surcharge & (eg. 0.15 is 15%): "))
extra_charge = original_price*surcharge_rate
total_price = original_price+extra_charge
print(f"The total meal price is ${total_price}.")

