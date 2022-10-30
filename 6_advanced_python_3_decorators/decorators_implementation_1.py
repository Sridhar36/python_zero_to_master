# decorator
def my_decorator(func):
    def wrap_func():
        print('*****')
        func()
        print('*****')

    return wrap_func


@my_decorator
def sayhello():
    print("am saying helloooo!!!!!")


sayhello()

'''
What if the function hello takes arguments? for that we need to use 
Decorators with arguments
'''
print("\n decorators with arguments from here")


def my_decorator2(func):
    def wrap_func(x):
        print('*****')
        func(x)
        print('*****')

    return wrap_func


@my_decorator2
def sayhello(greeting):
    print(greeting)


sayhello("hiiii")

'''
What if there are more arguments in teh function we cannot keep adding
arguments one after the other, so we use variable number of arguments in 
decorator functions. i.e using *args and **kwargs
'''
print("\ndecorators with variable no of arguments")


def my_decorator3(func):
    def wrap_func(*args, **kwargs):
        print('*****')
        func(*args, **kwargs)
        print('*****')

    return wrap_func


@my_decorator2
def sayhello(greeting, emoji=':('):
    print(greeting, emoji)


sayhello("hiiii")
