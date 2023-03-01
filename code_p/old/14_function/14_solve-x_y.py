# ---------- PROBLEM : SOLVE FOR X ----------
# Make a function that receives an algebraic equation like
# x + 4 = 9 and solve for x
# x will always be the 1st value received and you only
# will deal with addition

# Receive the string and split the string into variables
def solve_eq(equation):
    x, add, num1, equal, num2 = equation.split()

    # Convert the strings into ints
    num1, num2 = int(num1), int(num2)

    # Convert the result into a string and join (concatenate)
    # it to the string "x = "
    return "x = " + str(num2 - num1)


print(solve_eq("x + 6 = 9"))

"""
# Solve for y in 4 + y = 9
"""


def solve_y(equation2):
    num1, add, y, equal, num2 = equation2.split()

    # Convert the strings into ints
    num1, num2 = int(num1), int(num2)

    # Convert the result into a string and join
    return "y = " + str(num1 - num2)


print(solve_y("100 - y = 89"))
