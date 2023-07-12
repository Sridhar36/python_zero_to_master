'''
Just in case you want to check if three conditions all together
'''

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

c1 = a > 10 and b > 10 and c > 10 and d > 10 and e > 10
c2 = a < 30 and b < 30 and c < 30 and d < 30 and e < 30

if c1 and c2:
    print("all input value are greater then 10 and less then 30")
else:
    print("Either one condition not met")
