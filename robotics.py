from collections import deque
from datetime import datetime, timedelta

robots_input = input().split(';')
robots = []
for robot in robots_input:
    name, time = robot.split('-')
    robots.append({'name': name, 'process_time': int(time), 'busy_until': 0})

start_time = datetime.strptime(input(), '%H:%M:%S')

products = deque()
while True:
    product = input()
    if product == 'End':
        break
    products.append(product)

seconds = 1
while products:
    current_time = start_time + timedelta(seconds=seconds)
    current_time_seconds = seconds

    assigned = False
    for robot in robots:
        if robot['busy_until'] <= current_time_seconds and products:
            product = products.popleft()
            print(f"{robot['name']} - {product} [{current_time.strftime('%H:%M:%S')}]")
            robot['busy_until'] = current_time_seconds + robot['process_time']
            assigned = True
            break

    if not assigned and products:
        product = products.popleft()
        products.append(product)

    seconds += 1