# init method is used to initialize the state of an object
# *** init method is called by default whenever an object of the class is created. We need not call it explicitly. It is
# like a constructor.
# *** Since Python auto call the __init__() Immediately after creating a new object, you can use it to initialize the
# object's attributes.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    person = Person('Jhon', 25)
    print(f"I'm {person.name}. I'm {person.age} years old.")


class Product:
    count = 0

    def __init__(self, name, price, discount):
        self.id = Product.count + 1
        self.name = name
        self.price = price
        self.discount = discount
        self.isAvailable = True

        Product.count = Product.count + 1


p1 = Product('geaser', 2000, 0.05)
p2 = Product('AC', 500000, 0.2)

print(p1.__dict__)
print(p2.__dict__)
