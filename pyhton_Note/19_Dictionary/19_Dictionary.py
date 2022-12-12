# ---------- DICTIONARIES ----------

# While lists organize data based on sequential indexes
# Dictionaries instead use key / value pairs.

# A key / value pair could be
# fName : "Derek" where fName is the key and "Derek" is
# the value

# Create a Dictionary about me
derekDict = {"fName": "Derek", "lName": "Banas", "address": "123 Main St"}

# Get a value with the key
print("May name :", derekDict["fName"])

# Change a value with the key
derekDict["address"] = "215 North St"

# Dictionaries may not print out in the order created
# since they are unordered
print(derekDict)

# Add a new key value
derekDict['city'] = 'Pittsburgh'

# Check if a key exists
print("Is there a city :", "city" in derekDict)

# Get the list of values
print(derekDict.values())

# Get the list of keys
print(derekDict.keys())

# Get the key and value with items()
for k, v in derekDict.items():
    print(k, v)

# Get gets a value associated with a key or the default
print(derekDict.get("mName", "Not Here"))

# Delete a key value
del derekDict["fName"]

# Loop through the dictionary keys
for i in derekDict:
    print(i)

# Delete all entries
derekDict.clear()

# List for holding Dictionaries
employees = []

# Input employee data
fName, lName = input("Enter Employee Name : ").split()

employees.append({'fName': fName, 'lName': lName})

print(employees)

# ---------- PROBLEM : CREATE A CUSTOMER LIST ----------
# Create an array of customer dictionaries
# Output should look like this
'''
Enter Customer (Yes/No) : y
Enter Customer Name : Derek Banas
Enter Customer (Yes/No) : y
Enter Customer Name : Sally Smith
Enter Customer (Yes/No) : n
Derek Banas
Sally Smith
'''

# Create customer array outside the for so it isn't local
# to the while loop
customers = []

while True:

    # Cut off the 1st letter to cover if the user
    # types a n or y
    createEntry = input("Enter Customer (Yes/No) : ")
    createEntry = createEntry[0].lower()

    if createEntry == "n":

        # Leave the while loop when n is entered
        break
    else:

        # Get the customer name by splitting at the space
        fName, lName = input("Enter Customer Name : ").split()

        # Add the dictionary to the array
        customers.append({'fName': fName, 'lName': lName})

# Print out customer list
for cust in customers:
    print(cust['fName'], cust['lName'])
