#  Recursively Summing List Elements
def sum_of_n(lst):
    # Base case: if the list is empty, return 0
    if len(lst) == 0:
        return 0
    else:
        # Recursive case: sum of the first element + sum of the rest of the list
        return lst[0] + sum_of_n(lst[1:])

# Test the function
numbers = [1, 2, 3, 4, 5]
result = sum_of_n(numbers)
print(f"The sum of the elements in the list is: {result}")



def sum_of_n(n):
    # Base case: if n is 0, return 0
    if n == 0:
        return 0
    else:
        # Recursive case: sum of n is n + sum of n-1
        return n + sum_of_n(n-1)

# Test the function
n = 5
result = sum_of_n(n)
print(f"The sum of the first {n} natural numbers is: {result}")

# febanocci series
def fibonacci(n):
    # Base cases: Fibonacci of 0 is 0, Fibonacci of 1 is 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: Fibonacci of n is the sum of Fibonacci of (n-1) and (n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)

# Function to generate the Fibonacci series up to n
def generate_fibonacci_series(n):
    series = []
    for i in range(n):
        series.append(fibonacci(i))
    return series

# Test the function
n = 10  # Generate first 10 Fibonacci numbers
fib_series = generate_fibonacci_series(n)
print(f"The first {n} numbers of the Fibonacci series are: {fib_series}")

# nth fibanacci number
def fibonacci(n):
    if n <= 1:  # Base case
        return n
    else:  # Recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)

# sum of numbers in list
def sum_of_list(lst):
    if len(lst) == 0:  # Base case
        return 0
    else:  # Recursive case
        return lst[0] + sum_of_list(lst[1:])



def find_pair(arr, target):
    print(f"arr: {arr}")
    print(f"target : {target}")
    left, right = 0, len(arr) - 1
    while left < right:
        print(f"left: {left}")
        print(f"right: {right}")
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < target:
            print(f"left: {left}")
            print(f"right: {right}")
            left += 1
        else:
            print(f"left: {left}")
            print(f"right: {right}")
            right -= 1
    return None

arr = [1, 3, 4, 6, 8, 10]
target = 12
print(find_pair(arr, target))  # Output: (4, 8)



