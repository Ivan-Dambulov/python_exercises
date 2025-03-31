def is_valid(message):
    if "!:" not in message or message.count("!") < 2:
        return False

    command_part = message.split("!:")[0] + "!"
    if len(command_part) < 4:
        return False

    command = command_part[1:-1]
    if not (command[0].isupper() and command[1:].islower() and command.isalpha()):
        return False

    if "[" not in message or "]" not in message:
        return False

    string_start = message.find("[")
    string_end = message.find("]")
    if string_start >= string_end:
        return False

    string_part = message[string_start + 1:string_end]

    if len(string_part) < 8:
        return False

    if not all(char.isalpha() or char.isspace() for char in string_part):
        return False

    return command, string_part


def translate_string(string):
    ascii_values = [str(ord(char)) for char in string]
    return " ".join(ascii_values)


def main():
    n = int(input())

    for _ in range(n):
        message = input()
        validation_result = is_valid(message)

        if validation_result:
            command, string_part = validation_result
            translated = translate_string(string_part)
            print(f"{command}: {translated}")
        else:
            print("The message is invalid")


if __name__ == "__main__":
    main()