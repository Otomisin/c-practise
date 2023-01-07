
"""
Object Properties
Every object has properties with it. In other words, we can say that object property is an association between name and value.

Ref: https://pynative.com/python-classes-and-objects/
"""
class Employee:

     def __init__(self, first, last, pay):
          # Instance variable or data member
               self.first = first
               self.last = last
               self.pay = pay
               self.email = first + "." + last + '@comapny.com'

          # Instance Method
     def fullname(self):
          return f"{self.first} {self.last}"

# Creating a class 
emp_1 = Employee('Corey','Schafer', 5000)
emp_2 = Employee ('Test','User', 60000)
emp_3 = Employee('tosin','orenaike', 120000)

# Calling obects

print (emp_1.fullname())
print(Employee.fullname(emp_1))

print (f"Tosin since your first and last name is {emp_3.first} {emp_3.last}, then your email is {emp_3.email}")
print (emp_1.fullname())
