'''
Special data types in Python:

Remember this list at the beginning of the course where I talked about the data types that comes with Python, and then
we learned about classes and how we're able to create our own data types, our own objects in Python. But we also have
these specialized data types that come as well built into the Python standard library, which are really, really nice.
And this can make our programs really, really powerful. Now they're specialized because you're not going to see them
everywhere, but it's good to know that
'''

from collections import Counter, defaultdict, OrderedDict

# 1 counter
li = [1, 2, 3, 4, 5, 6, 7, 7]
print(Counter(li))
'''
Seven now has two. So what it does is it creates a dictionary that keeps track of how many times an item occurred in an 
iterable. So that seven occurred twice. So seven has a value of two. Another way we can use this is let's say we have a \
sentence and say in the sentence, I want to check.
'''

sentence = 'blah blah blabh blah ajhbutfeyc iyvgsriuyfhbksj  vsjuytevc'
print(Counter(sentence))

'''
Because this type of calculation of a counter of turning an item like a list into what we call a hash map or a 
dictionary like this to keep count is actually a very useful function that you see all over programming. It actually 
helps a lot with optimization problems. Now, we're not going to get into it there, but I just want to show you that 
counter is something that is really, really useful if you want to count duplicate users or duplicate emails.
Counter can be really, really useful.'''

# 2 default dict

dick = {'a': 1, 'b': '2'}
print(dick['a'])  # works
# print(dick['c'])  # key error

dick1 = defaultdict(lambda: 'does not exist', {'a': '1', 'b': '2'})
print(dick1['v'])  # prints does not exist

# 3 ordered dicts:
'''
TIP:

Recently, the Python has made Dictionaries ordered by default! So unless you need to maintain older version of Python 
(older than 3.7), you no longer need to use ordered dict, you can just use regular dictionaries!

An OrderedDict is a dictionary subclass that remembers the order that keys were first inserted. The only difference 
between dict() and OrderedDict() is that: OrderedDict preserves the order in which the keys are inserted. A regular dict
doesn’t track the insertion order and  iterating it gives the values in an arbitrary order. By contrast, the order the 
items are inserted is remembered by OrderedDict.
'''

# 4 date time module:

import datetime
from time import time

print(datetime.date.today())  # prints today's date
print(time())

# 5 Array - arrays takes less memory and perform faster
# faster then lists
from array import array

arr = array('i', [1, 2, 3])
print(arr[0])
