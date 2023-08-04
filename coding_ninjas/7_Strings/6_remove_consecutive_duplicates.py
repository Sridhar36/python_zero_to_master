from sys import stdin


def removeConsecutiveDuplicates(string):
    if not string:
        return ""

    output = string[0]  # Initialize output with the first character of the string
    prev_char = string[0]

    for i in range(1, len(string)):
        if string[i] != prev_char:
            output += string[i]
            prev_char = string[i]

    return output
