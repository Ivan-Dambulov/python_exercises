gradusi = int(input())
time_of_day = input()
outfit = ""
shoes = ""

if time_of_day == 'Morning':
    if 10 <= gradusi <= 18:
        outfit += 'Sweatshirt'
        shoes += 'Sneakers'
    elif 18 < gradusi <= 24:
        outfit += 'Shirt'
        shoes += 'Moccasins'
    elif gradusi >= 25:
        outfit += 'T-Shirt'
        shoes += 'Sandals'


if time_of_day == 'Afternoon':
    if 10 <= gradusi <= 18:
        outfit += 'Shirt'
        shoes += 'Moccasins'
    elif 18 < gradusi <= 24:
        outfit += 'T-Shirt'
        shoes += 'Sandals'
    elif gradusi >= 25:
        outfit += 'Swim Suit'
        shoes += 'Barefoot'


if time_of_day == 'Evening':
    if 10 <= gradusi <= 18:
        outfit += 'Shirt'
        shoes += 'Moccasins'
    elif 18 < gradusi <= 24:
        outfit += 'Shirt'
        shoes += 'Moccasins'
    elif gradusi >= 25:
        outfit += 'Shirt'
        shoes += 'Moccasins'


print(f'It\'s {gradusi} degrees, get your {outfit} and {shoes}.')