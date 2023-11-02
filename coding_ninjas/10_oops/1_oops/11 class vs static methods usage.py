'''
In Python, both static methods and class methods are used to define methods that are associated with a class rather than
an instance of the class. They are similar in that they can be called on the class itself, rather than on instance of
 the class. However, they serve different purposes and are used in different situations. Let's explore each of them and
  differentiate them with examples:

Static Method:
A static method is a method that belongs to a class and does not depend on the state of any instance. It does not have
access to the instance's data or attributes.

You define a static method using the @staticmethod decorator, and it does not take any reference to the instance (self)
 as its first argument.

Static methods are typically used for utility functions that are related to the class but don't need access to
instance-specific data.

Here's an example of a static method:
'''


class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y


result = MathUtils.add(3, 5)
print(result)  # Output: 8

'''
In this example, the add method is a static method because it doesn't rely on any instance-specific data. You can call 
it using the class name MathUtils.add().

Class Method:
A class method is a method that is bound to the class and not to the instance. However, it does take a reference to the 
class itself (usually named cls) as its first argument. This allows class methods to access and modify class-level 
attributes or perform actions related to the class as a whole.

You define a class method using the @classmethod decorator.

Here's an example of a class method:
'''


class Dog:
    num_dogs = 0  # A class-level attribute to keep track of the number of dogs

    def __init__(self, name):
        self.name = name
        Dog.num_dogs += 1

    @classmethod
    def get_num_dogs(cls):
        return cls.num_dogs


dog1 = Dog("Buddy")
dog2 = Dog("Rex")
num_dogs = Dog.get_num_dogs()
print(num_dogs)  # Output: 2

'''
In this example, the get_num_dogs method is a class method that can access and return the num_dogs attribute, which is a
 class-level attribute.

To summarize, the key difference between static and class methods is that static methods are used for utility functions 
that are independent of the class or its instances, while class methods are used to work with class-level attributes and
perform actions related to the class itself.
'''
