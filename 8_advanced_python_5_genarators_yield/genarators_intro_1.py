'''

generators are very fast. And better approach to use.

difference between generator and iterable is the way we implement them
In generators we use yield, which will pause the function and comes back to it when we do something to the same..
like using next.. it is like we just tell function to yield

we create generators in Python using the range and yeild keyword

yeild

generators allow us generate a value..

A generator is a special type of thing in Python that allows us to use a special keyword called yield
and it can pause and resume functions.

for example you need a list of 100000 numbers and use same. If you create this list and try use.. Then we need to
create a list that has 100000 values then we need to access.. this is time taking and memory in-efficient
Better way to do it is to return one value from list at once using yield.
'''
