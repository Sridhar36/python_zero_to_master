'''
class methods are created using the @class method DECORATOR and like static methods they do not need any instance to
invoke them.
class methods have access to class level attributes and the static methods but not the instance variables.
class methods do not need self as an argument as they do not have access to the instance of the class. But they require
another variable called the cls.
'''


class Employee:
    __company = "Coding Ninjas"

    def __init__(self, id, name, salary):
        self.__id = id
        self.__name = name
        self.__salary = salary

    @staticmethod
    def greet():
        return "Have a good day!"

    @classmethod
    def intro(cls):
        return "Welcome to " + cls.__company + ". " + cls.greet()


print(Employee.intro())

"""
Instance methods:
These are most common methods we work with in Python.
These methods must have self as a parameter.
These are used to read, modify instance of class or do some operations on instance of the class.

Remember, static and class methods can also invoked by using instance variables.
"""


class Employee:
    __company = " Coding Ninjas "

    def __init__(self, id, name, salary):
        self.__id = id
        self.__name = name
        self.__salary = salary

    def employeeDetails(self):
        return "Name: " + self.__name + "\nId: " + str(self.__id) + "\ncompany: " + self.__company


emp1 = Employee(1, "Ramu", 9000)
emp2 = Employee(2, "Sima", 9000)

print(emp1.employeeDetails())
print(emp2.employeeDetails())
