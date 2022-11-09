'''
I want to talk to you about some useful functions that we get that actually allow us to think in a functional. The name
of these functions are map, filter, Zip and reduce. These are very, very useful, very common functions that you'll write
a lot when you're a Python programmer.
'''

'''Map - map() function returns a map object(which is an iterator) of the results after applying the given function to 
each item of a given iterable (list, tuple etc.)
Syntax :
map(fun, iter)

Parameters :
fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.

NOTE : You can pass one or more iterable to the map() function.

Returns :Returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.) 
 NOTE : The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) .

in eg below:
by doing this map automatically runs this function for us and loops through all the items in the
iterable and returns for us a new map object that we're going to convert into a list if I run this.
A pure function is a function that doesn't affect the outside world. And this way map allows us to create a whole new 
list. That doesn't modify my list.'''


def multiply_by2(item):
    return item * 2


print(list(map(multiply_by2, [1, 2, 3])))  # o/p  [2, 4, 6]


# Python program to demonstrate working
# of map.

# Return double of n
def addition(n):
    return n + n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))  # o/p - [2, 4, 6, 8]
