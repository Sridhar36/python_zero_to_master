'''
In python, we have different levels of access same like any other programming language.

All class members are public by default in Python.

'''


class Geek:
    # constructor
    def __init__(self, name, age):
        # public data members
        self.geekName = name
        self.geekAge = age

    # public member function
    def displayAge(self):
        # accessing public data member
        print("Age: ", self.geekAge)


# creating object of the class
obj = Geek("R2J", 30)

# accessing the public data member
print("Name: ", obj.geekName)

# calling public member function of the class
obj.displayAge()

# ****** protected access modifier *********
'''
You cannot access the protected variables & functions outside the class.
You can access them either inside the class or in the derived classes (inherited classes).
We declare protected variables and functions with '_'
'''
