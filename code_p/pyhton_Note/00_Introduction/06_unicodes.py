"""
LEARN TO PROGRAM
Show the importance of age using logics
https://www.youtube.com/watch?v=02edODXdHgs&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=3&ab_channel=DerekBanas
"""

# A - Z 65 - 90
# a - z 97 - 122

# print ('A= ', ord("A"))  # Converts from Unicodes
# print("65= ", chr(65))   # Convert to unicodes
"""
UNICODE Problems

Make user enter a message and convert it to a unicode
"""
# Enter a string to hide un uppercase; HIDE
message = input('What\'s your message to hide upper case: ')
secrets_messages = ""

# Cycle through each character in the string
for char in message:
    secrets_messages = str(ord(char))

# Original Message : HIDE
print('Your message in unicode is', secrets_messages)
