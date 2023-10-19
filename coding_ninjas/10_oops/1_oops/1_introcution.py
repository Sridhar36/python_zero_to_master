'''
OOPS - Object oriented programming system. Any language that supports this system is called Object
oriented programming language.

Object:
Anything you see in real world can be represented as an object in programming world.
An object is instance of a class
eg: Bike --> it has identity such as unique name
         --> it has state such as Bike color
         --> it has behaviour like drive, brake, accelerate

Class:
It is a blueprint of an object. It’s just a plan which does not consume any memory.
A class is a blueprint for creating objects.
For example: If you wish to build a house on a piece of land, you would require
a map for your house. Since using same map, you can create several houses and
that map will not consume any memory.

Eg: Personal Class --> It has attributes like name, age, gender, occupation etc.,
                   --> It has functionalities like walk(), Eat(), Sleep(), Work() etc.,

'''


class Product:
    company = 'Adidas'  # this is class variable

    def print_company(self):
        print(self.company)


class Cart:
    maxSize = 50

    def printCartSize(self):
        print(self.maxSize)


p1 = Product()
print(p1.company)
p1.print_company()

# What if you try to invoke something which is not there
# eg:

# p1.name
"""
Traceback (most recent call last):
  File "C:\\Users\\sridh\PycharmProjects\pythonProject\pythonProject\zero_to_master_complete_python_2022\coding_ninjas\10_oops\1_oops\1_introcution.py", line 46, in <module>
    p1.name
AttributeError: 'Product' object has no attribute 'name'
"""

p2 = Product()
print(p2.company)
p2.print_company()

# here p1 and p2 will store the address of the objects in heap memory where objects are created.
