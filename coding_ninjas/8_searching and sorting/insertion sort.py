from typing import List

def insertionSort(a: List[int], n: int) -> None:
    for i in range(1, n):
        key = a[i]
        j = i - 1

        # Move elements of a[0...i-1] that are greater than key to one position ahead of their current position
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key
