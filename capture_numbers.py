import re

# List to store the numbers
numbers = []

# Receive input from the user until an empty line is entered
while True:
    line = input()

    if line == "":
        break

    # Use regular expression to find all numbers in the current line
    found_numbers = re.findall(r'\d+', line)

    # Append the found numbers to the list
    numbers.extend(found_numbers)

# Print all extracted numbers in a single line, separated by a space
print(" ".join(numbers))
