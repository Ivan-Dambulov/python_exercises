from collections import deque

green_duration = int(input())
free_window = int(input())

cars_queue = deque()
current_time = 0
cars_passed = 0

while True:
    command = input()
    if command == "END":
        print("Everyone is safe.")
        print(f"{cars_passed} total cars passed the crossroads.")
        break

    if command != "green":
        cars_queue.append(command)
    else:
        time_left = green_duration
        while time_left > 0 and cars_queue:
            car = cars_queue[0]
            if time_left >= len(car):
                cars_queue.popleft()
                cars_passed += 1
                time_left -= len(car)
                current_time += len(car)
            else:
                chars_passed = time_left
                current_time += time_left
                time_left = 0
                free_time = free_window
                while free_time > 0 and chars_passed < len(car):
                    chars_passed += 1
                    free_time -= 1
                    current_time += 1
                if chars_passed < len(car):
                    print("A crash happened!")
                    print(f"{car} was hit at {car[chars_passed]}.")
                    exit()
                else:
                    cars_queue.popleft()
                    cars_passed += 1
        current_time += time_left + free_window