from collections import Counter

arr1 = [2, 2, 6, 8, 5, 4, 3]
arr2 = [2, 2, 3, 4, 7]


def intersections(arr1, arr2):
    # Find the common elements with their counts using Counter
    common_elements = (Counter(arr1) & Counter(arr2))
    print("array -1 : ", arr1)
    print("array -2 : ", arr2)
    print("intersection : ", common_elements)

    # Print the intersection elements while maintaining the order from arr1
    for element in arr1:
        if common_elements[element] > 0:
            # print(element, end=" ")
            print(element)
            print("common_elements before - ", common_elements)
            common_elements[element] -= 1
            print("common_elements after - ", common_elements)


intersections(arr1, arr2)
