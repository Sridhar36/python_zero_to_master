'''
Inheritance is a fundamental concept in object-oriented programming that allows one class (called the child or subclass)
to inherit properties and behaviors from another class (called the parent or superclass). This means that a subclass
can reuse and extend the attributes and methods of its parent class.

Inheritance promotes code reusability and enables the creation of a hierarchy of related classes.
'''


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


# Create instances of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak method on each object
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!

'''
In this example, we have a parent class called Animal, which has an __init__ method to initialize the name attribute 
and a speak method. The speak method in the Animal class is a placeholder method (defined with pass) because it doesn't
 make sense for an animal to have a generic sound.

We then create two child classes, Dog and Cat, which inherit from the Animal class. These child classes override the 
speak method to provide specific behavior for dogs and cats.

When we create instances of Dog and Cat, they inherit the name attribute from the Animal class and the overridden speak
 method from their respective child classes. As a result, when we call the speak method on each object, it returns the 
 appropriate sound for each animal.

Inheritance allows you to create a hierarchy of classes, with more specialized subclasses inheriting and extending the 
functionality of more general superclasses, making your code more organized and efficient.
'''

# Types of Inheritence:


'''
Super() : to refer the attributes of Super class from my child class. Super class is parent class.
The super() keyword in Python is used in inheritance to call a method or constructor from a parent class (superclass) 
within a subclass. It allows you to access and invoke methods or attributes of the superclass, which can be useful for 
extending or overriding the behavior of the parent class.

Here's a neat and clear example to illustrate how the super() keyword is used in inheritance:
'''


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class constructor
        self.breed = breed

    def speak(self):
        super().speak()  # Call the speak method of the parent class
        print(f"{self.name} barks")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Call the parent class constructor
        self.color = color

    def speak(self):
        super().speak()  # Call the speak method of the parent class
        print(f"{self.name} meows")


# Create instances of Dog and Cat
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Calico")

# Call the speak method for Dog and Cat
dog.speak()
cat.speak()

'''
In this example:

We have a parent class Animal with an __init__ constructor that initializes the name attribute and a speak method that 
prints a generic sound.

We create two child classes, Dog and Cat, that inherit from the Animal class.

In the Dog and Cat constructors, we use super().__init__(name) to call the constructor of the parent class Animal, 
ensuring that the name attribute is properly initialized.

In the speak methods of Dog and Cat, we use super().speak() to call the speak method of the parent class Animal before 
adding the specific behavior for each subclass.

When we create instances of Dog and Cat and call their speak methods, the super() keyword ensures that the speak method 
of the parent class is invoked before the subclass-specific behavior. This allows us to reuse and extend the 
functionality of the parent class while customizing it for each subclass.

The output will be as follows:

Buddy makes a sound
Buddy barks
Whiskers makes a sound
Whiskers meows

As shown in the output, the super() keyword helps maintain and build upon the functionality of the parent class within the child classes
'''

'''
types of Inheritance:

Single Inheritance:
Single inheritance occurs when a class inherits from only one parent class.
'''


class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


dog = Dog()
print(dog.speak())  # Output: Woof!

'''
Multiple Inheritance:
Multiple inheritance happens when a class inherits from more than one parent class.
'''


class Bird:
    def fly(self):
        return "Flying"


class Dog:
    def bark(self):
        return "Barking"


class Pet(Dog, Bird):
    def play(self):
        return "Playing"


pet = Pet()
print(pet.bark())  # Output: Barking
print(pet.fly())  # Output: Flying

'''
Multilevel Inheritance:
Multilevel inheritance occurs when a class inherits from a superclass, which in turn inherits from another superclass.
'''


class Grandparent:
    def greet(self):
        return "Hello, I'm the Grandparent."


class Parent(Grandparent):
    def introduce(self):
        return "I'm the Parent."


class Child(Parent):
    def say_hello(self):
        return "Hello, I'm the Child."


child = Child()
print(child.greet())  # Output: Hello, I'm the Grandparent.
print(child.introduce())  # Output: I'm the Parent.
print(child.say_hello())  # Output: Hello, I'm the Child.

'''
Hierarchical Inheritance:
Hierarchical inheritance involves multiple classes inheriting from a single parent class.

Example:
'''


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius * radius


class Rectangle(Shape):
    def area(self, length, width):
        return length * width


circle = Circle()
rectangle = Rectangle()
print(circle.area(5))  # Output: 78.5
print(rectangle.area(4, 6))  # Output: 24

'''
Hybrid Inheritance:
Hybrid inheritance is a combination of any two or more types of inheritance mentioned above. It can be a mix of single, multiple, multilevel, or hierarchical inheritance.

Example:
'''


class A:
    def method_A(self):
        return "Method A"


class B(A):
    def method_B(self):
        return "Method B"


class C(A):
    def method_C(self):
        return "Method C"


class D(B, C):
    def method_D(self):
        return "Method D"


d = D()
print(d.method_A())  # Output: Method A
print(d.method_B())  # Output: Method B
print(d.method_C())  # Output: Method C
print(d.method_D())  # Output: Method D
