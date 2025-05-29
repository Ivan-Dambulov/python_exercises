from collections import deque

food_quantity = int(input())

orders = deque(int(x) for x in input().split())

max_order = max(orders)
print(max_order)

while orders:
    current_order = orders[0]  # Peek at first order
    if food_quantity >= current_order:
        food_quantity -= orders.popleft()
    else:
        break

if not orders:
    print("Orders complete")
else:
    print("Orders left:", " ".join(str(x) for x in orders))