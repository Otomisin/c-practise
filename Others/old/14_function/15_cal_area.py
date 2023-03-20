# We need this module for our program
import math


# Functions allow us to avoid duplicate code in our programs

# Aside from having to type code twice duplicate code is bad
# because it requires us to change multiple blocks of code
# if we need to make a change

# ---------- OUR FUNCTIONS ----------

# This routes to the correct area function
# The name of the value passed doesn't have to match
def get_area(shape):
    # Switch to lowercase for easy comparison
    shape = shape.lower()

    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Please enter rectangle or circle")


# Create function that calculates the rectangle area
def rectangle_area():
    length = float(input("Enter the length : "))
    width = float(input("Enter the width : "))

    area = length * width

    print("The area of the rectangle is", area)


# Create function that calculates the circle area
def circle_area():
    radius = float(input("Enter the radius : "))

    area = math.pi * (math.pow(radius, 2))

    # Format the output to 2 decimal places
    print("The area of the circle is {:.2f}".format(area))


# ---------- END OF OUR FUNCTIONS ----------

# We often place our main programming logic in a function called main
# We create it this way

def main():
    # Our program will calculate the area for rectangles or circles

    # Without functions we'd have to create a giant list of ifs, elifs

    # Ask the user what shape they have
    shape_type = input("Get area for what shape : ")

    # Call a function that will route to the correct function
    get_area(shape_type)

    # Because of functions it is very easy to see what is happening
    # For more detail just refer to the very short specific functions


# All of the function definitions are ignored and this calls for main()
# to execute when the program starts

main()