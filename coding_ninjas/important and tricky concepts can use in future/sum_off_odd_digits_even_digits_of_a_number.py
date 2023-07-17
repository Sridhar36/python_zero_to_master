'''
Sum of even & odd
Send Feedback
Write a program to input an integer 'n' and print the sum of all its even digits and sum of all its odd digits separately.


Digits mean numbers, not the places! That is, if the given integer is "132456", even digits are 2, 4 and 6 and odd digits are 1, 3 and 5.


Example :
Input: 'n' = 132456

Output: 12 9

Explanation:
The sum of even digits = 2 + 4 + 6 = 12
The sum of odd digits = 1 + 3 + 5 = 9
Input format :
 The first line contains an integer 'n'.


Output format :
In a single line, print two space separated integers, first the sum of even digits, and then the sum of odd digits.
Sample Input 1:
132456


Sample Output 1:
12 9


Explanation of sample input 1 :
The sum of even digits = 2 + 4 + 6 = 12
The sum of odd digits = 1 + 3 + 5 = 9


Sample Input 2:
552245
'''


## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)

n = int(input())
str_n = str(n)

sum_even = 0
sum_odd = 0

# Iterate through each digit in the number
while n > 0:
    digit = n % 10

    # Check if the digit is even or odd
    if digit % 2 == 0:
        sum_even += digit
    else:
        sum_odd += digit

    n = n // 10  # Remove the last digit

print(sum_even, sum_odd)
