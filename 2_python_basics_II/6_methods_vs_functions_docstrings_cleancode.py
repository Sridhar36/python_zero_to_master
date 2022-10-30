'''
methods vs functions
list(), print(), max(), min(), input() are default functions in python.

- we call functions with function name followed by ()
- methods are called using dot(.)
methods has to be owned by something ANd owned by whatever we have before (..)
'''


# Docstrings - helps to give the information
# real useful to add comments and additional info on functions, so when we get back to functions in future or if others
# checks this will understand easily
def sample(a):
    '''
    This is doc string
    :param a:
    :return:
    '''
    print(a)


sample('!!!!')

# we can use help to see docstrings of any function
help(sample)
''' this above prints
Help on function sample in module __main__:

sample(a)
    This is doc string
    :param a:
    :return:
'''

# another way to get info is using dunder method
print(sample.__doc__)


'''
clean code:
Think of ways how you can clean the code. ie., having less number of lines of code'''