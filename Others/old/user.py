#!/usr/bin/python3

#Ask the user to input miles and assign it to the miles variable
miles = input ('Enter the miles figure: ')

#convert from strings to integer
miles = int(miles)

#perform kilometers calculation by multiplying 1.60934 times miles
kilometers = miles * 1.60934

#Print result using format()
print("{} miles equals {}" kilometers .format(miles, kilometers))
