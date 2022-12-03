#!/usr/bin/python3

"""
This is a 
https://www.w3schools.com/python/python_strings.asp
https://www.youtube.com/watch?v=OICqSuUvSUc&ab_channel=datagy

"""
name = 'Tosin'

#print ("Hi my name is %s" %(name))

"""
Strings are Arrays
"""
a = """ This is a string testing"""
print(a)

print(a[1])

"""
Loop through strings
"""
#Loop through strings
for x in "name":
     print(x)


"""
String Lenght
"""

a = "Hello,world"
print(len(a))

"""
Check if a text is in a phrase  
"""
#To check use "in" and to check if not use "not in"
txt = "This is a text"
print("free" in txt)
print("text" in txt)
#use not if not present
print("man" not in txt)

#using if to check if a text is in a sentence
txt = "This is a text"
if "text" in txt:
     print("Yes there is a text in the phrase")

"""
STRING SLICING
"""
b = "Hello Mr Coder"
print(b[0])
print(b[0:6])  #Slice from the start
print(b[:6]) #Slice from the start
print (b[6:]) #Slice till the end
print (b[-2:]) #Negatinve slicing

"""
MODIFY SLICING
"""
a = "Hello, World!"
print(a.upper()) #The upper() method returns the string in upper case
print(a.lower()) #The lower() method returns the string in lower case
print(a.strip()) #The strip() method removes any whitespace from the beginning or the end
print(a.replace("H","B")) #The replace() method replaces a string with another string
print(a.split("-")) #The split() method returns a list where the text between the specified separator becomes the list items.

"""
CONCATENATION
"""
a = "Hello"
b = "Tosin"
print(a + " "+ b )
