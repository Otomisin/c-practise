"""
LEARN TO PROGRAM
Show the importance of age using logics
https://www.youtube.com/watch?v=nwjAHQERL08&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=1&ab_channel=DerekBanas
"""
# Let user input their age and store in age
age = eval(input("How old are you? "))  # use eval to automatically convert strings to integer
# and:
# or :
# not:


# if age is greater than or  equal to 1 ad less than or equal to 18 important
if (age >= 1) and (age <= 20):
    print("This is an important birthday")
# if age is either 21 or 50 important
elif (age == 30) or (age == 50) or (age == 40):
    print("This is also an important birthday")

# We check if age is less than 65 and then convert true to false and vice versa
elif not(age < 65):
    print("These are seniors and they are important as well ")

# Else not important
else:
    print("Sorry your birthday is not important")
