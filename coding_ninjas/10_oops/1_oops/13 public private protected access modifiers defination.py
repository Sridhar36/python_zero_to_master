'''
In Python, there is no strict concept of private, public, or protected access modifiers like in some other programming
languages such as Java or C++. However, Python provides naming conventions and language features to achieve similar
access control. These conventions are not enforced by the language itself but are followed as a best practice by
Python programmers. Here's an explanation of these conventions along with a real-time example:

Public:
In Python, all methods and attributes are considered public by default, which means they can be accessed from outside
the class without any restrictions.
Public methods and attributes are typically named in lowercase or lowercase_with_underscores.
'''


# Example of a public attribute and method
class Car:
    def __init__(self, make, model):
        self.make = make  # Public attribute
        self.model = model  # Public attribute

    def start_engine(self):
        return f"Starting the engine of {self.make} {self.model}"


'''
In this example, both make and model attributes are public, and the start_engine method is also public.

Protected:
In Python, a naming convention is used to indicate protected attributes and methods. These attributes and methods are 
prefixed with a single underscore (e.g., _my_attribute or _my_method()).
By convention, these attributes and methods should be considered non-public, and users of the class should avoid 
accessing them directly. However, Python doesn't enforce this; it's more of a hint to other programmers.
'''


# Example of a protected attribute:
class Employee:
    def __init__(self, name, _employee_id):
        self.name = name
        self._employee_id = _employee_id  # Protected attribute


'''
Private:
In Python, a double underscore prefix (e.g., __my_attribute or __my_method()) is used to indicate private attributes
and methods. Private attributes and methods are name-mangled, which means their names are modified in a way that makes
them less accessible from outside the class. For example, __my_attribute becomes _ClassName__my_attribute.
'''


# Example of a private attribute:
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private attribute


class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self._employee_id = employee_id  # Protected attribute
        self.__salary = salary  # Private attribute

    def display_employee_info(self):
        return f"Name: {self.name}, Employee ID: {self._employee_id}, Salary: {self.__salary}"

    def _calculate_bonus(self, bonus_percentage):
        bonus = (self.__salary * bonus_percentage) / 100
        return f"Bonus for {self.name}: ${bonus}"

    def get_salary(self):
        return self.__salary


# Creating an employee instance
employee = Employee("Alice", 1001, 50000)

# Accessing public attributes and methods
print(employee.name)  # Public attribute: Alice
print(employee.display_employee_info())  # Public method

# Accessing protected attributes and methods (by convention)
print(employee._employee_id)  # Protected attribute: 1001
print(employee._calculate_bonus(10))  # Protected method

# Accessing private attributes (name-mangled)
# Note: It's not recommended to access private attributes directly from outside the class.
# However, it's still possible to access them using name mangling.
print(employee._Employee__salary)  # Private attribute: 50000

# Attempting to access private method (name-mangled)
# Note: Private methods are not easily accessible from outside the class.
# They are typically accessed through public or protected methods.
# Accessing them directly is not recommended.
# print(employee._Employee__calculate_bonus(10))  # Error


'''
In this example, you can see how public, protected, and private attributes and methods are used in a Python class. 
While Python does not enforce strict access control, it encourages the use of naming conventions to indicate the 
intended level of visibility and access for class members.'''
