'''
args vs kwargs:

'''


# def super_func(args):
#     return sum(args)
#
#
# super_func(1, 2, 3, 4, 5)  # gives error - TypeError: super_func() takes 1 positional argument but 5 were given

# now lets add * , which says that any number of positional arguments can be added.
def super_func(
        *args):  # here instead of *args we can give any name like *dummies etc.. butt standard way is to use *args a per python community guidelines
    print(args)  # prints tuple of arguments i.e arguments given to function are converted inside function to tuple
    return sum(args)


print(super_func(1, 2, 3, 4, 5))


def superfunc(*args, **kwargs):
    print(kwargs)
    total = 0
    for items in kwargs.values():
        total = total + items
    return sum(args) + total


print(superfunc(1, 2, 3, 4, 5, num1=5, num2=19))

# Rule for order:
# params, *args, default parameters, **kwargs
