'''
Certainly! Let's go through the differences between lists, tuples, sets, and dictionaries in Python, along with some examples for each.

List:
A list is an ordered collection of elements that can be of different data types.
Lists are mutable, which means you can change their contents (add, remove, or modify elements).
They are defined using square brackets [].
Example:

python
Copy code
# Creating a list
fruits = ['apple', 'banana', 'orange', 'grape']

# Accessing elements
print(fruits[0])  # Output: 'apple'

# Modifying elements
fruits[1] = 'pear'
print(fruits)  # Output: ['apple', 'pear', 'orange', 'grape']

# Adding elements
fruits.append('kiwi')
print(fruits)  # Output: ['apple', 'pear', 'orange', 'grape', 'kiwi']

# Removing elements
fruits.remove('orange')
print(fruits)  # Output: ['apple', 'pear', 'grape', 'kiwi']
Tuple:
A tuple is an ordered collection, similar to a list, but it is immutable, meaning once you create it, you cannot change its elements.
Tuples are defined using parentheses ().
Example:

python
Copy code
# Creating a tuple
coordinates = (10, 20)

# Accessing elements
print(coordinates[0])  # Output: 10

# Attempting to modify elements (This will raise an error)
# coordinates[0] = 5  # TypeError: 'tuple' object does not support item assignment
Set:
A set is an unordered collection of unique elements (no duplicates allowed).
Sets are mutable, meaning you can add or remove elements, but the elements themselves must be immutable (e.g., numbers, strings).
Sets are defined using curly braces {} or the set() constructor.
Example:

python
Copy code
# Creating a set
prime_numbers = {2, 3, 5, 7, 11}

# Adding elements
prime_numbers.add(13)
print(prime_numbers)  # Output: {2, 3, 5, 7, 11, 13}

# Removing elements
prime_numbers.remove(5)
print(prime_numbers)  # Output: {2, 3, 7, 11, 13}
Dictionary:
A dictionary is an unordered collection of key-value pairs.
Each element in a dictionary consists of a key and its associated value, separated by a colon :.
Dictionaries are mutable, allowing you to add, modify, or remove key-value pairs.
They are defined using curly braces {} with the format {key: value}.
Example:

python
Copy code
# Creating a dictionary
student = {
    'name': 'John Doe',
    'age': 25,
    'major': 'Computer Science'
}

# Accessing values
print(student['name'])  # Output: 'John Doe'

# Modifying values
student['age'] = 26
print(student)  # Output: {'name': 'John Doe', 'age': 26, 'major': 'Computer Science'}

# Adding new key-value pairs
student['gpa'] = 3.8
print(student)  # Output: {'name': 'John Doe', 'age': 26, 'major': 'Computer Science', 'gpa': 3.8}

# Removing a key-value pair
del student['major']
print(student)  # Output: {'name': 'John Doe', 'age': 26, 'gpa': 3.8}
In summary, the main differences are:

Lists and dictionaries are ordered, while sets are unordered, and tuples maintain the order but are immutable.
Lists and dictionaries can store elements of different types, while sets and tuples can store elements of the same or different types.
Lists, sets, and dictionaries allow duplicates, but sets automatically remove duplicates by their nature.
Lists, sets, and dictionaries are mutable, meaning they can be modified after creation, while tuples are immutable, meaning their contents cannot be changed after creation.

'''