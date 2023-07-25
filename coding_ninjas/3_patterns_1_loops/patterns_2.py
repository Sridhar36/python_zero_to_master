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


# N = 5
#
# if N % 2 != 0:  # Ensure N is always odd
#
#     for i in range(1, N + 1, 2):  # Loop through odd numbers from 1 to N
#         spaces = (N - i) // 2
#         stars = i
#         print(" " * spaces, end="")
#         print("*" * stars)
#
#     for i in range(N - 2, 0, -2):  # Loop through odd numbers from N-2 to 1 in reverse
#         spaces = (N - i) // 2
#         stars = i
#         print(" " * spaces, end="")
#         print("*" * stars)


'''
trick here is to break and solve these problems:
split the below pattern into half - in my case I considered first pattern, then spaces, then spaces again, then pattern

most importantly pen down pattern and the figure out solution on paper..
how many rows
how many columns
what to print

1      1
12    21
123  321
12344321
'''
# n = 4
#
# for i in range(1, n + 1):
#     # start values
#     for j in range(1, i + 1):
#         print(j, end='')
#
#     # spaces first set
#     for k in range(n - i):
#         print(' ', end='')
#
#     # spaces second set
#     for l in range(n - i):
#         print(' ', end='')
#
#     # end values
#     for m in range(i, 0, -1):
#         print(m, end='')
#
#     print()


'''
*0000*0000*
0*000*000*0
00*00*00*00
000*0*0*000
0000***0000
'''

# N = 5
# for i in range(N):
#     for j in range((2 * N) + 1):
#         if j == i or j == N or j == (2 * N) - i:
#             print("*", end="")
#         else:
#             print("0", end="")
#     print()


'''
    1
   212
  32123
 4321234
543212345

To create the pyramid number pattern as described, you can use nested loops to control the spaces and the numbers on 
each row. Here's the Python function to generate the desired pattern:
'''
# N = 5
# for i in range(1, N + 1):
#     # Print spaces before the numbers
#     for j in range(N - i):
#         print(" ", end="")
#
#     # Print the decreasing numbers
#     for j in range(i, 0, -1):
#         print(j, end="")
#
#     # Print the increasing numbers
#     for j in range(2, i + 1):
#         print(j, end="")
#
#     print()


'''
*
 **
  * *
   *  *
    *   *
   *  *
  * *
 **
*

'''

N = 5
for i in range(1, (N // 2) + 2):
    # Print leading spaces
    for j in range(1, i):
        print(" ", end="")

    # Print stars with spaces in between
    for j in range(1, i + 1):
        if j == 1:
            print("*", end="")
        else:
            print(" *", end="")

    print()

for i in range(N // 2, 0, -1):
    # Print leading spaces
    for j in range(1, i):
        print(" ", end="")

    # Print stars with spaces in between
    for j in range(1, i + 1):
        if j == 1:
            print("*", end="")
        else:
            print(" *", end="")

    print()

