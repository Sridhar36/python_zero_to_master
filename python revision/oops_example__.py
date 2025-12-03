class Employee:
    company = "ABC Corp"   # class variable

    def __init__(self, name, salary):
        self.name = name          # instance variable
        self.salary = salary

    # instance method
    def get_details(self):
        return f"{self.name} works at {self.company} with salary {self.salary}"

    # class method
    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

    # static method
    @staticmethod
    def is_valid_salary(amount):
        return amount > 0


# Inheritance
class SDET(Employee):
    def __init__(self, name, salary, automation_tool):
        super().__init__(name, salary)
        self.automation_tool = automation_tool

    def get_details(self):
        base = super().get_details()
        return f"{base} and uses {self.automation_tool} for automation."


# Usage
emp = SDET("Sridhar", 1200000, "Selenium + Python")

print(emp.get_details())                   # instance method
Employee.change_company("XYZ Tech")        # class method
print(emp.get_details())
print(Employee.is_valid_salary(50000))     # static method
