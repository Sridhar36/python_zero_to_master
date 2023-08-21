def combine_alternate_characters(str1, str2):
    combined = ''.join([c1 + c2 for c1, c2 in zip(str1, str2)])
    return combined


# Example input
str1 = "Automation"
str2 = "Testing"

result = combine_alternate_characters(str1, str2)
print(result)

'''
The zip() function in Python is used to combine two or more iterables (such as lists, tuples, or strings) element-wise 
into an iterator of tuples. Each tuple contains elements from the input iterables at the same index. It stops when the shortest input iterable is exhausted.

Here's how the zip() function works:

python
Copy code
zip_iterator = zip(iterable1, iterable2, ...)
iterable1, iterable2, ...: The iterables you want to zip together.
The result of the zip() function is an iterator. To get a list of tuples or other iterable, you can convert it to a list using list().

Example usage:

python
Copy code
numbers = [1, 2, 3]
letters = ['A', 'B', 'C']
zipped = zip(numbers, letters)

# Convert the iterator to a list of tuples
zipped_list = list(zipped)
print(zipped_list)
'''

numbers = [1, 2, 3]
letters = ['A', 'B', 'C']
zipped = zip(numbers, letters)
zipped_list = list(zipped)
print(zipped_list)


# withou zip function:
def combine_alternate_characters(str1, str2):
    combined = ""
    min_len = min(len(str1), len(str2))  # Find the minimum length of the two strings

    # Combine characters alternately up to the length of the shorter string
    for i in range(min_len):
        combined += str1[i] + str2[i]

    # Add any remaining characters from the longer string
    combined += str1[min_len:] + str2[min_len:]

    return combined


# Example input
str1 = "Automation"
str2 = "Testing"

result = combine_alternate_characters(str1, str2)
print(result)
