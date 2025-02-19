def process_commands(initial_cards, commands):
    cards = initial_cards.split(", ") if initial_cards else []

    for command in commands:
        parts = command.split(", ")
        action = parts[0]

        if action == "Add":
            card_name = parts[1]
            if card_name in cards:
                print("Card is already in the deck")
            else:
                cards.append(card_name)
                print("Card successfully added")

        elif action == "Remove":
            card_name = parts[1]
            if card_name in cards:
                cards.remove(card_name)
                print("Card successfully removed")
            else:
                print("Card not found")

        elif action == "Remove At":
            index = int(parts[1])
            if 0 <= index < len(cards):
                cards.pop(index)
                print("Card successfully removed")
            else:
                print("Index out of range")

        elif action == "Insert":
            index = int(parts[1])
            card_name = parts[2]

            if 0 <= index <= len(cards):
                if card_name in cards:
                    print("Card is already added")
                else:
                    cards.insert(index, card_name)
                    print("Card successfully added")
            else:
                print("Index out of range")

    return ", ".join(cards)


initial_cards = input()
n = int(input())
commands = [input() for _ in range(n)]

result = process_commands(initial_cards, commands)
print(result)