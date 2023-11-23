from typing import List


'''
The function selectionSort is explicitly defined to accept a parameter of type List[int], which means it is specifically designed to work with 
lists of integers. If you were to pass in a list of strings, it would likely result in a type error.
'''
def selectionSort(arr: List[int]) -> None:
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        # Find the minimum element in the unsorted part of the array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the first element in the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
