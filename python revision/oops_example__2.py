class Employee:
    company = "VL tech" # class variable

    def __init__(self, name, sal):
        self.name = name # instance variable
        self.sal  = sal

    def get_details(self): # instance method
        return f"{self.name} works at  {self.company}; sal : {self.sal}"

    @classmethod
    def change_company(cls, new_comp):
        cls.company = new_comp

    @staticmethod
    def is_valid_salary(amount):
        return amount > 0


# inheritance
class SDET(Employee):

    def __init__(self, name, sal, tool):
        super().__init__(name, sal)
        self.tool = tool

    def get_details(self):
        base = super().get_details()
        return f"{base} and uses {self.tool} for automation"

