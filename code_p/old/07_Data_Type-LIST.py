#!/usr/bin/python3

"""
MODULES ===================
https://realpython.com/python-command-line-arguments/#the-python-standard-library
https://www.geeksforgeeks.org/command-line-arguments-in-python/


"""

"""
LIST
-List is ordered, meaning a new list will only go to the end.
-List items are indexed, with the first being [0], and second
-List is changeable
-List is duplicatable
-List items can be of any type
"""
tlist = ["apple", "mango", "orange","cherry"]
tlist2 = list(("Bola","Tolu","Tayo"))
tlist3 = list (("Man", 34, True))
print(tlist)
print(len(tlist))
print(tlist2[2])
print(type(tlist3[1]))
tlist3.append("man", "child") #Add an item to the  list
print(tlist3[3])
tlist3[3] = "woman" #change the item on a list
tlist3.insert(2, "boys")

"""
INSERT ITEMS
"""
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") #Insert items
print(thislist)

"""
Extend List
To append elements from another list to the current list, use the extend() method.
"""

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


"""
REMOVE FROM THE LIST 
"""
thislist = ["apple", "banana", "cherry"]
thislist.extend(['New','name'])
print(thislist)

#remove using the name of the item
thislist.remove("New") #remmove an item from the list
print(thislist)

#Remove using specific index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1) #Remove item on index 1
print(thislist)

#Clean entire list
thelist = ["this", "that"]
print(thelist)
thelist.clear()
print(thelist)


"""
LOOP THORUGH A LIST
"""
#Loop through the list
looplist = ["Items1", "Items2", 34]
for i in looplist:
     print(i)

# loop through the list 
looplist = ["Items1", "Items2", 34]


"""
List Comprehension
Example: Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
     if "a" in x:
          newlist.append(x)
print(newlist)

#Example 2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
     if "a" in x:
          newlist.append(x)

print(newlist.upper())

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