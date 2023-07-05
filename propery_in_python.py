'''
@property is decorator
property decorator allows us to define a method and access as an attr
This acts like getters and setters in another programming language.

We can create methods and call them as an attribute, that is , not using parannthesis
'''


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_1.last = "changed"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())
