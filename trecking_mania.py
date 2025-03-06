number_groups = int(input())

number_musala = 0
number_monblan = 0
number_kilimanjaro = 0
number_k2 = 0
number_everest = 0


for _ in range(number_groups):
    group_people = int(input())

    if group_people <= 5:
        number_musala += group_people
    elif group_people <= 12:
        number_monblan += group_people
    elif group_people <=25:
        number_kilimanjaro += group_people
    elif group_people <= 40:
        number_k2 += group_people
    else:
        number_everest += group_people

total_nuber = number_musala + number_monblan + number_kilimanjaro + number_k2 + number_everest

percent_musala = number_musala / total_nuber * 100
percent_monblan = number_monblan / total_nuber * 100
percent_kilimanjaro = number_kilimanjaro / total_nuber * 100
percent_k2 = (number_k2 / total_nuber * 100)
percent_everest = number_everest / total_nuber * 100

print(f'{percent_musala:.2f}%')
print(f'{percent_monblan:.2f}%')
print(f'{percent_kilimanjaro:.2f}%')
print(f'{percent_k2:.2f}%')
print(f'{percent_everest:.2f}%')


