def is_armstrong(n):
    # Convert the number to a string to find the number of digits
    n_str = str(n)
    num_digits = len(n_str)

    # Calculate the sum of digits raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in n_str)

    # Check if the sum is equal to the original number
    return armstrong_sum == n

# Test cases
print(is_armstrong(1634))  # Output: True
print(is_armstrong(371))   # Output: True
print(is_armstrong(123))   # Output: False
