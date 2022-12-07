#!/usr/bin/python3

"""
match Statements
A match statement takes an expression and compares its value to 
successive patterns given as one or more case blocks

https://docs.python.org/3/library/stdtypes.html#range
https://www.youtube.com/watch?v=dFfI6swA7co&ab_channel=JoeJames
"""
#=============================================================================================================

list(range(3, 6))


"""
4.6. match Statements
"""


var = 8
match var:
     case 1:
          print('small')
     case 2:
          print('Medium')
     case 3:
          print('large')
     case 4 | 5 | 7:
          print('This are above 3')
     case _:
          print('Unknown') #This match on anything

#For tuple
var2 = (8, 0)
match var2:
     case (0, x):
          print('on y-axis')
     case (x, 0):
          print('on y-axis')
     case (x, y):
          print('not on axis')

# Using function
def  print_grade(score):
     match score:
          case score if score >= 90:
               print ('You scored A, that\'s awesome!')
          case score if score >= 80:
               print ('You scored a B, that\'s good.')
          case score if score >= 70:
               print ('You score a C, that\'s good, but you can do better')
          case score if score >= 60:
               print ('You score D, that\'s that not enough, try better next time')
          case _:
               print('You score less than the pass mark, try again!')

print_grade(88)
print_grade(20)

#Example of a match statement
var3 = (4, 8)
#def point (x, y):
match var3:
     case (0, 0):
          print("Origin")
     case (0, y):
          print(f"Y={y}")
     case (x, 0):
          print(f"X={x}")
     case (x, y):
          print(f"X={x}, Y={y}")
     case _:
          raise ValueError("Not a point")

point(x, y)

def http_error(status):
    match status:
     case 400:
          return "Bad request"
     case 404:
          return "Not found"
     case 418:
          return "I'm a teapot"
     case 500:
          return "I don't know"
     case _:
          return "Something's wrong with the internet" 

http_error(400)