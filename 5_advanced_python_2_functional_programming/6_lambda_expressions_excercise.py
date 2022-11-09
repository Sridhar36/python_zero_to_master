'''
A lambda function is a small anonymous function. Because these are functions without definition or names
A lambda function can take any number of arguments, but can only have one expression.
- https://www.youtube.com/watch?v=hYzwCsKGRrg
* remember we can even pass functions as parameters to another functions because functions
are objects in Python.

Syntax
lambda arguments : expression
The expression is executed and the result is returned:
'''
# Example
# Add 10 to argument a, and return the result:

x = lambda a: a + 10
print(x(5))

# note - Lambda functions can take any number of arguments:

# Example
# Multiply argument a with argument b and return the result:

x = lambda a, b: a * b
print(x(5, 6))

# Example
# Summarize argument a, b, and c and return the result:

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

'''
Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.
Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
'''


# Use that function definition to make a function that always doubles the number you send in:

# Example
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))


# Or, use the same function definition to make a function that always triples the number you send in:

# Example
def myfunc(n):
    return lambda a: a * n


mytripler = myfunc(3)

print(mytripler(11))

'''
udemy:
lambda param : function or action (parameter)

Remember, Lambda expressions are one time anonymous functions.
There's no name attached to this function. This is a really nice feature of Python to keep your code really nice and 
clean and not clutter with all these functions.
'''
my_list = [1, 2, 3, 4]
print(list(map(lambda item: item * 2, my_list)))
# print(my_list)

from functools import reduce

print(reduce(lambda acc, item: acc + item, my_list))

# excercise -
# 1. create lambda expression to square the list
# 2. list sorting - we have a list of tuples , sort the tuples basis on the elements in tuple

# 1 square
my_list = [1, 2, 3, 4, 5, 6]
print(list(map(lambda a: a * a, my_list)))

# 2. sorting list of tuples:
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
sorted_lis = list(map(lambda a: sorted(a), a))
print(sorted_lis)

# 3. sort the list of tuples by second item in tuple
b = [(0, 2), (4, 3), (9, 9), (10, -1)]
b.sort(key=lambda x: x[1])
print(b)

# lambda for linear equations
# 3x + 4y
d = lambda x, y: 3 * x + 4 * y
print(d(4, 7))
