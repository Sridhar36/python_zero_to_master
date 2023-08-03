# taking line separated input in a list:

# li = []
# N = int(input())
# for i in range(N):
#     curr = int(input())
#     li.append(curr)
#
# print("This is your list - ", li)

# taking space separated input in a list:

li = []

# Strings split() function
# we can use split() with a delimiter to split the string

# str = "1,2,3,4,5"
# str_split = str.split(',')
# print('str - ', str)
# print('str_split - ', str_split)
#
# str_2 = "1 2 3 4 5"
# str_split_2 = str_2.split()  # takes space as delimiter by default
# print('str_2 - ', str_2)
# print('str_split_2 - ', str_split_2)
#
# # taking space separated input
# list1 = [int(x) for x in input().split()]
# print(list1)
#
# N = int(input("Enter the number of integers (N): "))
# arr = [int(x) for x in input(f"Enter {N} space-separated integers: ").split()][:N]
#


N = int(input())
# arr = list(map(int, input().split()))
# print(sum(arr))

list = [int(x) for x in input().split()][:N]
print(sum(list))
