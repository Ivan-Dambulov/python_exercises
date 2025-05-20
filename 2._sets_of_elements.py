n, m = map(int, input().split())

set1 = set()
set2 = set()

for _ in range(n):
    set1.add(int(input()))

for _ in range(m):
    set2.add(int(input()))

common_elements = set1.intersection(set2)

for element in common_elements:
    print(element)