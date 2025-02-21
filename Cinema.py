PREMIER = 12
NORMAL = 7.50
DISCOUNT = 5

screening_type = input()
rows = int(input())
columns = int(input())

income = 0

cinema_capacity = rows * columns

if screening_type == 'Premiere':
    income += cinema_capacity * PREMIER
elif screening_type == 'Normal':
    income += cinema_capacity * NORMAL
elif screening_type == 'Discount':
    income += cinema_capacity * DISCOUNT

print(f'{income:.2f} leva')