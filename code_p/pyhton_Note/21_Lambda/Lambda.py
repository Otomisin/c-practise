"""
Lambda is also known as anonymous function
# https://www.youtube.com/watch?v=1GAC6KQUPeg&ab_channel=DerekBanas
# https://www.youtube.com/watch?v=25ovCm9jKfA&ab_channel=Socratica
# https://www.youtube.com/watch?v=BcbVe1r2CYc&ab_channel=TechWithTim
"""

"""
WRITING A LAMBDA PARAMETER
"""
# What a lambda expression with single parameter
g = lambda x: 3 * x + 4
print(g(4))

# a lambda with multiple parameters
lamFun = lambda y, z, a: y * z + a
print(lamFun(3, 9, 4))

"""
LAMBDA WITHIN FUNCTIONS
"""


def myFun(n):
    return lambda x: x + n

mydouble = myFun(3)

print(mydouble(4))

# # Write a script using Lambda to do the following to the names of people; sort by last name, turn to lower class
# all_names = ["Oluwa Tosin", "Ore naike", "Anu Amos", "Bola Ojo Bayo", "Naa Bola Johnson"]
# print(all_names)
#
# # all_names = all_names.sort(key=lambda name: name.split(" ")[-1].lower())
# print(all_names.sort(key=lambda name: name.split(" ")[-1].lower()))
