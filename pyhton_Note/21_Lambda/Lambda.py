"""
Lambda is also know as anonymous function
# https://www.youtube.com/watch?v=1GAC6KQUPeg&ab_channel=DerekBanas
# https://www.youtube.com/watch?v=25ovCm9jKfA&ab_channel=Socratica
# https://www.youtube.com/watch?v=BcbVe1r2CYc&ab_channel=TechWithTim
"""


# Write a function that computes 3x + 1
def f(x):
    return 3 * x + 1


print(f(3))

# What a lambda expression looks like
g = lambda x: 3 * x + 4
print(g(4))

# Write a script using Lambda to do the following to the names of people; sort by last name, turn to lower class
all_names = ["Oluwa Tosin", "Ore naike", "Anu Amos", "Bola Ojo Bayo", "Naa Bola Johnson"]

all_names = all_names.sort(key=lambda name: name.split(" ")[-1].lower())
print(all_names)
