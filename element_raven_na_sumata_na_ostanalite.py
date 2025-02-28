n = int(input())


sum_numbers = 0
max_number = float('-inf')

for num in range(n):
    number = int(input())

    if number > max_number:
        max_number = number

    sum_numbers += number

half_sum = sum_numbers - max_number

if half_sum == max_number:
    print(f'Yes\nSum = {max_number}')
else:
    print(f'No\nSum = {max_number}')