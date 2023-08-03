string = "abdefgbabfba"

char_count = {}

for char in string:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)
max_value = 0
max_char_key = None
for key, val in char_count.items():
    if val > max_value:
        max_value = val
        max_char_key = key


def highestOccuringChar(string):
    char_count = {}

    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    max_value = 0
    max_char_key = None
    max_value_list = []
    for key, val in char_count.items():
        if val > max_value:
            max_value = val
            max_value_list.append(max_char_key)
            max_char_key = key
    return max_char_key[0]


def highestOccuringChar(string):
    char_count = {}

    # Count occurrences of each character
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the character with the highest count
    max_count = 0
    highest_char = ''
    for char, count in char_count.items():
        if count > max_count:
            max_count = count
            highest_char = char
        elif count == max_count:
            # If multiple characters have the same count, choose the one that comes first
            highest_char = min(highest_char, char)

    return highest_char

'''
The line highest_char = min(highest_char, char) compares the two characters with the same highest count and assigns the character that comes first in the ASCII table to highest_char'''


