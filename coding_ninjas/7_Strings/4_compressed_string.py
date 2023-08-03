def getCompressedString(input_str):
    compressed_str = ""

    # Initialize the current character and its count
    current_char = input_str[0]
    char_count = 1

    # Iterate through the string starting from the second character
    for char in input_str[1:]:
        if char == current_char:
            # If the current character is the same as the previous one, increment the count
            char_count += 1
        else:
            # If the current character is different, append the compressed part to the result string
            if char_count > 1:
                compressed_str += current_char + str(char_count)
            else:
                compressed_str += current_char
            # Reset the current character and count for the next character
            current_char = char
            char_count = 1

    # Append the last compressed part to the result string
    if char_count > 1:
        compressed_str += current_char + str(char_count)
    else:
        compressed_str += current_char

    return compressed_str


# Test the function with the given sample input
input_str = "aaabbccdsa"
print(getCompressedString(input_str))  # Output: 'a3b2c2dsa'


# 2
def getCompressedString(input_str):
    compressed_str = ""
    char_count = {}

    for char in input_str:
        char_count[char] = char_count.get(char, 0) + 1

    for char, count in char_count.items():
        if count > 1:
            compressed_str += char + str(count)
        else:
            compressed_str += char

    return compressed_str


# Test the function with the given sample input
input_str = "aaabbccdsa"
print(getCompressedString(input_str))  # Output: 'a3b2c2dsa'
