'''
inverted triangle pattern

*****
****
***
**
*

'''

# n = 5
# for i in range(n):
#     for j in range(n - i):
#         print('*', end="")
#     print()
#

'''
55555
4444
333
22
1
'''

# n = 5
# for i in range(n):
#     for j in range(n - i):
#         print(n - i, end="")
#     print()

'''
reverse pattern:
to create spaces we have to print space.
approach:
1. decide row count (n)
2. decide how many spaces and how many values to print.
3. What's the value to print.

Loop through i for rows.
while looping through j for columns
    first print spaces - print(' ', end='')
    then print values - print('*', end='')
Add print to move to next line.

    *
   **
  ***
 ****
*****
'''
#
# n = 5
# for i in range(n):
#     # Print spaces
#     for j in range(n - i - 1):
#         print(" ", end="")
#     # Print asterisks
#     for k in range(i + 1):
#         print("*", end="")
#     print()


'''
    1
   12
  123
 1234
12345
'''
# n = 5
# for i in range(n):
#     # Print spaces
#     for j in range(n - i - 1):
#         print(" ", end="")
#     # Print asterisks
#     for k in range(i + 1):
#         print(k + 1, end="")
#     print()


'''
Isosceles Pattern:

break pattern in three parts: spaces, increasing numbers, decreasing numbers

    1
   121
  12321
 1234321
123454321


'''

# rows = 5
# for i in range(1, rows + 1):
#     # Print spaces
#     for j in range(rows - i):
#         print(" ", end="")
#
#     # Print numbers in increasing order
#     for k in range(1, i + 1):
#         print(k, end="")
#
#     # Print numbers in decreasing order
#     for l in range(i - 1, 0, -1):
#         print(l, end="")
#
#     print()


'''
    *
   ***
  *****
 *******
*********
'''

# rows = 5
# for i in range(1, rows + 1):
#     # Print spaces
#     for j in range(rows - i):
#         print(" ", end="")
#
#     # Print numbers in increasing order
#     for k in range(1, i + 1):
#         print('*', end="")
#
#     # Print numbers in decreasing order
#     for l in range(i - 1, 0, -1):
#         print('*', end="")
#
#     print()


'''
   1
  232
 34543
4567654
'''
# rows = 4
# for i in range(1, rows + 1):
#     # Print spaces
#     for j in range(rows - i):
#         print(' ', end="")
#
#     # Print numbers in increasing order
#     for k in range(i):
#         print(i + k, end="")
#
#         # Print decreasing numbers
#     for l in range(i * 2 - 2, i - 1, -1):
#         print(l, end="")
#
#     print()


'''
  *
 ***
*****
 ***
  *
'''

rows = 5
# for i in range(1, (rows // 2) + 2):
#     # Print spaces
#     for j in range(rows - i):
#         print(" ", end="")
#
#     # Print numbers in increasing order
#     for k in range(1, i + 1):
#         print('*', end="")
#
#     # Print numbers in decreasing order
#     for l in range(i - 1, 0, -1):
#         print('*', end="")
#     print()
# for i in range((rows // 2), rows-1):
#     # Print spaces
#     for j in range((rows // 2)-i):
#         print(" ", end="")
#
#     # Print numbers in increasing order
#     for k in range(1, i + 1):
#         print('*', end="")
#
#     # Print numbers in decreasing order
#     for j in range(rows - i):
#         print(" ", end="")
#     print()


for i in range(rows):
    # Print leading spaces
    for j in range(rows - i - 1):
        print(" ", end="")

    # Print asterisks
    for k in range(2 * i + 1):
        print("*", end="")

    print()

for i in range(rows - 2, -1, -1):
    # Print leading spaces
    for j in range(rows - i - 1):
        print(" ", end="")

    # Print asterisks
    for k in range(2 * i + 1):
        print("*", end="")

    print()
