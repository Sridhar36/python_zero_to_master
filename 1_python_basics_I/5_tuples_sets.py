'''
Tuples: tuples are immutable collection,. you cannot do object assignment.
- tuple obj doesnot support item assignment
- why tuples? why not lists?  --> if we want to restrict others from making changes. makes code
more predictable.. but really less flexible.
- faster than list.

Set:
- an unordered collection of unique objects.
- It only has unique items.
'''

mytuple = (1, 2, 3, 8, 2, 34)
myset = {1, 2, 4, 5, 6, 6, 8, 9}
print(myset)  # prints without duplicates.

mylist = [1, 2, 2, 2, 2, 43, 5, 6, 7, 7, 7, 8, 9, 8]
print(set(mylist))
# set object doesnot support indexing
print(1 in myset)
print(len(myset))

# .clear() - can be used to clear list, dicts, tuples, sets..

# Methods in sets:
your_set = {2, 3, 4, 5}
print(myset)
print(your_set)
print(myset.difference(your_set))  # removes the common items & gives only the unique ones in both as a new set
print("\n difference", myset)

# discard()
myset.discard(8)  # to remove the item from set
print(myset)

# difference_update - updates the set by removing difference
myset.difference_update(your_set)
print("\nmy set after difference update ", myset)

# intersection  gives common items in two sets
# isdisjoint : do two sets have nothing in  common
# union - to create a new set by joining two sets
# is subset
# is superset
