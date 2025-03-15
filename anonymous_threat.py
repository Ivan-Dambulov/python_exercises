def merge(list_with_words: list, current_command: list) -> list:
    start_index, end_index = int(current_command[1]), int(current_command[2])
    if start_index not in range(len(list_with_words)):
        start_index = 0
    if end_index not in range(len(list_with_words)):
        end_index = len(list_with_words) - 1
    list_with_words[start_index] = "".join(list_with_words[start_index:end_index + 1])
    list_with_words = list_with_words[: start_index + 1] + \
                      list_with_words[end_index + 1:]
    return list_with_words


def divide(string_as_list: list, some_command: list) -> list:
    index, partitions = int(some_command[1]), int(some_command[2])
    element = string_as_list[index]
    partition_size = len(element) // partitions
    partitioned_element = []
    number_of_partition = 0
    for current_index in range(0, len(element), partition_size):
        number_of_partition += 1
        if number_of_partition == partitions:  # last partition -0 have to get all the symbols to the end
            current_partition = element[current_index:]
            partitioned_element.append(current_partition)
            break
        else:
            current_partition = element[current_index:current_index + partition_size]
            partitioned_element.append(current_partition)
    string_as_list = string_as_list[:index] + \
                     partitioned_element + \
                     string_as_list[index + 1:]
    return string_as_list


initial_string_as_list = input().split()
command = input()
while command != "3:1":
    command = command.split()
    action = command[0]
    if action == "merge":
        initial_string_as_list = merge(initial_string_as_list, command)
    elif action == "divide":  # else
        initial_string_as_list = divide(initial_string_as_list, command)
    command = input()
print(" ".join(initial_string_as_list))