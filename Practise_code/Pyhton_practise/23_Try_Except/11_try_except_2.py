#!/usr/bin/python3
# Python code to illustrate
# clean up actions
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Yeah ! Your answer is:", result)
    finally:
        print("I'm finally clause, always raised !! ")
  
# Look at parameters and note the working of Program
divide(3, 2)
divide(2,5.6)
