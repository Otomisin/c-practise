"""

LOOPING
PRINT THE INDEX OF A LIST
CONVERT A LIST TO A STRING AND VICE VERSA
https://www.youtube.com/watch?v=W8KRzm-HUcc&ab_channel=CoreySchafer
"""

"""
LOOPING 
"""

list1 = ["apple", "banana", "cherry"]
for x in list1:
    print(x)

# PRINT THE INDEX OF THE LIST

for x , y in enumerate(list1):
    print('The index and list names are: ', x, y)

# CONVERT A LIST TO STRING AND VICE VERSA
# JOIN the list to a string

course_str = '_'.join(list1)
print(course_str)
print(type(course_str))
print(type(list1))

# String to list
n_list = course_str.split('_')  # we used the dash (-) here because dash was used in the string.
print(n_list)

