'''
Object-Oriented Programming (OOP) is a way to structure code by grouping related data and behavior together into reusable blocks called objects.

Think of it like real life —
We have objects (Car, Human, Dog, Laptop).
Each object has:

Properties (data) → What it has

Behaviors (methods) → What it does

'''


'''
🚘 Step 1: Class — Blueprint

A class is like a blueprint for making something.

Imagine you are a car company.
Before making cars, you create a blueprint that defines:

What all cars will have (attributes)

What all cars can do (methods)
'''
class Car:
    def __init__(self, brand, color):
        self.color = color  # attributes : what car has
        self.brand = brand

    def start_engine(self): # methods : what car can do
        print(f"starting engine!")

    def stop_engine(self):
        print(f"stopping engine!")

car1 = Car("Toyota", "Red")
car2 = Car("Tesla", "Black")



# encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())   # 1500

# inheritance
class ElectricCar(Car):    # inherits from Car
    def __init__(self, brand, color, battery_capacity):
        super().__init__(brand, color)   # parent class constructor
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"{self.brand} is charging...")


# polymorphism
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

for animal in [Dog(), Cat()]:
    animal.speak()
