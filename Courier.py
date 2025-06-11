from collections import deque

packages = list(map(int, input().split()))
couriers = deque(map(int, input().split()))

total_weight = 0

while packages and couriers:
    package = packages[-1]
    courier = couriers[0]

    if courier >= package:
        total_weight += package
        packages.pop()
        couriers.popleft()

        if courier > package:
            new_capacity = courier - 2 * package
            if new_capacity > 0:
                couriers.append(new_capacity)
    else:
        total_weight += courier
        packages[-1] = package - courier
        couriers.popleft()

print(f"Total weight: {total_weight} kg")

if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages and not couriers:
    print("Unfortunately, there are no more available couriers to deliver the following packages:", end=" ")
    print(", ".join(map(str, packages)))
elif couriers and not packages:
    print("Couriers are still on duty:", end=" ")
    print(", ".join(map(str, couriers)), end=" ")
    print("but there are no more packages to deliver.")
