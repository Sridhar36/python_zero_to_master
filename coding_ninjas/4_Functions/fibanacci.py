def is_fibonacci_member(N):
    # Base cases for Fibonacci series
    if N == 0 or N == 1:
        return True

    # Initialize first two numbers of Fibonacci series
    a, b = 0, 1

    # Iterate to generate the Fibonacci series until we find a number greater than or equal to N
    while b <= N:
        if b == N:
            return True
        a, b = b, a + b

    return False


# Test cases
print(is_fibonacci_member(5))  # Output: True
print(is_fibonacci_member(14))  # Output: False
