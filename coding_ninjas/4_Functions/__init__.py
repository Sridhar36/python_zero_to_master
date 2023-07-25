'''
Functions - keeping some lines of code inside a block and calling the block instead of writing duplicate code..

In Python, a function is a block of organized, reusable code that performs a specific task or set of tasks. Functions
help in modularizing code, making it more organized, easier to read, and maintainable. By defining functions, you can
 break down complex tasks into smaller, manageable pieces, and then reuse those pieces wherever needed. Functions play
  a crucial role in programming and are a fundamental concept in most programming languages.

To define a function in Python, you use the def keyword, followed by the function name, a set of parentheses, and a
colon. The function body is indented and contains the code that the function will execute when called.


Code Reusability: Functions allow you to define a block of code once and use it multiple times throughout your program.
 This avoids duplicating code and improves maintainability.

Modularity: Functions allow you to break down complex tasks into smaller, more manageable pieces. Each function can
handle a specific task, making the overall code more organized and easier to understand.

Abstraction: Functions provide a level of abstraction, hiding the internal implementation details and only exposing
the interface (input parameters and return values). This allows you to use the function without needing to know how
it works internally.

Encapsulation: Functions can encapsulate a series of actions into a single unit. This can make the code more secure
and protect it from unintended external influences.

Readability: Well-named functions with clear purposes make the code more readable and self-explanatory. Instead of
 having long blocks of code, you can call a function with an appropriate name, making the code easier to understand.

Testing and Debugging: Functions make it easier to test and debug code. Since each function performs a specific task,
 it becomes simpler to isolate and fix issues if they arise.

'''

'''
How function calling works ?

A global variable has to be defined before function calling. And can be defined after the function defination as well.

'''


def fun(a):
    a = a + 10
    print(a)
    print(b)


a = 12
b = 20
fun(a)

'''
global vs local
'''

a4 = 12


def func_2():
    a4 = 20
    print(a4)


print(a4)
func_2()
print(
    a4)
# though we assigned a diff value this will still print global value, since Python differentiates between this
# a4 inside function as local instance

# So if you want to change the global values from local instance, then declare local values as global.
# like done below


a4 = 12


def func_2():
    global a4
    a4 = 20
    print(a4)


print(a4)
func_2()
print(
    a4)
