'''
list comprehension
'''

# convert a string into char list
print([char for char in 'hello'])
# create a list of 1 to 100 numbers
print([num for num in range(1, 100)])
# create a list of 1 to 100 multiplied by 2
print([num * 2 for num in range(100)])
# create a list of 1 to 100 squared
print([num ** 2 for num in range(100)])
# create a list of 1 to 100 evens
print([num for num in range(100) if num % 2 == 0])

'''
dictionary comprehension
'''
simpledict = {
    'a': 1,
    'b': 2,
}

# create a new dict from above using dict comprehension, multiply values
print({k: v ** 2 for k, v in simpledict.items()})
print({k: v ** 2 for k, v in simpledict.items() if v % 2 == 0})

# exercise
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'm', 'n', 'n']
print(set([char for char in some_list if some_list.count(char) > 1]))
