#!/usr/bin/python3

"""
Variables are containers for storing data values
Python has no command for declaring a variable and a varible is created the moment you first asign it.

Link: https://www.w3schools.com/python/python_variables.asp

"""
x = 4
y = "Tosin"

print(x)
print(y)

"""
CASTING
Casting helps to specify the data types of the variable
"""
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(type(x))
print(type(y))
print(type(z))

"""
VARIABLE NAMES AND THE RULES
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
     A variable name must start with a letter or the underscore character
     A variable name cannot start with a number
     A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
     Variable names are case-sensitive (age, Age and AGE are three different variables)

"""
#Assinging multiple variables
x, y, z = 'Tosin', 'Naa', 'Tola'
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a collecction
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print(x,y,z)
#or
print (x + y + z) #Not recommended

"""
GLOBAL AND LOCAAL VARIABLES
Variables that are created outside a function is called global variable and they can be used both within and outside a function.
While a local variable is a variable used within a function. You can however make a local variable global by using the "global" keyword. This will also take supiriority over the an intially delclared global variable
"""
#Creating a global variable for a function
x = "aswesome"

def myfunc():
     print("Python is " + x)

myfunc()

#Creating a global and local variable
x = "awesome"

def myfunc ():
     x = "fantastic"
     print("Python is " + x)

myfunc()

print ("Python is " + x)

#Global Keyword
def myfunc():
     global x
     x = "fantastic"

myfunc()
print ("Python is " + x)
