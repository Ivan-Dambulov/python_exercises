WIN_POINTS = 2000
FINAL_POINTS = 1200
SEMI_FINAL_POINTS = 720

number_tournaments = int(input())
starting_points = int(input())

total_point = 0
number_wins = 0

for _ in range(number_tournaments):
    stage = input()

    if stage == 'W':
        total_point += WIN_POINTS
        number_wins += 1
    elif stage == 'SF':
        total_point += SEMI_FINAL_POINTS
    elif stage == 'F':
        total_point += FINAL_POINTS

print(f'Final points: {starting_points + total_point}')
print(f'Average points: {total_point / number_tournaments}')
print(f'{number_wins / number_tournaments * 100:.2f}%')