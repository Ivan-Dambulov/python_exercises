locations = int(input())

sum_dug_gold = 0

for num_location in range(1, locations + 1):
    expected_average_dug = float(input())
    days = int(input())

    for num_days in range(1, days + 1):
        dug_gold = float(input())

        sum_dug_gold += dug_gold

    average_dug_gold = sum_dug_gold / days

    if average_dug_gold >= expected_average_dug:
        print(f"Good job! Average gold per day: {average_dug_gold:.2f}.")
        sum_dug_gold = 0
    else:
        print(f"You need {expected_average_dug - average_dug_gold:.2f} gold.")
        sum_dug_gold = 0