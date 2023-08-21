'''
An anagram is a word or phrase formed by rearranging the letters of another word or phrase, typically using all the
original letters exactly once. In other words, two words are considered anagrams of each other if they have the same
characters, but in a different order. Anagrams are a fun and interesting way to explore the permutations of letters
within words or phrases.
'''


# this is wrong
def is_anagram(str):
    if str == str[::-1]:
        return "is anagram"
    return "not anagram"


print(is_anagram("sridhr"))


# this is correct
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters of both strings are the same
    return sorted(str1) == sorted(str2)


# Example input
str1 = "Tesla"
str2 = "Slate"

if are_anagrams(str1, str2):
    print("Yes, the strings are anagrams.")
else:
    print("No, the strings are not anagrams.")

"""
The sorted() function in Python is used to sort elements in an iterable (such as lists, tuples, or strings) and return 
a new sorted list. It does not modify the original iterable but instead returns a new sorted version.
"""
