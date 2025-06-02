N = int(input())

pumps = []
for _ in range(N):
    petrol, distance = map(int, input().split())
    pumps.append((petrol, distance))


def find_starting_pump(N, pumps):
    start = 0
    tank = 0
    total_petrol = 0

    for i in range(N):
        petrol, distance = pumps[i]
        tank += petrol - distance
        total_petrol += petrol - distance


        if tank < 0:
            start = i + 1
            tank = 0


    return start if start < N else 0


print(find_starting_pump(N, pumps))