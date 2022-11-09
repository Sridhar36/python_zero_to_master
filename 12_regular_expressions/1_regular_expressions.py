import re

string = 'search inside the string text please!'
print('search' in string)  # prints True

print(re.search('the', string))  # <re.Match object; span=(14, 17), match='the'>

a = re.search('the', string)
print(a.span())  # gives a tuple of start index and end index of pattern that we are searching for , here (14,17)
print(a.start())  # to get at which index text starts
print(a.end())  # to get at which index text ends
print(a.group())  # part of string where there is a match

'''
or
'''

pattern = re.compile('this')  # compile allows us to give a pattern
string = 'search this inside of this text please!'
a = pattern.search(string)  # we can use compiled pattern to search
print(a)
b = pattern.findall(string)  # gives all, instances of the match
print(b)
c = pattern.fullmatch(string)  # if we have exact same strings that we compare then only it gives the match
# if not matched gives None
print(c)
d = pattern.match(string)
print(d)  # whatever matched will be given as matched object

'''
regular expressions 2 - advanced expressions
https://www.w3schools.com/python/python_regex.asp

useful website to build regular expressions :  https://regex101.com/
practice website : https://regexone.com/ 

eg:
(^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$)

^ -starts with, that is, the string should start with this group ^[a-zA-Z0-9+_.-]
+ -quantifier, that is, it indicates you can have as many groups of [a-zA-Z0-9+_.-] as you want.. nothing but how many
items as you want.
@ - as we have @ in email
[a-zA-Z0-9.-]+ - group with + sign , says again we can have as many groups as we want
$ - indicates that resource group should be at then end of string.
'''

pattern1 = re.compile(r"([a-zA-Z]).([a])")  # r stands for raw string

email_pattern = re.compile(r"(^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$)")
email = "a@a.com"
a = email_pattern.search(email)
print(a)  # <re.Match object; span=(0, 7), match='a@a.com'>
