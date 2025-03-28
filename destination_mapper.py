import re

def destination_mapper(input_string):
    # Regular expression to match valid locations
    pattern = r'([=/])([A-Za-z]{3,})\1'

    # Find all valid destinations using the pattern
    destinations = re.findall(pattern, input_string)

    # Extract only the names of the locations
    valid_destinations = [destination[1] for destination in destinations]

    # Calculate the total travel points (sum of the lengths of valid destinations)
    travel_points = sum(len(destination) for destination in valid_destinations)

    # Print the results
    print(f"Destinations: {', '.join(valid_destinations)}")
    print(f"Travel Points: {travel_points}")

# Example input
input_string = input()
destination_mapper(input_string)
