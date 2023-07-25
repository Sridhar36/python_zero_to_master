def is_palindrome(n):
    # Convert the number to a string for easy comparison
    n_str = str(n)

    # Compare the number with its reverse
    return n_str == n_str[::-1]

# Test cases
print(is_palindrome(51415))  # Output: True
print(is_palindrome(12321))  # Output: True
print(is_palindrome(12345))  # Output: False
