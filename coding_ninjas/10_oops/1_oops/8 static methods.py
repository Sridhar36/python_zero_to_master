'''
Static methods: These are bound to a class rather than an object.
They do not require a class instance creation. So they are not dependent on the state of the object.
They can be called both by the class and its object.

They are like any other methods defined outside the class.
Static methods logically make sense in the context of the class.

In below class, it makes more sense to have the add numbers inside the Calculator class.

remember, static methods will not have any access to the instances of the classes.
'''


class Calculator:

    @staticmethod
    def add_numbers(num1, num2):
        return num1 + num2


print(Calculator.add_numbers(4, 5))
