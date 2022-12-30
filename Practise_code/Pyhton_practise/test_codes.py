#!/usr/bin/python3
print("Welcome to the rollercoaster ")
height = int(input("What is your height? "))
if height >= 120:
     print("You can ride the rollercoaster ")
     age = int(input("How old are you? "))
     if age < 12:
          print("You are paying $5")
     elif age <= 18 and age <= 21:
          print("You can pay $7")
     else:
          print("You are to pay $12")
else:
     print("You can't ride a rollercoaster")
