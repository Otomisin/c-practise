"""
https://www.youtube.com/watch?v=W8KRzm-HUcc&ab_channel=CoreySchafer

ASSESSING LIST
APPENDING LIST
INSERT LIST
EXTEND LIST
REMOVING LIST
SORTING LIST

"""

# CREATING A LIST
thislist = ["apple", "banana", "cherry"]
list2 = ['return', 'deporte']
print(thislist)

"""
ACCESSING THE LIST 
"""
# ACCESSING THE LIST
print("The ite is 2nd and third position will be",
      thislist[1:3])  # get the 2nd and 3rd item on the list. Item in 3rd position will not be added

# Get the length of the list
print('The length os the list is: ', len(list2))


"""
APPEND TO A LIST
Used for appending and adding elements to List. It is used to add elements to the last position of the
"""
thislist.append("man")
print("This is an append outcome ", thislist)  # This adds man to the last index

"""
INSERT IN A LIST
Insert element in a specified position
"""
thislist.insert(2, "boys")  # Adding to specific location
print("insert outcome", thislist)

thislist.insert(0, list2)  # this adds a list within a list
print("List within a list", thislist)

"""
EXTEND A LIST
Adds more list to a list
"""
thislist.extend(list2)  # This helps to add two list together
print("Extend outcome", thislist)

list3 = list2 + thislist
print("Join list using +", list3)
# REMOVING ITEMS FROM THE LIST

for x in list2:
    thislist.append(x)
print("using loop", x)

"""
REMOVING LIST
"""
# Remove using names
print(list3)
list3.remove("man")
print('Remove man from the list', list3)

# Remove using index
list3.pop(0)
print(list3)

# Remove using del
del list3[1]
print('Delete using del', list3)

list3[1] = 'new man'
print('Modify a list', list3)

# Delete entire list
# del list3
# print(list3)

"""
SORTING LIST
"""
print(list3)

# Reverse
list3.reverse()
print('The list has beeb reversed',list3)

# Sorting
list3.sort()
print('Sorting', list3)

list3.sort(reverse=True)
print('reverse sorting', list3)

"""
ADDING AND SUBTRACTION
"""

num = [1,2,3,4]
print('The sum of the number is ', sum(num))
print('The max number is', max(num))
print('The min number is: ',min(num))

"""
FIDNING 
"""
print('man' in list3)