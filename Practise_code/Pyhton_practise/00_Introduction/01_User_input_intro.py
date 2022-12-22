"""
LEARN TO PROGRAM
https://www.youtube.com/watch?v=nwjAHQERL08&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=1&ab_channel=DerekBanas
"""
# Ask user to input 2 values  and store them in a variable num1 and num2
num1, num2 = input("Enter two number: ").split()  # More on split here https://www.simplilearn.com/tutorials/python-tutorial/split-in-python#:~:text=Whenever%20there%20is%20a%20need,given%20string%20or%20given%20line.

# Convert the strings into a regular number
num1 = int(num1)
num2 = int(num2)

# Add the values entered and stored in a variable called sum
sum = num1 + num2
# Subtract values and store in difference
difference = num1 - num2

# Multiply values and store in products
products = num1 * num2

# Divide values and store in quotients
quotients = num1 / num2

# Use modulus on the values to find the remainder
remainder = num1 % num2

# print the result for the user
print("Your result is {} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, products))
print("{} % {} = {}".format(num1, num2, remainder))
