"""
The members of the class declared as the private are accessible within the class only. Private access modifier is the
most secure access modifier. Data members of a class are declared private by adding a double underscore '__' symbol
before data member of that class.
"""


class Geek:
    # private data members or variables
    __name = None
    __roll = None
    __branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    # private member function
    def __displayDetails(self):
        # accessing private data members
        print("Roll : ", self.__name)
        print("Roll : ", self.__roll)
        print("Branch: ", self.__branch)

    # public member function
    def accessPrivateFunction(self):
        # accessing private member function
        # here accessPrivateFunction is able to access private method because of the reason it is inside same class
        self.__displayDetails()


# creating object
obj = Geek("R@J", 170879, "IT")
obj.accessPrivateFunction()  # we are accessing private attributes of the class using a public method, which in turn
# calls a private method of the class


# The display details are displayed in a way how the owner of the class wants it to be displayed
