'''
Scope - what variables do I have access to?
when variables / methods not accessible Python interpreter throws an error
'''

# gloabl scope
a = 100


def sun_func():
    total = 100


# this is not possible since the variable has a function scope only
# print(total)


if True:
    x = 10
print(x)  # this is posible since x has global scope

# 2.  scope rules:
b = 1


def confusion():
    b = 5
    return b


print(b)  # 1  - because for global scope b value is 1
print(confusion())  # 5 # confusion assigns b = 5 and returns b


# 1 - start with local
# 2 - Parent local ?
# 3 - Global
# 4 - built in python functions


# 3 global keyword - to give global instance
# 4 non local keyword:
def outer():
    x = "local"

    def inner():
        nonlocal x  # declaring as non local we can change the value of outer x as well
        x = "nonlocal"
        print("inner : ", x)

    inner()
    print("outer : ", x)


outer()  # prints -


# inner :  nonlocal
# outer :  nonlocal

def outer():
    x = "local"

    def inner():
        # nonlocal x # declaring as non local we can change the value of outer x as well
        x = "nonlocal"
        print("inner : ", x)

    inner()
    print("outer : ", x)


outer()  # prints - inner :  nonlocal
# outer :  local


'''
why using scope?
machines will not have unlimited space. We have to be careful about the memory space we are allocating.
To use same memory - we can have scope

like if we declare a variable as global and use the same.. then we are using same memory.
eg:
if we declare x globally and use same 'x' by using global keyword in all the methods, then technnically we are using the 
same space., Or if we declare multiple variables then it means we are creating multiple memory instances.
'''

'''
imposter syndrome: The idea of you thinking you are not good enough..!
Dont feel bad.. trust the process.. keep repeating and practicing.
Over the time you'll improve. 
'''
