''' Inheritance:
inheritance allows new objects to take on the properties of existing objects. So you can inherit classes.

'''


# not having init in class is also fine
# Shouldn't we have that init method that gets run first? Well, we could, but if we don't have any variables or
# attributes that we want to assign to the user, well, in that case we wouldn't need an A method.
# So for now, we'll just say that we don't need there's nothing that the user has other than this sign

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


wizard1 = Wizard('sridhar', 50)
archer1 = Archer('robin', 100)
wizard1.attack()
archer1.attack()

'''
If I click attack here and I run. See that I'm attacking with power of 50. If I do, archer one dot attack.
In that case, I'll get attacking with arrows.Arrows left 100.But both of these have the sign in function at the same time.
How cool is that? This is the power of inheritance.We're keeping our code dry, right?
We're abstracting away the part of the code that they both share, but then changing things according
to what each one needs.So for example, I could have different methods and properties on Wizard than the Archer, but also
have a shared user's user functionality that they have.And this way it keeps our code organized and clean.Now let's 
bring back the zoom in just so you can see it clear.Now, this idea of inheritance is really, really powerful.
And the key here is that we have a parent class and children classes.
Now, sometimes these children classes are called subclasses or derived classes because they're subclasses'''

''' isinstance:
Now Python gives us a useful tool to check if something is an instance.Of a class.
And easily enough for us.It's called instance.
Or is instance and is instance is a built in function in Python.
We give it the instance and then the class that we want to check.'''
print(isinstance(wizard1, Wizard))  # gives True

'''
But here is the interesting part.
If I do wizard1. (i.e., classobject.)
Do you see how I have our methods and attributes that I've added, but also all these Dunder methods
that we haven't really talked about yet?Where do these come from?Right.Well.

In Python.
Remember how I said everything is an object?
Well, everything in Python inherits from the base object class that Python comes with, and it's calledobject.
You see how it got highlighted here?So if I do, is instance wizard one of object?
Oh, and I have to remove the dot over here.Let's click Run.
It's true because Wizard One inherits or gets methods from the Wizard class, from the user class,
and even higher up from the object based class that Python comes with.And that's why we have these automatic methods 
attached for us.So that using object every single method that is useful.
For example, if I open up a list, if I do dot and let's say we pick the.
Our EPR method, which we don't really know what it does yet.
But if I go to a wizard one.And I do dot you see that I have it as well because they both inherit from the object base 
class and this way we avoid repeating code.
Any common functionality, I can just dish it out to all the objects that need it, which is very,
very cool.
So underneath the hood, when I do something like user, it's actually accepting object as the parent
class in order to accept these properties that are built in and that we might need in the future.'''
