# For loop
# short circuiting
# for item in iterable: iterables can be a list. dictionary, set, string, tuple etc.
# iterables are collection of items or the ones that are iterable.
# we can nest for loops

# eg for dictionary

user = {
    'user': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user.items():
    key, value = item
    print("captured keys", key)
    print("captured values ", value)

for k, v in user.items():
    print(k, v)

# range
print(range(100))
for i in range(10, 0, -2):
    print(i)

# this code below will print 0 to 9 numbers..
# we can use underscore because  this serves as an indicator that we are not really concerned about
# the  variable, but we are just trying to use range.
for _ in range(0, 10):
    print(_)

# quick way to print a list of 10 integers
print(list(range(10)))

# enumerate - takes iterable object and gives index
for i, char in enumerate('Helloooo'):
    print(i, char)
# below format output is possible because we are using enumerate. (it gives the index)
'''o/p
0 H
1 e
2 l
3 l
4 o
5 o
6 o
7 o
'''

# while loop
i = 0
while i < 50:
    print(i)
    i += 1
    break  # if we use break in while loop, then else loop will be ignored
else:
    print("done looping")

# while loops vs for loop
# while loops are flexible, but for loops are simple
# for loop - good for simple loops or iterating over some iterable objects
# while loop - if we are not sure how long we are going to loop, or where we gonna find the required condition.
# i.e if we are not sure on length or range
# eg: send emails as long as there are inflow requests
# syntax :
while True:
    s = input('say something..')
    if s == 'bye':
        break
