MIN_POINT = 1250.5

actor_name = input()
starting_points = float(input())
number_judges = int(input())

result = None

for i in range(number_judges):
    judge_name = input()
    judge_points = float(input())

    starting_points += (len(judge_name) * judge_points / 2)

    if starting_points > MIN_POINT:
        result = f'Congratulations, {actor_name} got a nominee for leading role with {starting_points:.1f}!'
        break
else:
    result = f'Sorry, {actor_name} you need {MIN_POINT - starting_points:.1f} more!'

print(result)