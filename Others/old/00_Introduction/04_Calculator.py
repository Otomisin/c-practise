"""
LEARN TO PROGRAM
A Calculator
https://www.youtube.com/watch?v=nwjAHQERL08&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=1&ab_channel=DerekBanas
"""

# Store the user input of 2 numbers and the operator
num1, operator, num2 = input('Enter numbers and operation you want to calculate ').split()
# Convert the strings to integers
num1 = int(num1)
num2 = int(num2)

# if + then we need to provide output based on addition
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1-num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
else:
    print("Use one of the three operations (+, - or /) next time")

# other operatioin
# >, < !=