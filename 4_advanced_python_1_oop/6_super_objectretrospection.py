'''
ploymorphism :
Well, poly means many and more ism means form so many forms.Now we know that methods belong to objects, right?
We use the self keyword to act upon the object that got instantiated.
Now in Python, this idea of polymorphism refers to the way in which object classes can share the same method name.
But those method names can act differently based on what object calls them.

Super keyword -
to call init method of parent from chile class we can use super()
'''


class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in!')


class Wizard(User):  # pass parent class in braces to inherit
    def __init__(self, name, power, email):
        User.__init__(self, email)  # calling init of parent
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with the power od {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')


wizard1 = Wizard('sridhar', 50, "xyz")
archer1 = Archer('robin', 100, "xyz")

# ploymorphism example: each object taking a different form
for char in [wizard1, archer1]:
    char.attack()

# Object introspection - ability to determine the type of object during run time. One of the python stengths.
print(dir(wizard1))

'''
I want to talk to you about this idea of introspection. And introspection in computer programming means the ability to 
determine the type of an object at runtime.
What is runtime? That is, when the code is running, you can determine the type of an object.
And it's actually one of Python's strengths, because everything in Python is an object we can examine.
We can introspect an object and actually figure out what our code does as we're coding and then running.
And Python allows us to do introspection and inspect these objects with some nice helper functions.
This one function is called DIR. Well, if I run this. Well, give me all of the methods and attributes that the Wizard 
Instant has. So with a dir function we give it an instance and right away we get access to what it has access to.
Well, we see that we have name, power and sign in.Again, we have the sign in from the user and then we have also attack 
from the Wizard class. And this Ed that I'm using whenever I do DOT is actually using this ability of introspection to 
just list out these available methods for me, just like I have here. So this is really useful when you're trying to 
figure out what you have access to, but you may notice'''
