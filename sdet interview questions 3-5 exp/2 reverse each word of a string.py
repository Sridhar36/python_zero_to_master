def reverse_words_in_string(s):
    words = s.split()  # Split the string into words
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    reversed_string = ' '.join(reversed_words)  # Join the reversed words back into a string
    return reversed_string


# Example input
str_input = "Hello World, How are you?"

reversed_output = reverse_words_in_string(str_input)
print(reversed_output)
