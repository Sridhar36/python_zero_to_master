'''
Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the
method name. Dunder here means “Double Under (Underscores)”. These are commonly used for operator
overloading. Few examples for magic methods are: __init__, __add__, __len__, __repr__ etc.

The __init__ method for initialization is invoked without any call, when an instance of a class
 is created, like constructors in certain other programming languages such as C++, Java, C#, PHP etc.
  These methods are the reason we can add two strings with ‘+’ operator without any explicit typecasting.

These are actually implemented using these dunder methods.
They allow us to use Python specific functions on objects created through our class.

we can modify the dunders as we like in our classes that we design.

'''


class SampleClass():
    def __init__(self):
        print("simple class accessed!!")

    # len dunder modified
    def __len__(self):
        return 5

    # call dunder method modified
    def __call__(self):
        return ("Yes?")


obj1 = SampleClass()
print(SampleClass())
