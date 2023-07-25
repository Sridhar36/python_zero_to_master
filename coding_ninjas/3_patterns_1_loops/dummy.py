# 20 15
x = 20
y = 15

flag = 0
high = 0

if x > y:
    high = x
else:
    high = y

for i in range(1, high + 1):
    if x % i == 0 and y % i == 0:
        flag = i
print(flag)


def findGcd(x, y):
    flag = 0
    high = 0

    if x > y:
        high = x
    else:
        high = y

    for i in range(1, high + 1):
        if x % i == 0 and y % i == 0:
            flag = i
    print(flag)
