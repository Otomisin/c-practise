#!/usr/bin/python3

"""
LIST COMPREHENSION ===================
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.



"""





"""
CAPITALISE LIST
"""
#Print the names in the list in lower
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
lower_fruits = []

for name in fruits:
     lower_fruits.append(name.lower())

print(lower_fruits)

#Print in capitalize
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
lower_fruits = []

for name in fruits:
     lower_fruits.append(name.upper())

print(lower_fruits)

#Using list comprehension

mates = ["Tosin", "Bola", "Buba", "Bole"]
names_lower = [x.lower() for x in mates] #convert a string to lowercase in Python, use the built-in lower() method of a string.
upper_names = [x.upper() for x in mates] # convert a string to uppercase in Python, use the built-in upper() method of a string.
cap_names = [x.capitalize() for x in mates] # convert a string to uppercase in Python, use the built-in upper() method of a string.
print(names_lower)
print(upper_names)
print(cap_names)