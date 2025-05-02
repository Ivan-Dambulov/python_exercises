from collections import deque

# Input parsing
bees = deque(map(int, input().split()))
bee_eaters = list(map(int, input().split()))  # We need list to control insert positions

while bees and bee_eaters:
    bee_group = bees.popleft()
    eater_index = len(bee_eaters) - 1
    eater_group = bee_eaters.pop()

    total_bee_kill = eater_group * 7

    if bee_group > total_bee_kill:
        # Bees win
        surviving_bees = bee_group - total_bee_kill
        bees.append(surviving_bees)
    elif total_bee_kill > bee_group:
        # Bee-eaters win — calculate how many survived
        bees_killed = 0
        survivors = 0
        for i in range(eater_group):
            if bees_killed + 7 <= bee_group:
                bees_killed += 7
            else:
                survivors = eater_group - i
                break
        if survivors > 0:
            # Return survivors to original position
            bee_eaters.insert(eater_index, survivors)
    # Else draw — both groups are eliminated

# Final Output
print("The final battle is over!")
if not bees and not bee_eaters:
    print("But no one made it out alive!")
elif bees:
    print("Bee groups left: " + ", ".join(map(str, bees)))
elif bee_eaters:
    print("Bee-eater groups left: " + ", ".join(map(str, bee_eaters)))
