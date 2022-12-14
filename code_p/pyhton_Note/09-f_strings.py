#!/usr/bin/python3

"""
Python 3's f-Strings ===================
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.


#https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python

"""
#=============================================================================================================

"""
How to Use %-formatting
The disadvantages of this method is 
- It can be verbose and lead to errors 
-
"""

name = "Eric"
age = 34
score = 3.5
print("Hello, %s." %name)
print("Hello, %s. You are, %s." %(name, age))
print("Hello, %s. You are %s, and your score is %s" %(name,age, score))

"""
How To Use str.format()
"""
name = "Eric"
age = 34
score = 3.5
print("Hello, {}." .format(name))
print("Hello, {}. You are, {}." .format(name, age))
print("Hello, {}. You are {}, and your score is {}" .format(name,age, score))

person = {'name': 'Eric', 'age': 73, 'score': 3.65}
print("Hello {name}, you are {age} and your score is {score}" .format(name = person['name'], age=person['age'], score= person['score']))


"""
f-Strings: A New and Improved Way to Format Strings in Python
"""

# Python3 program introducing f-string

name = "Tosin"
age = 25
print(f"My name is {name}, and I am {age} years old")

print (f"{2*4}")


height = 4
leght = 5

print(f"the total is {height*leght/height}")


#Loop over f strings

people = [{
          'name':'Tosin',
          'age': 32,
          'gender': 'male',
          'score':34.3},
     {
          'name':'Bola',
          'age': 34,
          'gender': 'female',
          'score': 55.7}
]

for person in people:
     print(f"{person.get('name')} is {person.get('age')} years old and your score is {person.get('score')}")

print(f"{'she' if person.get('gender')== 'female' else 'He'} went to the store") #Conditioin in Python
