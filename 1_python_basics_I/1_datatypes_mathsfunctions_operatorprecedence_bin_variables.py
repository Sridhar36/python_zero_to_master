'''
fundamental data types  in python
int
float
bool
str
list
tuple
set
dict

a data type is a value in Python, for eg:
int - numbers
str - letters


classes are custom datatypes

specialized data types we can use from modules.

None -  means nothing , like a zero in maths.

complex datatypes

'''

# Maths functions
# round - rounds down to a number
print(round(3.999))

# abs - returns absoulte value - no negative numbers
print(abs(-49))

# operator precedence
# every operation in Maths follows an order  () -> ** -> * -> / -> + -> -


# Bin - function : returns binary representation of integer
print(bin(6))

# variables - Well, variables store information that can be used in our programs so we can hold perhaps user inputs
# like values.
'''
So let's have a look at this variables and remember this is the symbol for best practices are what we
call snake case.
Snake gas means it's all lowercase and then spaces well they don't exist.
We use underscores variables must start with a lowercase or an underscore.
Variables can be anything with letters, numbers and underscores.
But remember, they have to start with lowercase and underscore that means we can start a variable with
a number.
They're also case sensitive.
That means if I create a variable, but let's say this snake case, this variable has a capital E instead
of a lowercase E, they'll be a different variable.
And then finally you can't overwrite keywords.
Let's go through these with some examples.
First, a variable has to be in the form of a snake case.
That is, if I want to call this user IQ, I should technically have an underscore here instead of a
space just to make sure that a programmer maybe I'm working on a team can read this variable.
So that's snake case.
You also have to start your variables with either a letter or an underscore so I can technically do this and I click run.'''

# CONSTANTS should have capital letters - constants are the values that cannot be changed


# expression vs statements:
iq = 99  # statement
user_age = iq / 5  # performs an action - expression - code producing a value of o/p
# here iq / 5 is expression and statement is line above - user_age = iq / 5


# augmented assignment operator
a = 5
a += 3  # augmented assign operator i.e +=
