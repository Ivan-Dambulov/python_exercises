def process_sequence(initial_sequence):
    sequence = list(map(int, initial_sequence.split()))

    while True:
        command = input().strip()
        if command == "Finish":
            break

        parts = command.split()
        action = parts[0]

        if action == "Add":
            value = int(parts[1])
            sequence.append(value)

        elif action == "Remove":
            value = int(parts[1])
            if value in sequence:
                sequence.remove(value)

        elif action == "Replace":
            value = int(parts[1])
            replacement = int(parts[2])
            if value in sequence:
                index = sequence.index(value)
                sequence[index] = replacement

        elif action == "Collapse":
            threshold = int(parts[1])
            sequence = [x for x in sequence if x >= threshold]

    return " ".join(map(str, sequence))


# Get initial sequence
initial_sequence = input()
result = process_sequence(initial_sequence)
print(result)