#!/usr/bin/python3

"""
## Python Data Types
Link: https://www.w3schools.com/python/python_variables.asp

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	     str
Numeric Types:	     int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	     dict
Set Types:	     set, frozenset
Boolean Type:	     bool
Binary Types:	     bytes, bytearray, memoryview
None Type:	     NoneType

##EXAMPLES

"""
# Python3 program for explaining
# use of list, tuple, set and
# dictionary
 
# Lists
l = []
 
# Adding Element into list
l.append(5)
l.append(10)
print("Adding 5 and 10 in list", l)
 
# Popping Elements from list
l.pop()
print("Popped one element from list", l)
print()
 
# Set
s = set()
 
# Adding element into set
s.add(5)
s.add(10)
print("Adding 5 and 10 in set", s)

# Removing element from set
s.remove(5)
print("Removing 5 from set", s)
print()
 
# Tuple
t = tuple(l)
 
# Tuples are immutable
print("Tuple", t)
print()
 
# 19_Dictionary
d = {}
 
# Adding the key value pair
d[5] = "Five"
d[10] = "Ten"
print("19_Dictionary", d)
 
# Removing key-value pair
del d[10]
print("19_Dictionary", d)

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

a, b = 0, 1
while a < 1000:
    print(a, end='')
    a, b = b, a+b

# Measure some strings:
words = ['cat', 'window', 'defenestrate', 'woman']
for w in words:
    print(w, len(w), end = '')

names = ['Bola', 'Boluwatife', 'Anu', 'oluwaseunfunmi']
for x in names:
     print(x, len(x), end = " $ ")