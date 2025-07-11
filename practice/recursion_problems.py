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
