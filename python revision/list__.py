# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)
#
#
# # rotate list
# def rotate_lst(lst, k):
#     n = len(lst)
#     k = k % n
#     return lst[-k:] + lst[:-k]
#
# print(rotate_lst([1,2,3,4,5,6,7,8],2))
#
#
#
# # flatten nested list
#
#
#
#
# def kids(*kids):
#     print(kids)
#
# kids("sir", "ff", "ee", "ee" ,"dd")
#
# def jobs(*kwargs):
#     pass

lst = [1, 2, 2, 3, 4, 6, 7]

from collections import Counter

counts = Counter(lst)
sum_ = sum(num for num, cnt in counts.items() if cnt == 1)
print(sum_)