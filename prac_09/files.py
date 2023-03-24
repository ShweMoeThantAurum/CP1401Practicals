# 4. Read a String from a File

FILENAME = "name.txt"
in_file = open(FILENAME, "r")
text = in_file.read()
print(f"Greetings {text}!")
in_file.close()

# 5. Greater-Than Counter

FILENAME = "recentrain.txt"
greater_numbers = []
threshold = float(input("Threshold: "))
count = 0
in_file = open(FILENAME, "r")
for line in in_file:
    if float(line) > threshold:
        greater_numbers.append(float(line))
    count = count + 1
print(f"{len(greater_numbers)} out of {count} ({(len(greater_numbers)/count)*100}%) values in {FILENAME} "
      f"are greater than {threshold}.")

# 6. File Filter

input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")
search_string = input("Enter the search string: ")
in_file = open(input_file, "r")
out_file = open(output_file, "w")
for line in in_file:
    if search_string in line:
        out_file.write(line)
in_file.close()
out_file.close()

# 6. Optional - Version 2
input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")
in_file = open(input_file, "r")
out_file = open(output_file, "w")
for line in in_file:
    if line[0] in ["a", "e", "i", "o", "u"]:
        out_file.write(line)
in_file.close()
out_file.close()


