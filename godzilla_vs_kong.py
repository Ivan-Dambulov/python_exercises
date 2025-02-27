DECOR_PERCENT = 0.10
DISCOUNT_THRESHOLD = 150
DISCOUNT_PERCENT = 0.10


budget = float(input())
number_people = int(input())
price_cloathing_per_person = float(input())

sum_decor = budget * DECOR_PERCENT
clothes_price = number_people * price_cloathing_per_person

if number_people > DISCOUNT_THRESHOLD:
   clothes_price -= (clothes_price * DISCOUNT_PERCENT)

total_sum = sum_decor + clothes_price

if total_sum > budget:
    print('Not enough money!')
    print(f'Wingard needs {total_sum - budget:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {budget - total_sum:.2f} leva left.')