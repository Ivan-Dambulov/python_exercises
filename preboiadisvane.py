from math import floor, ceil

broi_kutii_boia = int(input())
broi_rolki = int(input())
price_chift_rukavici = float(input())
price_chetka = float(input())

PAINT = 21.50
ROLKA_TAPETI = 5.20
BROI_RUKAVICI = ceil(broi_rolki * 0.35)
BROI_CHETKI = floor(broi_kutii_boia * 0.48)


total_price = ((broi_kutii_boia * PAINT) + (broi_rolki * ROLKA_TAPETI) + (BROI_CHETKI * price_chetka)
               + (BROI_RUKAVICI * price_chift_rukavici))





print(f'This delivery will cost {total_price / 15:.2f} lv.')