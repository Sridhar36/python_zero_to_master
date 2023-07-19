'''
How to approach pattern problems?
First, you have to manually write down the pattern for different inputs to see how it looks like.
printing happens in first row to last row.. line by line. So you have to make sure you are printing from first line.


1. How many rows do I need to print? { n  = how much ? }
2. How many columns do we have to print for an ith row?
3. What to print ?   stars, numbers etc.. | This print value can be function of n or i row or j column

note: when working on patterns.. most of your time should go in understanding what to print rather then directly
printing something
'''

# 1
#
# n = int(input())
#
# for i in range(n):
#     for j in range(n):
#         print('*', end='')  # by giving end='' we are saying do nothing, and do not get into new line.
#     print()
#
# # 2
# # Read input as specified in the question
# # Print the required output in given format
# n = int(input())
#
# for i in range(n):
#     for j in range(n):
#         print(n, end='')
#     print()


'''
Square patterns:

11111
22222
33333
44444
55555
'''
#
# n = 5
#
# for i in range(1, n + 1):
#     for j in range(n):
#         print(i, end='')
#     print()

'''
12345
12345
12345
12345
12345
'''

# n = 5
#
# for i in range(n):
#     for j in range(1,n+1):
#         print(j, end='')
#     print()


'''
54321
54321
54321
54321
54321
'''
# n = 5
#
# for i in range(n):
#     for j in range(n):
#         print(n - j, end='')
#     print()


# Triangular patterns
'''
1
12
123
1234
12345
'''

# n = 5
#
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end='')
#     print()
#


'''
1
23
345
4567
56789
'''
# n = 5
#
# for i in range(1, n + 1):
#     for j in range(i):
#         print(i + j, end='')
#     print()


'''
1
23
456
78910'''
# n = 4

# p = 1
# for i in range(1, n + 1):
#     for j in range(i):
#         print(p, end='')
#         p += 1
#     print()


'''
*
**
***
****
'''

# n = 4
#
# for i in range(1, n + 1):
#     for j in range(i):
#         print('*', end='')
#     print()

'''
1
22
333
4444
'''
# n = 4
#
# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end='')
#     print()


'''
1
21
321
4321
'''

# n = 4
#
# for i in range(1, n + 1):
#     for j in range(i, 0, -1):
#         print(j, end="")
#     print()

'''
CHARACTER PATTERNS

ABCD
ABCD
ABCD
ABCD

ABCD
BCDE
CDEF
DEFG

ord() - gives ascii value for a character
chr() - gives character for ascii value

'''

# n = 4
# for i in range(n):
#     for j in range(1, n + 1):
#         charP = chr(ord('A') + j - 1)
#         print(charP, end='')
#     print()

# n = 4
# for i in range(1, n + 1):
#     start_char = chr(ord('A') + i - 1)
#     for j in range(1, n + 1):
#         charP = chr(ord(start_char) + j - 1)
#         print(charP, end='')
#     print()

'''
A
BC
CDE
DEFG
'''
# n = 4
# for i in range(1, n + 1):
#     start_char = chr(ord('A') + i - 1)
#     for j in range(1, i + 1):
#         charP = chr(ord(start_char) + j - 1)
#         print(charP, end='')
#     print()

'''
E
DE
CDE
BCDE
ABCDE
'''

# n = 5
#
# start_char = ord('A') + n - 1
#
# for i in range(n):
#     for j in range(i + 1):
#         char = chr(start_char - i + j)
#         print(char, end="")
#     print()

'''
1
11
111
1111
'''
#
# n = 5
# for i in range(n):
#     for j in range(i):
#         print('1', end="")
#     print()

'''
1
11
202
3003
40004
'''

'''
1
11
121
1221
12221
'''
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print('1', end='')
        else:
            print('2', end='')
    print()

'''
12345
1234
123
12
1
'''
# n = 5
# for i in range(n):
#     for j in range(1, n + 1 - i):
#         print(j, end='')
#     print()

'''
A
BB
CCC
DDDD
EEEEE
FFFFFF
GGGGGGG
'''

'''
important : why we need range(i+1)

The inner loop's range is changed to range(i+1) to ensure that the character is repeated i+1 times on each line.

In the original code, the inner loop was using range(i), which caused the character to be repeated i times instead of i+1 times. By changing the range to range(i+1), we ensure that the loop iterates i+1 times, resulting in the desired number of repetitions for each character on each line.

Let's go through an example to illustrate this:

When i is 0, the inner loop's range is range(0), which means the loop doesn't run at all, and no character is printed on the line.

When i is 1, the inner loop's range is range(1), and the loop runs once. The character assigned to start_char is 'B', and it is printed once on the line.

When i is 2, the inner loop's range is range(2), and the loop runs twice. The character assigned to start_char is 'C', and it is printed twice on the line.

This pattern continues, with the inner loop running i+1 times for each value of i, ensuring that the character assigned to start_char is repeated the appropriate number of times on each line.

Changing the inner loop's range to range(i+1) allows us to control the number of repetitions of the character on each line, creating the desired pattern.

'''
# n = 6
# for i in range(n):
#     start_char = chr(ord('A') + i)
#     for j in range(i + 1):
#         print(start_char, end="")
#     print()
