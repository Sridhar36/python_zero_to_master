'''
Methods: it is a block of code written once and executed whenever we need the functionality.
'''


def square(n):
    return n * n


print(square(5))

# In python, we can store methods in variables. i.e methods can be assigned to variables.
s = square
print(s(6))

sq = s
print(sq(7))


# We can also pass methods as variables or arguments to another functions.
def factors(fun, n):
    sq = fun(n)

    factors = []
    for i in range(2, sq):
        if sq % i == 0:
            factors.append(i)

    return factors


print(factors(square, 10))
# print(factors(cube, 10))


# Nested methods:
def outer():
    def inner(name):
        return "good morning " + name

    return inner


greet = outer()

print(greet("coding ninjas"))

'''
Decorator:
it is a design pattern that allows a user to add new functionality to an existing object without modifying its structure
'''

def upperCaseDecorator(fun):
    def toUpperCase(string):
        x = fun(string)
        x = x.upper()
        return x

    return toUpperCase

def greet(name):
    return 'Hello '+name+' , How are you ?'

upper = upperCaseDecorator(greet)
print(upper('Ravi'))


# actual implementation

def upperCaseDecorator(fun):
    def toUpperCase(string):
        x = fun(string)
        x = x.upper()
        return x

    return toUpperCase

@upperCaseDecorator
def greet(name):
    return 'Hello '+name+' , How are you ?'

# upper = upperCaseDecorator(greet)
print(upper('Ravi'))



# example - 2

from datetime import datetime


def log_datetime(func):
    def wrapper():
        print(f"Function: Datetime")
        print(f'{"-" * 30}')
        func()

    return wrapper

@log_datetime
def daily_bckup():
    print("daily backup job is done !!")

daily_bckup()
