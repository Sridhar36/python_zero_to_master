# prime number - a number which can be divisible by one and itself
# If none of the numbers in the loop divide the given number evenly, we know that it has no factors other than 1 and
# itself, so we return True, indicating that the number is prime.

# Find if given number is prime
n = int(input())
d = 2
flag = False

while d < n:
    if (n % 2 == 0):
        flag = True
    d = d + 1

if flag:
    print("not prime")
else:
    print("prime")

# find prime numbers in given number range

n = int(input())
k = 2
while k <= n:
    d = 2
    Flag = False
    while (d <= k):
        if k % d == 0:
            flag = True
        d += 1
    if not (flag):
        print(k)
