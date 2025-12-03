# b = "Hello, World!"
# print(b[2:5])
#
# print(b[-2:])
# print(b[2:5])
# print(b[2:5])

a = " Hello, World!,,,,,,,      "
print([w[::-1] for w in a.strip().replace(',', '').split()])




#
# # 1. Remove whitespace
# a = a.strip()
#
# # 2. Remove commas
# a = a.replace(",", "")
#
# # 3. Split into words
# words = a.split()
#
# # 4. Reverse the words
# reversed_words = words[::-1]
#
# print(reversed_words)



#
# a = " Hello, World!,,,,,,,      "
# print(a.strip()) # returns "Hello, World!"
#
# # print(a.strip().upper())
# print(a.strip(','))
# # print(a.lower())
#
# b = a.strip()
#
#
# # reverse a string
# print(a.strip().split())
# print(a[::-1])
# #
#
# # str.split(separator, maxsplit)
# text = "apple,orange,banana,grape"
# result = text.split(",")  # Split by comma
# print(result)
#
# # str.replace(old, new, count)
# text = "hello world"
# result = text.replace("world", "Python")
# print(result)
#
# text = "apple apple apple"
# result = text.replace("apple", "orange", 2)  # Replace only the first two occurrences
# print(result)
#
# # separator.join(iterable)
# words = ["apple", "orange", "banana"]
# result = ", ".join(words)
# print(result)
# #
# #
#
#
# # longest substring
# def longest_unique(s):
#     seen = {} # where we last saw each character
#     left = 0 # start index of current window
#     best = "" # longest substring found so far
#
#     for right, ch in enumerate(s):
#         if ch in seen and seen[ch] >= left:
#             left = seen[ch] + 1
#
#         seen[ch] = right
#
#         current = s[left:right+1]
#
#         if len(current) > len(best):
#             best = current
#
#     return best
#
#
# print(longest_unique('abca'))
#
#
#
#
# def longest_substring(s : str):
#     seen = {}
#     left = 0
#     best = ""
#
#     for right, ch in enumerate(s):
#
#         if ch in seen and seen[ch] >= left:
#             left = seen[ch] + 1
#
#         seen[ch] = right
#
#         current = s[left:right+1]
#
#         if len(current) > len(best):
#             best = current
#
#     return best
#
# # # check anagram
# from collections import Counter
#
# def are_anagrams(a: str, b: str) -> bool:
#     print(Counter(a))
#     print(Counter(b))
#     return Counter(a) == Counter(b)
#
#
# # Examples
# print(are_anagrams("listen", "silent"))   # True
# print(are_anagrams("hello", "world"))     # False


def are_anagrams(a: str, b: str) -> bool:
    print(sorted(a))
    print(sorted(b))
    return sorted(a) == sorted(b)

# Examples
print(are_anagrams("listen", "silent"))  # True
# print(are_anagrams("hello", "world"))    # False


#
#
# # char freq counter
# from collections import Counter
#
# def char_frequency(s: str) -> dict:
#     return dict(Counter(s))
#
# print(char_frequency("sridhar"))
#
# # count each word
#
# from collections import Counter
#
# def word_frequency(s: str) -> dict:
#     words = s.lower().split()
#     print(words)
#     return dict(Counter(words))
#
#
# # Example
# text = "This is is name Name this"
# print(word_frequency(text))
# # {'this': 2, 'is': 2, 'name': 2}
#
#
# # remove duplicates and preserve order
# # Example
# # print(remove_duplicates_keep_order("banana"))  # "ban"
#
# def remove_duplicates_keep_order(s: str) -> str:
#     seen = set()
#     result = []
#
#     for ch in s:
#         if ch not in seen:
#             seen.add(ch)
#             result.append(ch)
#     return "".join(result)
#
#
#
# match = {')':'(', ']':'[', '}':'{'}
# print(match.values())
#
# # for i in match:
# #     print(i)
#
#
#
#
# def is_balanced(s):
#     stack = []
#     match = {')':'(', ']':'[', '}':'{'}
#
#     for ch in s:
#         if ch in match.values():
#             stack.append(ch)
#         elif ch in match:
#             if not stack or stack.pop() != match[ch]:
#                 return False
#
#     return not stack
#
#
#

# def log_decorator(func):
#     def wrapper():
#         print(f"Calling {func.__name__}")
#         result = func()
#         print(f"Finished {func.__name__}")
#         return result
#     return wrapper
#
# def say_hello():
#     print("Hello")
#
# # Manually decorating
# decorated = log_decorator(say_hello)
# decorated()

