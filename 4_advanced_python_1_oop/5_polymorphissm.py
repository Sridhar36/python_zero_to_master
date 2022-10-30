'''
ploymorphism :
Well, poly means many and more ism means form so many forms.Now we know that methods belong to objects, right?
We use the self keyword to act upon the object that got instantiated.
Now in Python, this idea of polymorphism refers to the way in which object classes can share the same method name.
But those method names can act differently based on what object calls them.
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


wizard1 = Wizard('sridhar', 50)
archer1 = Archer('robin', 100)

# ploymorphism example: each object taking a different form
for char in [wizard1, archer1]:
    char.attack()
