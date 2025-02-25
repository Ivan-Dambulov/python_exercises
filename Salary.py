FACEBOOK = 150
INSTAGRAM = 100
REDDIT = 50

open_tabs = int(input())
salary = int(input())

result = ''

for _ in range(open_tabs):
    website = input()

    if website == 'Facebook':
        salary -= FACEBOOK
    elif website == 'Instagram':
        salary -= INSTAGRAM
    elif website == 'Reddit':
        salary -= REDDIT


    if salary <= 0:
        result = 'You have lost your salary.'
        break
else:
    result = salary

print(result)