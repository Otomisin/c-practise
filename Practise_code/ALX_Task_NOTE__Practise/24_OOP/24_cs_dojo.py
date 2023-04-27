#!/usr/bin/python3
class Robot:
     def introduce_self(self):
          print("My name is " + self.name)

#Create an objective for the class Robot
r1 = Robot()
r1.name = "Tom"
r1.color = "Red"
r1.weight = 30

r2 = Robot()
r2.name = "Bola"
r2.color = "Green"
r2.weight = 40

r1.introduce_self()
r2.introduce_self()
