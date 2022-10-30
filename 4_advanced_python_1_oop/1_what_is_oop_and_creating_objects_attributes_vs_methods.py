'''
What is OOP?

- we were able to create objects or use various methods using these objects wth the helo if OOP

OOP is paradigm, it is way to assume or build an application or to code.
- It helps to build organised code.
- It helps us to write code that is repeatable and memory organised.
- Object oriented programming allows us to create objects that have their own methods, attributes and Properties.
- in OOP - there is this idea of classes and objects.
class - it is blue-print of basically what we want to create.
from this blueprint we can create multiple objects.

we create the instances for a class i.e., we create objects for a class.
'''


# eg:
# creating below a class / blueprint
class BigObject():
    pass


# object creation
obj1 = BigObject()  # instansiating the class
obj2 = BigObject()
obj3 = BigObject()


# OOP
class PlayerCharacter():
    def __init__(self, name):  # constructor - this is called whenever we instantiate the clas. i.e., when we create an
        # an object of the class.
        self.name = name  # way for us to define the instance of the class. # this is attribute

    def run(self):
        print("run!!")


player1 = PlayerCharacter("Sridhar")
player1.run()


# Attributes vs methods:
class PlayerCharacter():
    # class object attribute & will have class level access
    membership = True

    # self refers to PlayerCharacter i.e., class instance
    def __init__(self, name,
                 age):  # constructor - this is called whenever we instantiate the clas. i.e., when we create an
        # an object of the class.
        self.name = name  # way for us to define the instance of the class. # this is attribute
        self.age = age

    def run(self):  # class methods should have self as parameter
        print("run!!")

    def shout(self):
        print(f'my name is {self.name}')


player2 = PlayerCharacter("Sridhar")
player2.run()
# help(player2)  # gives blueprint of object
# help(list)  # gives blueprint of list class
