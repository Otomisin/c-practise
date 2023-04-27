#!/usr/bin/python3

"""
Class Attributes
Accessing properties and assigning values

Ref: https://pynative.com/python-classes-and-objects/
"""
class Student:
    # class variables
    school_name = 'ABC School'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

s1 = Student("Harry", 12)
# access instance variables
print('Student from instance variable:', s1.name, s1.age)

# access class variable
print('School name from class variable:', Student.school_name)

# Modify instance variables
s1.name = 'Jessa'
s1.age = 14
print('New student details:', s1.name, s1.age)

# Modify class variables
Student.school_name = 'XYZ School'
print('New school name:', Student.school_name)