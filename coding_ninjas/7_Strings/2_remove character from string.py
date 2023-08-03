def remove_character(string, X):
    # Use list comprehension to create a new string without the character X
    updated_string = ''.join([ch for ch in string if ch != X])
    return updated_string


# Test the function
input_string = input().strip()
character_to_remove = input().strip()
output_string = remove_character(input_string, character_to_remove)
print(output_string)
