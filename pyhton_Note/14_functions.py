#!/usr/bin/python3

"""
Python Functions
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.

https://www.w3schools.com/python/python_functions.asp
"""
#=============================================================================================================

"""
Creating a function
"""

def my_function():
     print('Hello I am a function')

my_function()

"""
Arguments
Information can be passed into functions as arguments
"""

def my_argument (fname): #fname is the parameter
     print (fname + ' the Coder')

my_argument('Tosin') #Tosin is the argument
my_argument('Bola')

"""
Number of Arguments
By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less
"""

def my_func(fname, lname):
     print(fname + lname)

my_func('Tosin',' Orenaike')
my_func("Emil", " Refsnes")


"""
Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:
"""

def my_function(*kids):
  print(kids)

my_function("Emil", "Tobias", "Linus")

#An example without arbitra

list_to_sum = [1,2,3,4,5]

def sum_function(numbers):
    total = 0
    for i in numbers:
        total += i

    return total

print(sum_function(list_to_sum))

#An example with arbitrary
def sum_function(*numbers):
    total = 0
    for i in numbers:
        total += i #The Python addition asignment operator (+=) lets you add two values together and assign the resultant value to a variable.

    return total
    
print(sum_function(1,2,3,4,5,6))


"""
Keyword Arguments
You can also send arguments with the key = value syntax.
This way the order of the arguments does not matter.
"""

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


"""
Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
"""
#Get the last name
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#Get the first name
def my_function(**kid):
  print("His first name is " + kid["fname"])

my_function(fname = "Tobias", lname = "Refsnes")

"""
Default Parameter Value
If we call the function without argument, it uses the default value
"""

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

"""
Return Values
To let a function return a value, use the return statement:
"""

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
my_function(4)


"""
The pass Statement
function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
"""

def my_func():
     pass

my_func()