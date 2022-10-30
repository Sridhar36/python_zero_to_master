# string - Strings are Arrays. Like many other popular programming languages, strings in Python are arrays of bytes
# representing unicode characters.

# string concatnation - only works with Strings
print("heloo" + " sridhar")

# escape sequenece

# issue - weather = "It's "kind of " sunny"
# escape sequenece is adding a '\'
# whatever comes after \ is a string , we are defining
# \t - tab space  |  \n - next line

weather = "It's \"kind of \" sunny"
print(weather)

# formatted strings -  better way of printing using f - new feature of Python 3
name = "Sridhar"
age = 25
print(f"hi {name}, your age is {age}.. pls confirm")

# string indexing
# [start:stop:step]
print(name[0:5])
print(name[5:7])
print(name[-7:-5])
print(name[::-1])

# strings are immutable.. you cannot change string values

# Strings built-in functions
# str(), int(), float(), type(), abs(), round() - some built functions egs
# for stringgs we have below
# len()
print(len(name))

# find()

quote = "you got to be quick"
print(quote.find('be'))  # prints index of found substring
