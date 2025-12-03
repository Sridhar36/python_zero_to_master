# def my_decorator(func):
#     def wrapper():
#         print("Before function runs")
#         func()
#         print("After function runs")
#     return wrapper
#
#
# @my_decorator
# def my_function():
#     print("Inside the function")
#
#
# my_function()
#
#
# users = [
#     {"name": "Sridhar", "age": 30},
#     {"name": "Ayaan", "age": 1},
#     {"name": "Ravi", "age": 35},
# ]
#
# sorted_users = sorted(users, key=lambda u: u["age"])
# print(sorted_users)
#
# # this is tests
#
# tests = [
#     {"id": 1, "priority": "P2"},
#     {"id": 2, "priority": "P0"},
#     {"id": 3, "priority": "P1"},
# ]
# priority_order = {"P0": 0, "P1": 1, "P2": 2}
#
#
# sorted_tests = sorted(tests, key=lambda t: priority_order[t["priority"]])
# print(sorted_tests)

def log_decorator(func):
    def wrapper():
        print(f"Calling {func.__name__}")
        result = func()
        print(f"Finished {func.__name__}")
        return result
    return wrapper

def say_hello():
    print("Hello")

# Manually decorating
decorated = log_decorator(say_hello)
decorated()


# decorators with args and kwargs
# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"[LOG] Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         print(f"[LOG] {func.__name__} returned {result}")
#         return result
#     return wrapper
#
# @log_decorator
# def add(a, b):
#     return a + b
#
# add(2, 3)

# Without wraps, the decorated function loses its name/docstring:
from functools import wraps

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def add(a, b):
    """Add two numbers"""
    return a + b

print(add.__name__)   # 'add', NOT 'wrapper'
print(add.__doc__)    # "Add two numbers"





def sample_args(*args):
    print(args)

def sample_kwargs(**kwargs):
    print(kwargs)

sample_args(1,2,3,4)
sample_kwargs(a=1,b=2,c=3)



nums = [1, 2, 3, 4]

result = map(lambda x: x*x, nums)
print(list(result))    # [1, 4, 9, 16]

