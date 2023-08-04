# split
str = "my name is sridhar"
li = str.split()
print(li)  # ['my', 'name', 'is', 'sridhar']

li = str.split(' ', 1)  # delimeter to split # here it splits to two strings
print(li)  # ['my', 'name is sridhar']

# replace
str = "my name is sridhar"
new_str = str.replace("sridhar", "kavya")
print(new_str)  # my name is kavya

str = "my name is sridhar sridhar sridhar"
new_str = str.replace("sridhar", "kavya")
print(new_str)  # my name is kavya kavya kavya

str = "my name is sridhar sridhar sridhar"
new_str = str.replace("sridhar", "kavya", 1)
print(new_str)  # my name is kavya

# find - to find a particular substring in a string. Find returns index of substring found in string
str = "My name is sridhar"
index = str.find("na")
print(index)

# lower upper
lowered_str = str.lower()
print(lowered_str)  # my name is sridhar
uppered_str = str.upper()
print(uppered_str)  # my name is sridhar

# starts-with : returns the boolean value
a = str.startswith("My")
print(a)  # True