from functools import wraps

# def log_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper
#
# @log_decorator
# def add(a, b):
#     """Add two numbers"""
#     return a + b
#
# print(add.__name__)   # 'add', NOT 'wrapper'
# print(add.__doc__)    # "Add two numbers"



# from functools import wraps
#
# def repeat(n):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             result = None
#             for i in range(n):
#                 print(f"Run {i+1}/{n}")
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator
#
# @repeat(3)
# def say_hi():
#     print("Hi")
#
# say_hi()

# find duplicates

def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for i in arr:
        if i in seen:
            duplicates.add(i)
        else:
            seen.add(i)
    return list(duplicates)

print(find_duplicates([1,2,2,2,3,4,5,6,7,8,9,7]))


arr = [2, 3, 2, 5, 3, 2]

counts = {}
for x in arr:
    counts[x] = counts.get(x, 0) + 1

print(counts)


# How many unique items are repeated in [1,2,2,3,3,3,4]?
from collections import Counter

counts = Counter([1,2,2,3,3,3,4])
print([item for item, value in counts.items() if value>1])




# Return True if the list [1,2,3,4,2] has duplicates
# Find all duplicate names in ["Alice", "Bob", "Alice", "Charlie"]
# Find all numbers that appear more than once in [1,2,2,3,4,5,1]
#
# Count how many times each number appears in [2,3,2,5,3,2]
# Count each word in ["apple", "banana", "apple", "orange", "banana"]
# Which number appears most in [2,3,2,5,3,2]?
# Find numbers that appear exactly once in [2,3,2,5,3,2]?



# check anagram
# from collections import Counter
# def is_anagram(a,b):
#     return Counter(a)==Counter(b)
#     return Sorted(a) == Sorted(b)

# reverse string
# def reverse_string(s):
#     result = ""
#     for ch in s:
#         result = ch + result
#     return result

def rev(s):
    res = ''
    for ch in s:
        res = ch + res
    return res

print(rev("sridhar"))


def clean_string(s):
    result = []
    for ch in s:
        if ch.isalnum():
            result.append(ch)
    return "".join(result)


# Example
print(clean_string("he!!o@ 123_#"))  # "heo123


# def non_rep_chars(s):
#     counts = {}
#     for ch in s:
#         counts[ch] = counts.get(ch, 0)  + 1
#
#     for ch in s:
#         if counts[ch] == 1:
#             return ch
#
#     return -1


def non_rep_chars(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    non_rep_list = []
    for ch in s:
        if counts[ch] == 1:
            non_rep_list.append(ch)
    print(non_rep_list)

    return non_rep_list[1]

print(non_rep_chars('srrondbiidd'))


import re

def is_valid_email(email):
    pattern = "^[A-Za-z0-9._%+-]+@[A-Za-z0-9_.-]+\.[A-Za-z]{2,}$"
    return re.match(pattern, email) is not None

# check if an array is sorted

def is_sorted(nums):
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            return False
    return True


# merge two sorted arrays

def merge_sort(a,b):
    i = j = 0
    result = []

    while i <len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i+=1
        else:
            result.append(b[j])
            j+=1

    result.extend(a[i:])
    result.extend(b[j:])

    return result





def max_consecutive_char(s):
    # If string is empty, return no character and count 0
    if not s:
        return None, 0

    # Initialize: assume the best streak starts with the first character
    max_char = s[0]      # character with the longest streak so far
    max_count = 1        # length of the longest streak so far

    # Initialize current streak details
    curr_char = s[0]     # character we are currently counting
    curr_count = 1       # count of current repeating streak

    # Loop through the string starting from the second character
    for ch in s[1:]:
        # If same as previous char, increase current streak count
        if ch == curr_char:
            curr_count += 1
        else:
            # If current streak ended → check if it was the longest so far
            if curr_count > max_count:
                max_count = curr_count
                max_char = curr_char

            # Reset current streak to the new character
            curr_char = ch
            curr_count = 1

    # After the loop ends, we must check the last streak
    # (because it might be the longest and the loop won't check it)
    if curr_count > max_count:
        max_count = curr_count
        max_char = curr_char

    # Return the character with the longest streak and the streak length
    return max_char, max_count

print(max_consecutive_char("aaabbccccdd"))























