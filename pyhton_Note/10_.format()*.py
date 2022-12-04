#!/usr/bin/python3

"""
The String .format() Method: Arguments


https://realpython.com/python-formatted-output/#the-python-string-format-method

"""
#=============================================================================================================
print('%d %s cost $%.2f' % (6, 'bananas', 1.74))


"""
USING POSITIONAL PARAMETERS
The replacement fields are {0}, {1},{2} and {3}, which contain numbers that correspond to the zero-based positional arguments 6, 'bananas', 1.74 and 2022. 
"""
print ("{0} {1} cost ${2}" .format (6, 'bananas', 1.74))
print ("{0} {1} cost ${2} in {3}" .format (6, 'bananas', 1.74, 2022))

"""
USING KEYWORD ARGUMENT
-Replacement fields don’t have to appear in the template in numerical order. They can be specified in any order, and they can appear more than once:
"""

print ("{quantity} {item} cost ${price} in {year}" .format(quantity=6, item ='bananas', price = 50, year = 2022))

#The position does not matter when you use the replacement fields and 
print('{2}.{1}.{0}/{0}{0}.{1}{1}.{2}{2}'.format('foo', 'bar', 'baz'))

#You can also omit the 
