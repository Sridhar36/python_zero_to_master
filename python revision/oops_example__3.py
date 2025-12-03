# from abc import ABC, abstractmethod
#
#
# # ---------------------- Abstraction ----------------------
# class BaseEmployee(ABC):
#     """Abstract base class enforcing common behavior for all employees."""
#
#     @abstractmethod
#     def get_details(self):
#         pass
#
#
# # ---------------------- Employee Class ----------------------
# class Employee(BaseEmployee):
#     company = "ABC Corp"  # class variable (shared across all objects)
#
#     def __init__(self, name, salary):
#         # ---------------------- Encapsulation ----------------------
#         self._name = name  # protected attribute
#         self.__salary = salary  # private attribute
#
#     # Getter (encapsulation)
#     @property
#     def salary(self):
#         return self.__salary
#
#     # Setter (encapsulation)
#     @salary.setter
#     def salary(self, amount):
#         if amount <= 0:
#             raise ValueError("Salary must be positive")
#         self.__salary = amount
#
#     # instance method
#     def get_details(self):
#         return f"{self._name} works at {self.company} with salary {self.__salary}"
#
#     # class method
#     @classmethod
#     def change_company(cls, new_name):
#         cls.company = new_name
#
#     # static method
#     @staticmethod
#     def is_valid_salary(amount):
#         return amount > 0
#
#
# # ---------------------- Inheritance + Polymorphism ----------------------
# class SDET(Employee):
#     def __init__(self, name, salary, automation_tool):
#         super().__init__(name, salary)
#         self.automation_tool = automation_tool
#
#     # Polymorphism → overriding parent method
#     def get_details(self):
#         base = super().get_details()
#         return f"{base}. Automation Tool: {self.automation_tool}"
#
#
# # ---------------------- Another Polymorphic Class ----------------------
# class ManualTester(Employee):
#     def __init__(self, name, salary, test_management_tool):
#         super().__init__(name, salary)
#         self.test_management_tool = test_management_tool
#
#     # Polymorphism → overriding same method differently
#     def get_details(self):
#         return f"{self._name} is a manual tester using {self.test_management_tool}."
#
#
# # ---------------------- Usage ----------------------
# emp = SDET("Sridhar", 1200000, "Selenium + Python")
#
# print(emp.get_details())  # instance method (polymorphic)
# Employee.change_company("XYZ Tech")
# print(emp.get_details())  # reflects changed class variable
# print(Employee.is_valid_salary(50000))
#
# # Testing encapsulation: salary setter
# emp.salary = 1500000
# print(emp.salary)


def only_positive(func):
    def wrapper(a,b):
        result = func(a,b)
        if result<0:
            return "Only positives allowed"
        return result
    return wrapper


@only_positive
def distance(a,b):
    return a-b


print(distance(3,3))
print(distance(5,3))
print(distance(3,5))
