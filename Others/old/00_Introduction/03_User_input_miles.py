"""
LEARN TO PROGRAM
https://www.youtube.com/watch?v=nwjAHQERL08&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=1&ab_channel=DerekBanas
"""
# Problem: Receive miles and convert to kilometer
# Kilometer = miles * 1.60934
# Enter Mile number
# Print the output of miles

# Ask user to input miles and assign it to miles variable
miles = input('What is the miles? ')

# Convert string to integer
miles = int(miles)

# Convert miles to kilometer by multiplying result times 1.60934
kilometer = miles * 1.60934

# Print the output using format()
print('The result of {} miles when converted is {} Kilometers'.format(miles, kilometer))
