#!/bin/bash
'''
https://www.youtube.com/watch?v=EcL9ty-sSAw
Discussed about 
1. How to initialize a variable
2. How to update a variable
3. How to  restricting a variable from getting updated
4. How to delete a variable
5. How to get Process ID
6. How to get file name
7. How to provide command line argument
8. How to print command line arguments
9. How to print all the command line arguments
10. How to know total number of command line arguments
'''

read input
echo $input

Name="Tosin" # Set variable names, do not leave a space between the variable and assignments
echo $Name # Read the variable
echo "Name is: $Name"

Name="Btosin"
echo "the new name is: $Name"

readonly Name # set this to read only if to avoid modification of the variable Name
Name="Ctosin"
echo "3rd change: $Name" #if you try to change the name now, it wont change

unset Name # To delete a variable
echo "$Name"

echo $$ # Print process ID

echo $0 # Print file name
