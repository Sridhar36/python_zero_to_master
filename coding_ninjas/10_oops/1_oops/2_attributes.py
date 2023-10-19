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
