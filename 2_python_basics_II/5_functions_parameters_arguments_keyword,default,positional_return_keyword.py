'''
def - that lets the python interpreter know that we are creating a function.
In order to use a function we have to call it with ()

Nested functions are possible in Python
'''


def sayhello():
    print('Helloo..')


sayhello()

'''
arguments vs parameters :
we can give parameters in function inside brackets, The ones we give while defining the function
arguments are the values we give while calling the function, The ones we give while calling function
'''


def sayhello(name, emoji):
    print(f'Helloo.. {name}'
          f'{emoji}')


sayhello('Sridhar', ':)')

'''
Default parameters vs keyword arguments
positional arguments - based on position of parameters
keyword arguments - we give keyword and value
'''
# keyword arguments below
sayhello(emoji=':)', name='Sridhar')


# default arguments below:
# it allows us to have default values, i.e when the arguments are not given while calling the function
# then these default values are considered.
# this is great way to make the function callable even when arguments are missed
def sayhello(name='Dark rider', emoji='😂'):
    print(f'Helloo.. {name}'
          f'{emoji}')


sayhello()  # prints Darkrider😂
sayhello('sridhar')  # prints sridhar😂


# return - it is a Python keyword
# exit the function and return something
# key note: A function should usually return something..
# return keyword automatically exits the function.. i.e whatever code you write return statement will not get executed

def sum(num1, num2):
    return num1 + num2


print(sum(4, 5))


def sum(num1, num2):
    def another_func(num1, num2):
        return num1 + num2


total = sum(10, 20)
print(total)  # this will print None


# nested function
def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2

    return another_func(num1, num2)


total = sum(10, 20)
print(total)  # now prints 30
