def process_message():
    # Read the initial concealed message
    message = input().strip()

    while True:
        # Read the next instruction line
        command = input().strip()

        if command == "Reveal":
            # When "Reveal" command is encountered, print the final message
            print(f"You have a new text message: {message}")
            break

        # Split the command based on ":|:"
        parts = command.split(":|:")

        if parts[0] == "InsertSpace":
            # InsertSpace:|:{index} -> Insert space at the given index
            index = int(parts[1])
            message = message[:index] + " " + message[index:]
            print(message)

        elif parts[0] == "Reverse":
            # Reverse:|:{substring} -> Reverse the first occurrence of the substring
            substring = parts[1]
            if substring in message:
                start_index = message.find(substring)
                message = message[:start_index] + message[start_index + len(substring):] + substring[::-1]
                print(message)
            else:
                print("error")

        elif parts[0] == "ChangeAll":
            # ChangeAll:|:{substring}:|:{replacement} -> Replace all occurrences of a substring
            substring = parts[1]
            replacement = parts[2]
            message = message.replace(substring, replacement)
            print(message)


# Run the function to process the instructions
process_message()
