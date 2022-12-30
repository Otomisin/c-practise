#!/usr/bin/python3
class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight        

    def introduce_self(self):
        print("My name is " + self.name)
        print(" My color is " + self.color + " Years old\n")


r1 = Robot("Tom", "Red", 30)
r2 = Robot("Bola", "Blue", 60)


r1.introduce_self()
r2.introduce_self()

print(r1.name)
