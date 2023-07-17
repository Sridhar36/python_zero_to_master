'''
Input format :
Integer N
Output format :
Corresponding reverse number
Constraints:
0 <= N < 10^8
Sample Input 1 :
1234
Sample Output 1 :
4321
Sample Input 2 :
1980
Sample Output 2 :
891
'''

# Write Your Code Here
number = int(input())
while number % 10 == 0:
    number = number // 10

reversed_number = str(number)[::-1]

print(int(reversed_number))
