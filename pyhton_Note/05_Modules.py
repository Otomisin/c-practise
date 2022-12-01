#!/usr/bin/python3

"""
MODULES ===================
https://www.w3schools.com/python/python_strings.asp

A module is like a code library. It's a file containing a set of function you want to include in your application. To create a module just save your code in a fiel extension .py
"""

##Create a Module. 
#To create a module simply create a file with .py in the same folder

"""
IMPORT A MODULE
"""
def greeting (name):
     print ("Hello," + name)


##Use the module here
import mymodule
mymodule.greeting ("Jonathan")

import mymodule
a = mymodule.person1["age"]
print(a)

"""
RE-NAME A MODULE
"""
import mymodule as mx
a = mx.person1 ["age"]
print(f"Years old {a}")

"""
BUILT IN MODULES
"""
#Platform

import platform
x = platform.system()
print(x)


"""
CHECK THE BUILT IN FUNCTIONS NAMES/VARIABLES IN A MODULE
"""

import platform
x = dir(platform)
print(x)

import mymodule
x = dir(mymodule)
print(x)

"""
IMPORTING FROM A MODULE
You can choose to import only parts from a module, by using the "from" keyword
For example, in mymodule you can import the dictionary alone
"""
from mymodule import person1
print(person1["age"])

#Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]