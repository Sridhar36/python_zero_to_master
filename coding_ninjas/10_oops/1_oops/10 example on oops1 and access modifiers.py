class Product:
    __count = 0

    def __init__(self, name, price, discount):
        self.__id = self.__count + 1
        self.__name = name
        self.__price = price
        self.__discount = discount
        self.__isAvailable = True

        Product.__count = Product.__count + 1

    @staticmethod
    def checkOwner(product):  # this is a utility method
        # just checks whether or not product belongs to a company, this doesnot require instance of class so we made
        # static
        return product.getName().startswith('CN_')

    @classmethod
    def totalProducts(cls):
        # total products is nothing but how many objects of this class are created.Basically dependent on class so we
        # created a class method
        return cls.__count

    # below three are instance methods
    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price - self.__price * self.__discount

    def getId(self):
        return self.__id


prod = Product("CN_washine_machine", 5000, 0.15)
print(prod.checkOwner(prod))
print(prod.getPrice())

