class Product:
    company = 'Adidas'  # this is class variable

    def __init__(self, id):
        self.id = id

    def print_company(self):
        print(self.company)


class Cart:
    maxSize = 50
    count = 0

    def __init__(self, id):
        Cart.count = Cart.count + 1  # whenever an object of this class Cart is created, then this attribute count will
        # be increased. This way we can keep a count of how many Carts have been created and subsequent usage.
        self.id = id

    def printCartSize(self):
        print(self.maxSize)


p1 = Product(1)
p2 = Product(2)
print(p1.company)
print(p2.company)
'''
we get adidas printed in both above statemnets because company is class variable which is same across all instances of 
class
Adidas
Adidas
'''
print(p1.id)
print(p2.id)
'''
we get 1 and 2 printed because these are instance variables which has unique id. Each object has its own instance.
1
2
'''

cart1 = Cart(1)
cart2 = Cart(2)

'''
Easiest way to know what all attributes are existing in the class we can use dict method.
'''

print(cart1.__dict__)  # gives all instance variables of this object i.e prints {'id': 1}

# basically __dict__ is to print the instance variables of the class

print(Cart.__dict__)  # now this gives class variables of class Cart.

# Other way to do this is using vars()

print(vars(cart1))
print(vars(Cart))

'''
instance variables are bound to object. That is limited to object.
class variables are bound to class. class variables are shared by all the objects of the class.
'''


# attributes-2:
# what is the order in which we access the variables
# First instance level variables are checked , then class level
# that is first it will check if required value is in instance level, if not it goes and checks the class level.

class Car():
    company = "Toyota"

    def __init__(self, id, company):
        self.id = id
        self.company = company


car1 = Car(1, 'Suzuki')
car2 = Car(2, 'Hyundai')

print(car1.company)  # Though we have a class variable named company and instance variable named company. Here first
# priority will be given to instance variables as per order. So Suzuki gets printed.
# if you want to access class variable here then you need to use ClassName.classobject ie., Car.company

# case -2 here we only have a class variable and we are trying to access using objects.
class Student:
    name = 'Rohan'
    age = 16


s1 = Student()
s2 = Student()
print(s1.name, end=' ')
print(s2.name, end=' ')
# prints Rohan Rohan

# case 3
class Student:
    name = 'Parikh'

    def store_details(self):
        self.age = 60

    def print_details(self):
        print(self.name, end=' ')
        print(self.age)


s = Student()
s.store_details()
s.print_details()
# prints Parikh 60


# case 4
class Student:
    name = 'Parikh'

    def store_details(self):
        self.age = 60

    def print_age(self):
        print(self.age)


s = Student()
s.store_details()
s1 = Student()
s1.print_age()
# throws error : AttributeError: 'Student' object has no attribute 'age'
'''you call the print_age method on s1. However, since you didn't call the store_details method on s1, the age attribute
 is not defined for s1, and it will raise an AttributeError when trying to print it.'''




# what is self keyword?
class Dog:
    def __init__(self):
        print("Self from init ", id(self))


dog = Dog()
print("id from outside ", id(dog))

# Both returns same id. That means self refers current object that you are invoking.


# note: A class variable is shared by all instances of a class, while an instance variable is unique to each instance.
