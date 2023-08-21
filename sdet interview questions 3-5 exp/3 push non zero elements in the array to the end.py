# chat gpt
def push_zeros_to_end(arr):
    non_zero_count = 0

    # Traverse the array, move non-zero elements to the left
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_count] = arr[i]  # it is like shifting non zeroes to first side..
            non_zero_count += 1

    # Fill the remaining positions with zeros
    while non_zero_count < len(arr):
        arr[non_zero_count] = 0
        non_zero_count += 1

    return arr


# Example input
array = [1, 2, 0, 4, 3, 0, 5, 0]

result = push_zeros_to_end(array)
print(result)


# mine
def push_non_zereos_to_the_end(arr):
    nonZ = 0
    new_arr = []
    for i in range(len(arr)):
        if arr[i] != 0:
            new_arr.append(arr[i])
        elif arr[i] == 0:
            nonZ += 1
    for j in range(nonZ):
        new_arr.append(0)
    return new_arr


arr = [0, 0, 2, 1, 2, 3, 0, 0]
print(push_non_zereos_to_the_end(arr))
