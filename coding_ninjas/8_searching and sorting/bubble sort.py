from typing import List

def bubbleSort(arr: List[int], n: int):
    for i in range(n):
        # Flag to check if any swap is done in this pass
        swapped = False

        # Last i elements are already sorted, so we don't need to check them again
        for j in range(n - i - 1):
            # Swap the elements if they are in the wrong order
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped in the inner loop, the array is already sorted
        # and we can break out of the outer loop early.
        if not swapped:
            break
