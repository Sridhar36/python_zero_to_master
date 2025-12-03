from abc import ABC, abstractmethod

# Encapsulation: Hiding implementation details within the class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand  # public attribute
        self.__model = model  # private attribute (encapsulation)

    # Getter method (encapsulation)
    def get_model(self):
        return self.__model

    # Setter method (encapsulation)
    def set_model(self, model):
        self.__model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.__model}")


# Abstraction: Using abstract base class (ABC) and abstract methods
class Engine(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


# Inheritance: A Car class inherits from Vehicle and Engine
class Car(Vehicle, Engine):
    def __init__(self, brand, model, fuel_type):
        Vehicle.__init__(self, brand, model)  # Initialize parent class (Vehicle)
        self.fuel_type = fuel_type

    # Implementing abstract methods (polymorphism)
    def start_engine(self):
        print(f"The {self.brand} {self.get_model()} engine is starting...")

    def stop_engine(self):
        print(f"The {self.brand} {self.get_model()} engine is stopping...")

    def display_info(self):
        # Overriding the parent class method (polymorphism)
        print(f"Brand: {self.brand}, Model: {self.get_model()}, Fuel Type: {self.fuel_type}")


# Polymorphism: Same method name but different behavior
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model, "Electric")
        self.battery_capacity = battery_capacity

    # Overriding start_engine method for ElectricCar
    def start_engine(self):
        print(f"The electric engine of {self.brand} {self.get_model()} is now running silently...")

    def display_info(self):
        # Overriding display_info method for ElectricCar
        print(f"Brand: {self.brand}, Model: {self.get_model()}, Fuel Type: {self.fuel_type}, Battery Capacity: {self.battery_capacity} kWh")


# Create objects and demonstrate OOP concepts
vehicle = Vehicle("Generic", "Model X")
vehicle.display_info()

car = Car("Toyota", "Corolla", "Petrol")
car.display_info()
car.start_engine()
car.stop_engine()

electric_car = ElectricCar("Tesla", "Model S", 100)
electric_car.display_info()
electric_car.start_engine()
electric_car.stop_engine()
