def intersections(arr1, n, arr2, m):
    intersection = []

    for num in arr1:
        # Check if the element is present in list2.
        if num in arr2:
            intersection.append(num)

    return intersection



def intersections(arr1, n, arr2, m):
    intersection = []

    for num in arr1:
        # Check if the element is present in list2.
        if num in arr2:
            intersection.append(num)

    # print(intersection)
    print(" ".join(str(num) for num in intersection))


def intersections(arr1, n, arr2, m):
    intersection = []

    # Create a dictionary to store the occurrences of each element in arr1.
    element_count = {}

    # Count the occurrences of each element in arr1.
    for num in arr1:
        element_count[num] = element_count.get(num, 0) + 1

    # Iterate through arr2 and check if each element is present in arr1.
    for num in arr2:
        if num in element_count and element_count[num] > 0:
            intersection.append(num)
            element_count[num] -= 1

    return intersection


def pairSum(arr, n, x):
    # Create a dictionary to store the occurrences of each element in arr.
    element_count = {}

    # Count the occurrences of each element in arr.
    for num in arr:
        element_count[num] = element_count.get(num, 0) + 1

    # Initialize the count of pairs to zero.
    count_pairs = 0

    # Iterate through the elements in arr.
    for num in arr:
        # Calculate the difference between the current element and x.
        diff = x - num

        # If the difference exists in the dictionary and its occurrence is greater than zero,
        # then we found a pair that sums to x.
        if diff in element_count and element_count[diff] > 0:
            # Update the count of pairs and decrement the occurrences of the current element and the difference.
            count_pairs += 1
            element_count[num] -= 1
            element_count[diff] -= 1

    return count_pairs
