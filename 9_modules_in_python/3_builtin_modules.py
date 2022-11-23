'''
One of the reason why Python is so popular is the Python builtin modules.
these get downloaded along with Python interpreter. When we want to use these, we have to import them.
'''

import random

print(random)  # gives location of the module
help(random)  # gives documentation and information of help module
print(dir(random))  # gives methods available in the package

print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # picks the number from given list

import sys  #

sys.argv

'''
Command line arguments are those values that are passed during calling of program along with the calling statement. 
Thus, the first element of the array sys.argv() is the name of the program itself. sys.argv() is an array for command 
line arguments in Python. To employ this module named “sys” is used. sys.argv is similar to an array and the values are 
also retrieved like Python array.'''


