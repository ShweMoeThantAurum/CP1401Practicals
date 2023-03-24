# Example

"""
places = empty list
get place
while place is not empty
    add place to places
    get place
if len(places) > 0
    print "On my holiday, I went to: "
    longest_place = empty string
    for place in places
        print place
        if len(place) > len(longest_place)
            longest_place = place
    print "The place with the longest name was {longest_place}."
else:
    print "I went nowhere."
"""

places = []
place = input("Place: ").title()
while place != "":
    places.append(place)
    place = input("Place: ").title()
if len(places) > 0:
    print("On my holiday, I went to: ")
    longest_place = ""
    for place in places:
        print(place)
        if len(place) > len(longest_place):
            longest_place = place
    print(f"The place with the longest name was {longest_place}.")
else:
    print("I went nowhere.")
