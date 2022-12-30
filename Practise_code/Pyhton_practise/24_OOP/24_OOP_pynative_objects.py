#!/usr/bin/python3

"""
Object Properties
Every object has properties with it. In other words, we can say that object property is an association between name and value.

Ref: https://pynative.com/python-classes-and-objects/
"""
class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show(self):
        print("Fruit is", self.name, "and Color is", self.color)

# creating object of the class
obj = Fruit("Apple", "red")

# Modifying Object Properties
obj.name = "strawberry"

# calling the instance method using the object obj
obj.show()
# Output Fruit is strawberry and Color is red


"""
DELETING Object properties
"""
# Deleting Object Properties
# del obj.name

# Accessing object properties after deleting
#print(obj.name)
# Output: AttributeError: 'Fruit' object has no attribute 'name'


"""
DELETEING Objects
"""

#Deleting objects
del obj

#Trying to access object after deleting
obj.show()
