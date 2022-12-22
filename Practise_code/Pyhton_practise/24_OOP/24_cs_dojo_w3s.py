#!/usr/bin/python3
class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight        

    def __str__(self): # Using The __str__() Function
        return f"{self.name} {self.color} {self.weight}"


r1 = Robot("Tom", "Red", 30)
r2 = Robot("Bola", "Blue", 60)


print(r1)

"""
The self Parameter (self)_
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
"""