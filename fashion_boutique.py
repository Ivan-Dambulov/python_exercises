clothes = [int(x) for x in input().split()]
capacity = int(input())

racks = 1  
current_sum = 0
stack = clothes[::-1]

while stack:
    cloth = stack.pop()
    if current_sum + cloth < capacity:
        current_sum += cloth
    elif current_sum + cloth == capacity:
        current_sum = 0
        if stack:
            racks += 1
    else:
        racks += 1
        current_sum = cloth

print(racks)