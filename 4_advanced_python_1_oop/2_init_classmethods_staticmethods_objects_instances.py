'''class methods vs static methods'''


class PlayerCharacter():
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):  # class methods should have self as parameter
        print("run!!")

    def shout(self): pass

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    # we can even instantiating class instances from the class methods using cls like shown below
    # in class methods we have to class instance using cls
    @classmethod
    def add_age(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    # in static we dont have self or cls
    # we dont care about attributes or state of the class
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


# we are instantiating the PlayerCharacter class by creating the player1 object
player1 = PlayerCharacter('Tome', 20)
print(player1.adding_things(5, 5))  # by using class object, we are calling the method

# BUT for claasmethods we need not instantiate the class. LIke shown in example below
print(PlayerCharacter.adding_things(3, 3))

# creating instance using class methos
player3 = PlayerCharacter.add_age(20, 3)
print(player3.age)


