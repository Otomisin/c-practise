"""
LEARN TO PROGRAM
Show the importance of age using logics
https://www.youtube.com/watch?v=nwjAHQERL08&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=1&ab_channel=DerekBanas
"""
# Let user input their age and store in age
age = eval(input("How old are you? "))  # use eval to automatically convert strings to integer

# Allocate the ages in their respective classes
if age < 5:
    print("Too young for school")
elif age == 5:
    print('Go to Kindergarten')
elif (age > 17) and (age < 50):
    grade = age - 5
    print('Go to {}th College'. format(grade))
else:
    print('you should be working')
