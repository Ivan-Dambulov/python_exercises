def process_sequences():
    # Read input sequences
    first_seq = set(map(int, input().split()))  # Convert to set for unique values
    second_seq = set(map(int, input().split()))

    # Read number of commands
    n = int(input())

    # Process commands
    for _ in range(n):
        command = input().split()
        action = command[0] + " " + command[1]  # e.g., "Add First"
        numbers = list(map(int, command[2:])) if len(command) > 2 else []

        if action == "Add First":
            first_seq.update(numbers)  # Add numbers, set ensures uniqueness
        elif action == "Add Second":
            second_seq.update(numbers)
        elif action == "Remove First":
            first_seq.difference_update(numbers)  # Remove numbers if they exist
        elif action == "Remove Second":
            second_seq.difference_update(numbers)
        elif action == "Check Subset":
            # Check if one sequence is a subset of the other
            is_subset = first_seq.issubset(second_seq) or second_seq.issubset(first_seq)
            print("True" if is_subset else "False")

    # Prepare final output
    sorted_first = " ".join(map(str, sorted(first_seq)))
    sorted_second = " ".join(map(str, sorted(second_seq)))
    print(f"{sorted_first}, {sorted_second}")


# Run the program
process_sequences()