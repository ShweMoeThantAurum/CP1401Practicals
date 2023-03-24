# 1.Discount Price
"""
get original_price
discount = original_price * 0.2
new_price = original_price – discount
print new_price
"""

DISCOUNT_RATE = 0.2
original_price = float(input("Original price:$ "))
discount = original_price * DISCOUNT_RATE
new_price = original_price - discount
print(f"The final price is ${new_price}")

# 2.Kilometres to miles
"""
get distance in kilometres
converted_distance= distance in kilometres*0.621371
print converted_distance 
"""
KILOMETRE_TO_MILES_CONVERSION_RATE = 0.621371
distance_in_kilmetres = float(input("Please type your distance in kilometres: "))
converted_distance = distance_in_kilmetres*KILOMETRE_TO_MILES_CONVERSION_RATE
print(f"Your distance in miles is {converted_distance} miles.")

# 3 Holiday Cost
"""
get daily food cost, daily activities cost, number of days
total cost= (daily food cost+ daily activities cost+ 75)*number of days
print total cost
"""

HOTEL_COST_PER_DAY = 75
daily_food_cost = float(input("Daily food cost:$ "))
daily_activities_cost = float(input("Daily activities cost:$ "))
number_of_days = int(input("Number of days: "))
total_cost = (HOTEL_COST_PER_DAY+daily_food_cost+daily_activities_cost)*number_of_days
print(f"The trip will cost ${total_cost}.")

# 4 Deep Sleep Calculation
"""
get total sleep in seconds
get deep sleep in seconds
total sleep in minutes_m= total sleep in seconds//60
total sleep in minutes_s= total sleep in seconds%60
deep sleep in minutes_m= deep sleep in seconds//60
deep sleep in minutes_s= deep sleep in seconds%60
percentage= (deep sleep in seconds/total sleep in seconds)* 100
print total sleep in minutes, deep sleep in minutes, percentage
"""
SECONDS_PER_MINUTE = 60
PERCENTAGE = 100
total_sleep_in_seconds = int(input("Your total sleep in seconds is: "))
deep_sleep_in_seconds = int(input("Your deep sleep in seconds is: "))
total_sleep_in_minutes_m = total_sleep_in_seconds//SECONDS_PER_MINUTE
total_sleep_in_minutes_s = total_sleep_in_seconds % SECONDS_PER_MINUTE
deep_sleep_in_minutes_m = deep_sleep_in_seconds//SECONDS_PER_MINUTE
deep_sleep_in_minutes_s = deep_sleep_in_seconds % SECONDS_PER_MINUTE
percentage = (deep_sleep_in_seconds/total_sleep_in_seconds)*PERCENTAGE
print(f"Deep sleep: {deep_sleep_in_minutes_m}m {deep_sleep_in_minutes_s}s")
print(f"Total sleep: {total_sleep_in_minutes_m}m {total_sleep_in_minutes_s}s")
print(f"Percentage: {percentage}%")
