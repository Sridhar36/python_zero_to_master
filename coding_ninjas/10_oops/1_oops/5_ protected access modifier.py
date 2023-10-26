# ****** protected access modifier *********
'''
You cannot access the protected variables & functions outside the class.
You can access them either inside the class or in the derived classes (inherited classes).
We declare protected variables and functions with '_'
'''


# Super class

class Student:
    # protected data members or variables
    _name = None
    _roll = None
    _branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch

    # protected member function
    def _displayRollAndBranch(self):
        # accesing protected data members
        print("Roll : ", self._roll)
        print("Branch: ", self._branch)


class Geek(Student):  # Geek inheriting from Student

    # constructor
    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)

    # public member function
    def displayDetails(self):
        # accessing protected data members of Super Class
        print("Name: ", self._name)

        # accessing protected member functions of Super class
        # here we are able to access the below protected member of Student class is only because Geek is inheriting the
        # Student class
        self._displayRollAndBranch()


# creating objects of the derived class
obj = Geek("R@J", 170356, "IT")

# callling public member functions of the class
obj.displayDetails()
