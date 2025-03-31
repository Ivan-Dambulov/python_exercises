def process_string_commands():
    string = input()

    while True:
        command = input()
        if command == "End":
            break

        parts = command.split()
        action = parts[0]

        if action == "Translate":
            char, replacement = parts[1], parts[2]
            string = string.replace(char, replacement)
            print(string)

        elif action == "Includes":
            substring = parts[1]
            print(str(substring in string))

        elif action == "Start":
            substring = parts[1]
            print(str(string.startswith(substring)))

        elif action == "Lowercase":
            string = string.lower()
            print(string)

        elif action == "FindIndex":
            char = parts[1]
            print(string.rindex(char))

        elif action == "Remove":
            start_index = int(parts[1])
            count = int(parts[2])
            string = string[:start_index] + string[start_index + count:]
            print(string)


process_string_commands()