n = int(input())

longest_intersection = set()
max_length = 0

for _ in range(n):
    range1, range2 = input().split('-')
    start1, end1 = map(int, range1.split(','))
    start2, end2 = map(int, range2.split(','))


    set1 = set(range(start1, end1 + 1))
    set2 = set(range(start2, end2 + 1))
    intersection = set1.intersection(set2)

    current_length = len(intersection)
    if current_length > max_length:
        max_length = current_length
        longest_intersection = intersection

intersection_list = sorted(list(longest_intersection))

print(f"Longest intersection is {intersection_list} with length {max_length}")