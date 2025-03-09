num_kids = 0
num_adults = 0
money_for_toys = 0
money_for_sweaters = 0


while True:
    age_input = input()
    if age_input == "Christmas":
        break
    age = int(age_input)

    if age <= 16:
        num_kids += 1
        money_for_toys += 5
    else:
        num_adults += 1
        money_for_sweaters += 15


print(f"Number of adults: {num_adults}")
print(f"Number of kids: {num_kids}")
print(f"Money for toys: {money_for_toys}")
print(f"Money for sweaters: {money_for_sweaters}")
