BROTHER = 1
INCREASE_MONEY_FOR_BIRTH = 10

ages = int(input())
price_washing_machine = float(input())
unit_price = int(input())

birth_money = 10
count_toys = 0
total_money = 0

for year in range(1, ages + 1):

    if year % 2 == 0:
        total_money += (birth_money - BROTHER)
        birth_money += INCREASE_MONEY_FOR_BIRTH

    else:
        count_toys += 1


total_money += (count_toys * unit_price)

if total_money >= price_washing_machine:
    print(f'Yes! {total_money - price_washing_machine:.2f}')
else:
    print(f'No! {price_washing_machine - total_money:.2f}')