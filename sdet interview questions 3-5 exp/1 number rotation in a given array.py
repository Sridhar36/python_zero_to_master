def right_rotate_array(arr, rotation):
    n = len(arr)
    rotation %= n  # Normalize rotation in case it's larger than the array length
    rotated = arr[-rotation:] + arr[:-rotation]
    return rotated


# Example input
array = [1, 2, 3, 4, 5]
rotation = 2

# Example input
array_2 = [1, 2, 3, 4, 5]
rotation_2 = 4


rotated_array = right_rotate_array(array, rotation)
print(rotated_array)

rotated_array2 = right_rotate_array(array_2, rotation_2)
print(rotated_array2)

'''
Suppose we have the following input:

python
Copy code
array = [1, 2, 3, 4, 5]
rotation = 2
We want to perform a right rotation of the array by 2 positions.

Calculate Effective Rotation:
The given rotation value is 2. However, since the length of the array is 5, rotating by 2 positions is the same as rotating by 2 % 5 = 2 positions. This normalization step ensures that we don't perform unnecessary full cycles of rotation.

Calculate Rotated Array:
The rotated array can be obtained by splitting the original array into two parts: the last rotation elements and the remaining elements.

Last 2 elements of the original array: [4, 5]
Remaining elements: [1, 2, 3]
Now, if we concatenate these two parts in the order of last elements followed by the remaining elements, we get the rotated array:

Rotated array: [4, 5, 1, 2, 3]

Print Rotated Array:
The final rotated array is [4, 5, 1, 2, 3], which is the desired output.

Here's the breakdown of the right_rotate_array function with the given input:

python
Copy code
def right_rotate_array(arr, rotation):
    n = len(arr)
    rotation %= n  # Normalize rotation in case it's larger than the array length
    rotated = arr[-rotation:] + arr[:-rotation]
    return rotated

# Example input
array = [1, 2, 3, 4, 5]
rotation = 2

rotated_array = right_rotate_array(array, rotation)
print(rotated_array)
In this example, the function calculates the normalized rotation (rotation %= n) to ensure we perform the correct number of rotations. Then, it constructs the rotated array by slicing the original array into two parts and concatenating them in the desired order. The rotated_array is printed, resulting in the output [4, 5, 1, 2, 3].
'''
