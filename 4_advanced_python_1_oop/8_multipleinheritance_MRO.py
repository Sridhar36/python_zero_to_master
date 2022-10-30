'''
multiple inheritance: Inheriting from two parent classes.,
'''


class User:
    def sign_in(self):
        print('logged in!')


class Wizard(User):  # pass parent class in braces to inherit
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with the power od {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')

    def run(self):
        print("ran really fast")


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


wizard1 = Wizard('sridhar', 50)
archer1 = Archer('robin', 100)

hb1 = HybridBorg('borgie', 50, 100)
print(hb1.__dict__)

'''MRO - method resolution order
mro or method resolution order is a rule that Python follows to determine when you run a method
which one to run when you have such complicated inheritance structure.
Amro is a rule that says, Hey, do this, do this, and then do that. And that's the method that you should run.
'''


class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.num)  # prints 1
print(D.mro())  # gives the order of running/checking by interpreter
