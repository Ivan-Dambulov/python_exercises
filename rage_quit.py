text = input()
final_text = ""
sub_string = ""
repetitions = ""
for index in range(len(text)):
    # Case where we have some character
    if not text[index].isdigit():
        sub_string += text[index].upper()
    # Case where we have some digit
    else:
        for next_symbols_index in range(index, len(text)):
            if not text[next_symbols_index].isdigit():
                break
            repetitions += text[next_symbols_index]
        final_text += sub_string * int(repetitions)
        sub_string = ""
        repetitions = ""
print(f"Unique symbols used: {len(set(final_text))}")
print(final_text)