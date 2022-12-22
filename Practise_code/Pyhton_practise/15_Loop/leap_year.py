#!/usr/bin/python3

print("hello")

year = int(input("What year is it? "))

# Check if it's a leap year
if (year % 4 == 0):
     if (year % 100 == 0):
          if year % 400 == 0:
               print ("Leap year.")
          else:
               print("Not leap year. ")
     else:
          print("Leap year ")
else:
     print("Not leap yeat.")

