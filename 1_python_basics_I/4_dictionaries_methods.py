'''
-In other languages we have hashmaps, maps or objects
-A dict is key value pair
-dict is an unordered data structure , we cannot access dict values using the indexes. We are not
sure where they gets stored in teh memory.
- dict is an unordered key value pair.. as long as we know what is the key then we can get the values.
- dict keys are immutable but the values are mutable .
- keys has to unique
-

'''

dict_test = {
    'a': 1,
    'b': 2
}

print(dict_test)
print(dict_test['a'])

# dictionary methods.
# using get is a good option since it wont throw error if key not found.
# using get :

# creating dictionary
# @1
user = {
    'basket': [1, 2, 3],
    'greet': 'hello'
}
# print(user['age'])  # this will throw error since we dont the have key age
# this below approach is better way instead of above
print(user.get('age', 55))  # here we are saying that in case age doesnot exist, then add a default value
# if age key is present then it will give value.
print(user)

# @2
user2 = dict(name="sridhar")
print(user2)

# dict methods - in
print("greet" in user.keys())  # returns true
print("hello" in user.values())
print(user.items())

# user.clear()  # clears everything in dict
user3 = user.copy()  # to copy a dictionary and create new one
print(user3)

# pop reomves the values
print(user3.pop('greet'))  # removes the item from dict and returns teh removed item's value
# popitem() randomly removes items from dictionary and return values #from python 3.7 removes last item

# update - updates dict key with new value
user.update({'greet': 'hello booiiii'})  # updates the key with new value
print(user)
