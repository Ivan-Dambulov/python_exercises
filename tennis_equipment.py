import math

tennis_racket_price = float(input())
number_tennis_rackets = int(input())
number_tennis_shoes = int(input())


tennis_shoes_total_price = (tennis_racket_price / 6) * number_tennis_shoes
tennis_rackets_total_price = tennis_racket_price * number_tennis_rackets
other_equipment = (tennis_shoes_total_price + tennis_rackets_total_price) * 0.2
total_price = tennis_shoes_total_price + tennis_rackets_total_price + other_equipment

djokovic = math.floor(total_price / 8)
sponsors = math.ceil(total_price * 7 / 8)

print(f'Price to be paid by Djokovic {djokovic}')
print(f'Price to be paid by sponsors {sponsors:}')
