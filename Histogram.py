n = int(input())

number_p1 = 0
number_p2 = 0
number_p3 = 0
number_p4 = 0
number_p5 = 0

for _ in range(n):
    number = int(input())

    if number < 200:
        number_p1 += 1
    elif 200 <= number < 400:
        number_p2 += 1
    elif 400 <= number < 600:
        number_p3 += 1
    elif 600 <= number < 800:
        number_p4 += 1
    else:
        number_p5 += 1

number_p = number_p1 + number_p2 + number_p3 + number_p4 + number_p5

percent_p1 = number_p1 / number_p * 100
percent_p2 = number_p2 / number_p * 100
percent_p3 = number_p3 / number_p * 100
percent_p4 = number_p4 / number_p * 100
percent_p5 = number_p5 / number_p * 100

print(f'{percent_p1:.2f}%')
print(f'{percent_p2:.2f}%')
print(f'{percent_p3:.2f}%')
print(f'{percent_p4:.2f}%')
print(f'{percent_p5:.2f}%')
