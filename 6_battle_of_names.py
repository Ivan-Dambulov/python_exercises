# Read number of names
N = int(input())

odd_set = set()
even_set = set()

# Process each name
for row in range(1, N + 1):
    name = input()
    # Sum ASCII values of letters in name
    ascii_sum = sum(ord(char) for char in name)
    # Integer divide by row number
    result = ascii_sum // row
    # Add to appropriate set
    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

# Calculate sums
odd_sum = sum(odd_set)
even_sum = sum(even_set)

# Determine output based on sums
if odd_sum == even_sum:
    # Print union of sets
    print(", ".join(str(x) for x in odd_set.union(even_set)))
elif odd_sum > even_sum:
    # Print difference (odd_set - even_set)
    print(", ".join(str(x) for x in odd_set.difference(even_set)))
else:
    # Print symmetric difference
    print(", ".join(str(x) for x in odd_set.symmetric_difference(even_set)))