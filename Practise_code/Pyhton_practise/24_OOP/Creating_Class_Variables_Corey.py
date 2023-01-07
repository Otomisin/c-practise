
"""
Class Variables
Class variables are variables that are shared among instances of a class

Ref: https://pynative.com/python-classes-and-objects/
"""
class Employee:

     raise_amount = 1.04

     def __init__(self, first, last, pay):
          # Instance variable or data member
               self.first = first
               self.last = last
               self.pay = pay
               self.email = first + "." + last + '@comapny.com'

               Employee.num_of_emps += 1

          # Instance Method
     def fullname(self):
          return f"{self.first} {self.last}"
     def apply_raise(self):
          self.pay = int(self.pay * self.raise_amount)

# Creating a class 
emp_1 = Employee('Corey','Schafer', 5000)
emp_2 = Employee ('Test','User', 60000)
emp_3 = Employee('tosin','orenaike', 120000)

# Calling obects
print (emp_1.fullname())
print(Employee.fullname(emp_1))

print (f"Tosin since your first and last name is {emp_3.first} {emp_3.last}, then your email is {emp_3.email}")
print (emp_1.fullname())

print(Employee.num_of_emps)
