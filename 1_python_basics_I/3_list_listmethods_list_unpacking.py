'''
an ordered sequence of objects of any data types. Lists are mutable.
eg: list_a = [1,2, 'wer', True]

-lists are extremely important.. just like in another programming languages we have arrays
-List is a Data structure.. basically a way of organizing the data.

'''

# eg for list
amazon_cart = ['notebooks', 'sunglasses']
print(amazon_cart[0])

# List slicing
print("\nlist slicing")

amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

amazon_cart[0] = 'mobiles'
print(amazon_cart)

# you can create a new list from an existing list
new_cart = amazon_cart[0:2]
print("\nAmazon_cart - ", amazon_cart)
print("\nNew cart - ", new_cart)

# if you want to copy a list and create a new list
newreplica_cart = amazon_cart[:]  # this is right way of copying
# if you do newreplica_cart  = amazon_cart  --  here new list will simply point to same memory of Amazon cart
print("copied list\t-", newreplica_cart)

''' Matrix - lists of lists  | in java array of arrays 
'''
print("\n matrix from here ")
matrix = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]
print(matrix)
print(matrix[0][1])

'''list methods '''
print("\nlist methods from here ")
basket = [1, 2, 3, 4, 5, 6, 7]
print(len(basket))

# to add elements to list - append()
basket.append("amazon dabba")  # at the end
basket.insert(2, "neee abba")  # at the given index
basket.extend([1, 2, 3, 4, 5])  # to add iterable, like a list
print(basket)

# to remove
print(basket)
basket.pop()  # pops whatever is at the end of the list or we can give pop(index)
basket.remove("neee abba")  # to remove a value.. unlike pop where we give the index.
# basket.clear() - to empty the list, removes everything
print(basket)

# to get the index of value in the list - .index() method
print(basket.index("amazon dabba"))

# in keyword - to check if a value is present in a list
print("amazon dabba" in basket)

# count keyword - gives the count of number of times a value occur in a list
print(basket.count(1))

# sort method - to get the sorted list
# basket.sort() - modifies existing list
# sorted(basket) - creates new sorted copy of list

newlst = ['a', 'v', 'b', 'h', 'z']
newlst.sort()
newlst.reverse()  # reverses the list  or use newlst[::-1]
print(newlst)

print(list(range(100)))  # to create list of range 100 real quick

'''.join()'''
# works on strings and lists
sentence = ''
newsentence = sentence.join(['hi', 'my', 'name', 'is', 'sridhar'])
print(newsentence)
# instead of above two lines we can use below.. directly giving empty string
newsentence = " ".join(['hi', 'my', 'name', 'is', 'sridhar'])
print(newsentence)

# list unpacking
a, b, c, d, *other = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)
print(other)

# None - we use when we not sure what is the value currently - nothing
