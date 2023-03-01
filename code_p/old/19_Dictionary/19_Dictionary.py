# ---------- DICTIONARIES ----------

# While lists organize data based on sequential indexes
# Dictionaries instead use key / value pairs.

# A key / value pair could be
# fName : "Derek" where fName is the key and "Derek" is
# the value

"""
CREATE A DICTIONARY
"""
# Create a Dictionary about me
derekDict = {"fName": "Derek", "lName": "Banas", "address": "123 Main St", "course" : ['Math', 'Compsci']}
print('This is the dictionary', derekDict)

# Get a value with the key
print("May name :", derekDict["fName"])

"""
UPDATE THE DICTIONARY
"""

# Change a value with the key
derekDict["address"] = "215 North St"

# Add new value:
derekDict['city'] = "Pittsburgh"
print('The updated address and city is ', derekDict)

# Update multiple entries at once
derekDict.update({'fName': 'Tosin' , 'lName': 'Orenaike'})
print(derekDict)

"""
CHECK KEYS AND VALUES
"""

# Check entries
print("check if city is present: ", "city" in derekDict)

# Get the list of values
print(derekDict.values())

# Check how many keys
print(len(derekDict))

# Check and see the keys
print(derekDict.keys())

# Check the keys and values
print(derekDict.items())

# Dictionaries may not print out in the order created
# since they are unordered
"""
LOOPS 
"""
# Get the key and value with items()
for k, v in derekDict.items():
    print(k, v)