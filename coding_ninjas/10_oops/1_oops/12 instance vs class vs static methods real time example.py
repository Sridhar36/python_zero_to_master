'''
Instance methods like deposit, withdraw, and get_balance operate on specific instances of the BankAccount class and
interact with instance-specific data.

The static method is_valid_account_number doesn't depend on instance-specific data and can be used to check the
validity of any account number.

The class method get_total_balance works with class-level data (the total balance of all accounts) and provides
information about the entire class.
'''


class BankAccount:
    total_balance = 0  # Class-level variable to keep track of the total balance of all accounts

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
        BankAccount.total_balance += balance

    def deposit(self, amount):
        self.balance += amount
        BankAccount.total_balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            BankAccount.total_balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        else:
            return "Insufficient balance"

    def get_balance(self):
        return f"Account balance for {self.holder_name}: {self.balance}"

    @staticmethod
    def is_valid_account_number(account_number):
        return len(str(account_number)) == 10

    @classmethod
    def get_total_balance(cls):
        return f"Total balance across all accounts: {cls.total_balance}"


# Creating bank accounts
account1 = BankAccount(1001, "Alice", 1000)
account2 = BankAccount(1002, "Bob", 1500)

# Deposit and withdraw using instance methods
print(account1.deposit(500))  # Output: Deposited 500. New balance: 1500
print(account2.withdraw(700))  # Output: Withdrew 700. New balance: 800

# Check balance using an instance method
print(account1.get_balance())  # Output: Account balance for Alice: 1500

# Check if an account number is valid using a static method
print(BankAccount.is_valid_account_number(1003))  # Output: False

# Get the total balance across all accounts using a class method
print(BankAccount.get_total_balance())  # Output: Total balance across all accounts: 2300

'''
2.
In this example:

Instance methods like start_engine and stop_engine operate on specific instances of the Car class and interact with 
instance-specific data.

The static method is_valid_year doesn't depend on instance-specific data and can be used to check the validity of any 
year.

The class method get_total_cars works with class-level data (the total number of cars) and provides information about 
the entire class.

This example demonstrates how instance methods, static methods, and class methods can be used in the context of a car 
class for managing car-related operations and information.
'''


class Car:
    total_cars = 0  # Class-level variable to keep track of the total number of cars

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Car.total_cars += 1

    def start_engine(self):
        return f"{self.year} {self.make} {self.model}'s engine is started."

    def stop_engine(self):
        return f"{self.year} {self.make} {self.model}'s engine is stopped."

    @staticmethod
    def is_valid_year(year):
        return year >= 1900 and year <= 2023

    @classmethod
    def get_total_cars(cls):
        return f"Total number of cars: {cls.total_cars}"


# Creating car instances
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)

# Start and stop car engines using instance methods
print(car1.start_engine())  # Output: 2020 Toyota Camry's engine is started.
print(car2.stop_engine())  # Output: 2019 Honda Civic's engine is stopped.

# Check if a year is valid using a static method
print(Car.is_valid_year(2025))  # Output: False

# Get the total number of cars using a class method
print(Car.get_total_cars())  # Output: Total number of cars: 2

'''
3.
In this example:

Instance methods like introduce operate on specific instances of the Employee class and interact with instance-specific 
data.

The static method is_valid_employee_id doesn't depend on instance-specific data and can be used to check the validity 
of any employee ID.

The class method get_total_employees works with class-level data (the total number of employees) and provides 
information about the entire company.

This example demonstrates how instance methods, static methods, and class methods can be used in the context of an 
employee management system to handle employee-related operations and information.
'''


class Employee:
    employee_count = 0  # Class-level variable to keep track of the total number of employees

    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        Employee.employee_count += 1

    def introduce(self):
        return f"Hi, I'm {self.name}, and I work in the {self.department} department."

    @staticmethod
    def is_valid_employee_id(employee_id):
        return len(str(employee_id)) == 6

    @classmethod
    def get_total_employees(cls):
        return f"Total number of employees in the company: {cls.employee_count}"


# Creating employee instances
employee1 = Employee("Alice", 100001, "HR")
employee2 = Employee("Bob", 100002, "Engineering")

# Introduce employees using instance methods
print(employee1.introduce())  # Output: Hi, I'm Alice, and I work in the HR department.
print(employee2.introduce())  # Output: Hi, I'm Bob, and I work in the Engineering department.

# Check if an employee ID is valid using a static method
print(Employee.is_valid_employee_id(12345))  # Output: False

# Get the total number of employees in the company using a class method
print(Employee.get_total_employees())  # Output: Total number of employees in the company: 2

'''
4.
In this example:

Instance methods like display_product_info and apply_discount operate on specific instances of the Product class and 
interact with instance-specific data.

The static method is_valid_category doesn't depend on instance-specific data and can be used to check the validity of 
any product category.

The class method get_total_products works with class-level data (the total number of products) and provides information 
about the entire product inventory.

This example demonstrates how instance methods, static methods, and class methods can be used in the context of an 
e-commerce system for managing and providing information about various products.

'''


class Product:
    total_products = 0  # Class-level variable to keep track of the total number of products

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        Product.total_products += 1

    def display_product_info(self):
        return f"Product: {self.name}, Category: {self.category}, Price: ${self.price}"

    def apply_discount(self, discount_percentage):
        discounted_price = self.price - (self.price * (discount_percentage / 100))
        return f"Discounted Price for {self.name}: ${discounted_price}"

    @staticmethod
    def is_valid_category(category):
        valid_categories = ["Electronics", "Clothing", "Home & Garden", "Toys"]
        return category in valid_categories

    @classmethod
    def get_total_products(cls):
        return f"Total number of products available: {cls.total_products}"


# Creating product instances
product1 = Product("Smartphone", 499.99, "Electronics")
product2 = Product("T-shirt", 19.99, "Clothing")

# Display product information using instance methods
print(product1.display_product_info())  # Output: Product: Smartphone, Category: Electronics, Price: $499.99

# Apply a discount using an instance method
print(product2.apply_discount(10))  # Output: Discounted Price for T-shirt: $17.99

# Check if a category is valid using a static method
print(Product.is_valid_category("Toys"))  # Output: True

# Get the total number of products available using a class method
print(Product.get_total_products())  # Output: Total number of products available: 2
