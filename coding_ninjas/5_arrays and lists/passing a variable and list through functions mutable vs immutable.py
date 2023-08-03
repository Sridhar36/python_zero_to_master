a = 3


def increment(a):
    a = a + 2
    return


print(a)  # prints 3
increment(a)
print(a)  # prints 3

# variables are immutable, here a outside method and a inside method hold different instances

li = [1, 2, 3, 4]


def increment(li):
    li[2] = li[2] + 1
    return


print(li)  # prints [1, 2, 3, 4]
increment(li)
print(li)  # prints [1, 2, 4, 4]

# this is because lists are mutable
# li holds same instance i.e., li inside loop and outside loop point at same instance where li value stored in storage
