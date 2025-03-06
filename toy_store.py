PRICE_PUZZLE = 2.60
PRICE_SPEAKING_DOLL = 3
PRICE_TEDDY_BEAR = 4.10
PRICE_MINION = 8.20
PRICE_TRUCK = 2
DISCOUNT_THRESHOLD = 50
DISCOUNT_PERCENT = 0.25
RENT_PERCENT = 0.10

vacation_price = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_teddy_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

number_toys = number_puzzles + number_dolls + number_teddy_bears + number_minions + number_trucks
sum_toys = ((number_puzzles * PRICE_PUZZLE) + (number_dolls * PRICE_SPEAKING_DOLL)
                             + (number_teddy_bears * PRICE_TEDDY_BEAR) + (number_minions * PRICE_MINION)
                             + (number_trucks * PRICE_TRUCK))

if number_toys >= DISCOUNT_THRESHOLD:
    sum_toys -= (sum_toys * DISCOUNT_PERCENT)

sum_toys -= (sum_toys * RENT_PERCENT)

if sum_toys >= vacation_price:
    print(f'Yes! {sum_toys - vacation_price:.2f} lv left.')
else:
    print(f'Not enough money! {vacation_price - sum_toys:.2f} lv needed.')