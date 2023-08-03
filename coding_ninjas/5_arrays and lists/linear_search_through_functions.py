# linear search through functions:
list = [int(x) for x in input("enter the space separated input list: ").split()]
number = int(input("enter the number you are searching for: "))


def linear_search(li, ele):
    if ele in li:
        return li.index(ele)
    return -1


print(linear_search(list, number))
