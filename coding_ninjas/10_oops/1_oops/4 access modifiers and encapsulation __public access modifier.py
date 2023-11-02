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

'''
Encapsulation:
bundling data and functions within in a single object or class.
Encapsulation in Python is achieved by using the access modifiers.

Basically we declare variables as private and protected, then write getters and setters to change the state of these
variables. 
'''


# Encapsulation Example:
# Balance here is the sensitive info. So we made it private and put in some checks.
# people accessing this can only use these methods to access balance, add & withdraw from balance but not directly
# change the balance value

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient balance")


'''
In Python, the concept of private and protected is not strictly enforced.
Only that using these _  and __  we are saying co programmers not to alter these values, and these are protected or
private. Then dev as to make sure he does not directly access them but look out for some methods.

So encapsulation in Python is more of Sudo - Encapsulation.
 
'''
