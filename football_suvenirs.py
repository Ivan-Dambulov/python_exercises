country = input()
suvenir = input()
broi_suveniri = int(input())

total_price = 0

if country == 'Argentina':
    if suvenir == 'flags':
        total_price += broi_suveniri * 3.25
    elif suvenir =='caps':
        total_price += broi_suveniri * 7.20
    elif suvenir == 'posters':
        total_price += broi_suveniri * 5.10
    elif suvenir == 'stickers':
        total_price += broi_suveniri * 1.25
    else:
        print('Invalid stock!')
        exit()

    print(f'Pepi bought {broi_suveniri} {suvenir} of {country} for {total_price:.2f} lv.')

elif country == 'Brazil':
    if suvenir == 'flags':
        total_price += broi_suveniri * 4.20
    elif suvenir == 'caps':
        total_price += broi_suveniri * 8.50
    elif suvenir == 'posters':
        total_price += broi_suveniri * 5.35
    elif suvenir == 'stickers':
        total_price += broi_suveniri * 1.20
    else:
        print('Invalid stock!')
        exit()

    print(f'Pepi bought {broi_suveniri} {suvenir} of {country} for {total_price:.2f} lv.')

elif country == 'Croatia':
    if suvenir == 'flags':
        total_price += broi_suveniri * 2.75
    elif suvenir == 'caps':
        total_price += broi_suveniri * 6.90
    elif suvenir == 'posters':
        total_price += broi_suveniri * 4.95
    elif suvenir == 'stickers':
        total_price += broi_suveniri * 1.10
    else:
        print('Invalid stock!')
        exit()

    print(f'Pepi bought {broi_suveniri} {suvenir} of {country} for {total_price:.2f} lv.')

elif country == 'Denmark':
    if suvenir == 'flags':
        total_price += broi_suveniri * 3.10
    elif suvenir == 'caps':
        total_price += broi_suveniri * 6.50
    elif suvenir == 'posters':
        total_price += broi_suveniri * 4.80
    elif suvenir == 'stickers':
        total_price += broi_suveniri * 0.90
    else:
        print('Invalid stock!')
        exit()



    print(f'Pepi bought {broi_suveniri} {suvenir} of {country} for {total_price:.2f} lv.')

else:
    print('Invalid country!')


