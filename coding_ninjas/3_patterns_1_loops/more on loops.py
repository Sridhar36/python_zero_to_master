'''
for loops:

range method - takes three values...start, stop [stop - 1 in actual], step

Break Keyword - Just in case you are using the loop and you want to exit loop when you got your result..
then you can use break

Else with loops: In python you can use else with loops. Else code will not get executed if loop
is terminated. it only gets executed if loop is fully executed.

Continue keyword: When you want to skip an iteration you can use Continue. . .

'''

# # print 1 to n evens skipping the multiple of 7
# n = 100
# for i in range(2, n + 1, 2):
#     if i % 7 == 0:
#         continue
#     print(i)


# i = 1
# while i < 5:
#     if i == 3:
#         continue
#     print(i, end=" ")
#     i = i + 1

'''
i=1
while i<5:
    if i==3:
            continue
    print(i,end=" ")
    i = i + 1

is this correct ?
ChatGPT
No, the code you provided will result in an infinite loop. The issue is with the placement of the increment i = i + 1 inside the while loop. Since it is inside the if statement, it will never be reached when i is equal to 3, causing the loop to keep running indefinitely.

To fix the code and make it work as intended, you should move the increment statement outside of the if block. Here's the corrected version:

python
Copy code
i = 1
while i < 5:
    if i == 3:
        i = i + 1
        continue
    print(i, end=" ")
    i = i + 1
Now, the output will be:

Copy code
1 2 4
With this corrected code, when i is 3, the continue statement will be executed, and the loop will skip the print statement and increment the value of i to 4, eventually exiting the loop when i becomes greater than or equal to 5.
'''

'''
Pass keyword: Will let you pass a loop.
'''

'''
Print the binary pattern
1111
000
11
0
'''

# n = 4
# for i in range(1, n + 1):
#     for j in range(1, n - i + 2):
#         if i % 2 == 0:
#             print('0', end='')
#         else:
#             print('1', end='')
#     print()

#
# n = int(input())
# for i in range(1, n + 1):  # Loop for the upper half of the pyramid
#     # Print spaces
#     for j in range(1, i):
#         print(" ", end="")
#
#     # Print numbers in ascending order
#     for k in range(i, n + 1):
#         print(k, end="")
#
#     print()  # Move to the next line after each row
#
# for i in range(n - 1, 0, -1):  # Loop for the lower half of the pyramid
#     # Print spaces
#     for j in range(1, i):
#         print(" ", end="")
#
#     # Print numbers in ascending order
#     for k in range(i, n + 1):
#         print(k, end="")
#
#     print()  # Move to the next line after each row


'''
  *
 ***
*****
 ***
  *
  '''
# N = 5
#
# # Upper half of the diamond
# for i in range(1, N // 2 + 2):
#     print(" " * (N // 2 + 1 - i) + "*" * (2 * i - 1))
#
# # Lower half of the diamond
# for i in range(N // 2, 0, -1):
#     print(" " * (N // 2 + 1 - i) + "*" * (2 * i - 1))

'''
555555555
544444445
543333345
543222345
543212345
543222345
543333345
544444445
555555555

'''
# N = 5
#
# # Initialize a 2D list to store the pattern
# pattern = [[0 for _ in range(2 * N - 1)] for _ in range(2 * N - 1)]
#
# # Fill the pattern with the rectangular numbers
# for i in range(N):
#     for j in range(i, 2 * N - i - 1):
#         pattern[i][j] = N - i
#         pattern[2 * N - i - 2][j] = N - i
#
#     for j in range(i + 1, 2 * N - i - 2):
#         pattern[j][i] = N - i
#         pattern[j][2 * N - i - 2] = N - i
#
# # Print the pattern row by row
# for row in pattern:
#     for num in row:
#         print(num, end="")
#     print()

'''

'''
n = 5
p = 1
c = (n + 1) // 2
for i in range(1, c + 1):
    j = 1
    while (j <= n):
        print(p, end=" ")
        p += 1
        j += 1
    p += n
    print(end="\n")
if (n % 2 == 0):
    p = n * n - n + 1;
else:
    p = n * n - n * 2 + 1
c = (n) // 2
for i in range(1, c + 1):
    j = 0
    while (j < n):
        print(p, end=" ")
        p += 1
        j += 1
    p -= n * 3
    print(end="\n")
