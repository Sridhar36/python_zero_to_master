# def reverse_in_place(nums: list[int]) -> None:
#     left, right = 0, len(nums) - 1
#     while left < right:
#         nums[left], nums[right] = nums[right], nums[left]
#         left += 1
#         right -= 1
#
# # Example
# arr = [1, 2, 3, 4, 5]
# reverse_in_place(arr)
# print(arr)  # [5, 4, 3, 2, 1]
#



#
# def reverse_list(lst):
#     left, right = 0, len(lst) - 1
#     while left<right:
#         lst[left], lst[right] = lst[right], lst[left]
#         left += 1
#         right -= 1
#     return lst
#
# lst = [1,2,3,4,5,6]
# print(reverse_list(lst))
#


def move_zeroes(nums: list[int]) -> None:
    ins = 0

    for i in nums:
        if i != 0:
            nums[ins] = i
            ins+=1
        else:
            continue
    while ins < len(nums):
        nums[ins] = 0
        ins+=1


arr = [0,0,1,0,0,10,10,10,0,0,0,1]
move_zeroes(arr)
print(arr)
