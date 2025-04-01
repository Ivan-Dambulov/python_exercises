first_string, seconds_string = input().split()
total_sum = 0
if len(first_string) > len(seconds_string):
    for index in range(len(seconds_string)):
        total_sum += ord(first_string[index]) * ord(seconds_string[index])
    for index in range(len(seconds_string), len(first_string)):
        total_sum += ord(first_string[index])
elif len(seconds_string) > len(first_string):
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(seconds_string[index])
    for index in range(len(first_string), len(seconds_string)):
        total_sum += ord(seconds_string[index])
else: #len(seconds_string) == len(first_string)
    for index in range(len(seconds_string)):
        total_sum += ord(first_string[index]) * ord(seconds_string[index])
print(total_sum)