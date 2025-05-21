text = input()

char_count = {}

for char in text:
    char_count[char] = char_count.get(char, 0) + 1

for char in sorted(char_count.keys()):
    print(f"{char}: {char_count[char]} time/s")