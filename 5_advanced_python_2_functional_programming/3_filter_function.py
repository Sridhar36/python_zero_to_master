'''# filter
The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be
true or not

filter(function, sequence)
Parameters:
function: function that tests if each element of a
sequence true or not.
sequence: sequence which needs to be filtered, it can
be sets, lists, tuples, or containers of any iterators.
Returns:
returns an iterator that is already filtered.

Application:
It is normally used with Lambda functions to separate list, tuple, or sets.
'''

my_list = [1, 2, 3]


def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))

'''
Again if let's say we have a list of users. In that case, we might want to filter out based on users, starting with the 
name A. We can use the filter function to filter through all the usernames. And only have a new list with the usernames 
with letters, starting with a. Another very useful function.'''


def check_if_A_name(name):
    return name[0] == 'A' or name[0] == 'a'


names = ['Ashwin', 'sridhar', 'gutum', 'arun', 'ayush']
print(list(filter(check_if_A_name, names)))

'''eg:2'''


# function that filters vowels
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False


# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(fun, sequence)

print('The filtered letters are:')
for s in filtered:
    print(s)
