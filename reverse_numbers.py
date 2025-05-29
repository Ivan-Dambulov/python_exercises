numbers = [int(x) for x in input().split()]

stack = []
for num in numbers:
    stack.append(num)

reversed_numbers = []
while stack:
    reversed_numbers.append(stack.pop())

print(" ".join(str(x) for x in reversed_numbers))