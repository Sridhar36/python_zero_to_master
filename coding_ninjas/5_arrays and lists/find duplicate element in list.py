n = 9
arr = [1, 1, 2, 1, 1, 3, 4, 4, 3]


def duplicate(arr):
    # initialize dictionary
    elements_count = {}

    # iterating through list and creating key value pairs in dict for each list element
    for number in arr:
        elements_count[number] = elements_count.get(number, 0) + 1
        print(elements_count)

    # iterating through list and checking first unique count number and returning it.
    for i in arr:
        if elements_count[i] != 1:
            print("duplicate element : ", i)
            return


duplicate(arr)
