'''

binary search: the basic idea behind binary search is to divide the search space in half at each step until the target
value is found or the search space becomes empty.

a= [1,2,3,4,5,6,7]
value_to_search(x) = 5

1. sort array
2.

'''


def binary_search(arr, target):
    lower_bound = 0
    upper_bound = len(arr) - 1

    while lower_bound <= upper_bound:
        middle = (lower_bound + upper_bound) // 2
        if target == arr[middle]:
            return middle
        elif target > middle:
            lower_bound = middle + 1
        elif target < middle:
            upper_bound = middle - 1
    return -1


print(binary_search([1, 2, 3, 4, 5], 3))

# 2
test = [1, 2, 2, 3, 3, 3, 4, 8, 9, 19, 19, 19]
# print(binary_search(test, 2))

print(test)
print(sorted(test))
print(test[::-1])


def find_first_last_occurrences(arr, target):
    first_occurrence = arr.index(target)
    last_occurrence = len(arr) - 1 - arr[::-1].index(target)
    return first_occurrence, last_occurrence

