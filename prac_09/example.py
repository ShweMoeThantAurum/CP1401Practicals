# Files Example

"""
FILENAME = "scores.txt"
total = 0.0
count = 0
open "FILENAME" for reading as in_file
for line in in_file
    score = line as float
    total = total + score
    count = count + 1
    print scores and total so far
close in_file
print average
"""

FILENAME = "scores.txt"
total = 0.0
count = 0
in_file = open(FILENAME, "r")
for line in in_file:
    score = float(line)
    total = total + score
    count = count + 1
    print(f"Score = {score} \t Total so far = {total:,.1f}", sep=" ")
in_file.close()
print(f"Average = {total/count:,.1f}")
