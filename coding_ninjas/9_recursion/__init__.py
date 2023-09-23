'''
Recursion is where a function calling itself.

PMI is the math behind recursion is itself based on PMI.
principle of mathematical induction - concept that is used to prove mathematical concepts.
eg:
we can use PMI to prove sum of n natural numbers. ie, n(n+1)/2
f is true for all natural numbers.

steps to solve:
> first prove it is true for first N natural numbers.
> Assume f(k) is true
> Prove f(k+1) is true.

Think these Qs while implementing recursion:
what is my base case?
what is my hypothesis?
what is the induction step I need to take care about?

'''


# factorial program
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


print(fact(90))


# find power of a raised to b
def power_n(a, b):
    if b == 0:  # any number raised to power of 0 is 1
        return 1
    elif b == 1:
        return a
    else:
        return a * power_n(a, b - 1)


print(power_n(5, 5))

'''
first prove base case
once you prove base case,we can assume f(k) is true <-- here extended version of PMI says we can prove for f(k+1), 
f(k+2) etc.,
using the above prove f(k+1) is true
'''


# Fibanacci numbers
def fib(n):
    if n == 1 or n == 2:
        return 1
    fib_n_1 = fib(n - 1)
    fib_n_2 = fib(n - 2)
    output = fib_n_1 + fib_n_2
    return output


print("fibanacci series")
print(fib(4))


# Sum of n natural numbers
def print_n_naturals(n):
    if n == 0:
        return

    print_n_naturals(n - 1)
    print(n)
    return


print_n_naturals(15)

print()
print()


def fun(n):
    if (n == 4):
        return n
    else:
        return 2 * fun(n + 1)


print(fun(2))


# array sum

def SumArray(arr):
    l = len(arr)
    if l == 1 or l == 0:
        return arr
    return sum(arr)


print(SumArray((1, 2, 3)))


# is x in arrai
def is_present(arr, x):
    n = len(arr)
    # Base case: If the array is empty, x is not present.
    if n == 0:
        return False

    # Check if the first element of the array is equal to x.
    if arr[0] == x:
        return True

    # Recursive case: Check the rest of the array.
    return is_present(arr[1:], x)