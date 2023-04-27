#!/usr/bin/python3

"""
This is a
https://www.w3schools.com/python/python_strings.asp
https://www.youtube.com/watch?v=OICqSuUvSUc&ab_channel=datagy

"""

"""
Subscriptng
"""
name = 'Tosin'

# print ("Hi my name is %s" %(name))

"""
Strings are Arrays
"""
a = """ This is a string testing"""
print(a)

print(a[1])

"""
Loop through strings
"""
# Loop through strings
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
# To check use "in" and to check if not use "not in"
txt = "This is a text"
print("free" in txt)
print("text" in txt)
# use not if not present
print("man" not in txt)

# using if to check if a text is in a sentence
txt = "This is a text"
if "text" in txt:
    print("Yes there is a text in the phrase")

"""
STRING SLICING
"""
b = "Hello Mr Coder"
print(b[0])
print(b[0:6])  # Slice from the start
print(b[:6])  # Slice from the start
print(b[6:])  # Slice till the end
print(b[-2:])  # Negatinve slicing

"""
MODIFY SLICING
"""
a = "Hello, World!"
print(a.upper())  # The upper() method returns the string in upper case
print(a.lower())  # The lower() method returns the string in lower case
print(a.strip())  # The strip() method removes any whitespace from the beginning or the end
print(a.replace("H", "B"))  # The replace() method replaces a string with another string
print(a.split(
    "-"))  # The split() method returns a list where the text between the specified separator becomes the list items.

"""
CONCATENATION
"""
a = "Hello"
b = "Tosin"
print(a + " " + b)

"""
GETTING RID OF SPACES
"""

rand_string = "   this is an important string  "
rand_string = rand_string.lstrip()  # removes the last spaces
rand_string = rand_string.lstrip()  # removes the first spaces
rand_string = rand_string.lstrip()  # removes all spaces
rand_string = rand_string.upper()  # change text to upper case
rand_string = rand_string.lower()  # change text to lower case
# or

print(rand_string.upper())
print(rand_string.lower())

"""
CONVERT STRINGS TO LIST AND VICE VERSA
"""
# Example: Convert a list to a string and vice versa
a_list = ["Bunch", "Tosin", "Man", "Bola"]
a_list2 = (" ".join(a_list))
print(type(a_list2))

# Example: Convert a string to a list
a_list3 = a_list2.split()
print(a_list3)

"""
FIND, COUNT and REPLACE IN A STRING
"""

print("How many is: ", rand_string.count("an"))
print("Where is string located? ", rand_string.find("an"))
print(rand_string.replace("an ", "a kind of "))

"""
PROBLEM SOLVING: 
Develop an acronym generator
"""

# Ask for a string
orig_string = input("What's the string you want me to help you with? ")
# Convert the string to uppercase
orig_string = orig_string.upper()

# Convert the string into a list
last_string = orig_string.split()

# Cycle through the list and Get the 1st letter of the words and eliminate the newline
for x in last_string:
    print(x[0], end="")

# Add a newline
print()


"""
CHECKING FOR STRINGS FEATURES -----
"""

letter_z = "z"
num_3 = "3"
a_space = " "

# Returns True if characters are letters or numbers
# Whitespace is false
print("Is z a letter or number :", letter_z.isalnum())

# Returns True if characters are letters
print("Is z a letter :", letter_z.isalpha())

# Returns True if characters are numbers (Floats are False)
print("Is 3 a number :", num_3.isdigit())

# Returns True if all are lowercase
print("Is z a lowercase :", letter_z.islower())

# Returns True if all are uppercase
print("Is z a uppercase :", letter_z.isupper())

# Returns True if all are spaces
print("Is space a space :", a_space.isspace())