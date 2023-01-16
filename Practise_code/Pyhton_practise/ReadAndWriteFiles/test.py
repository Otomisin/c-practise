import csv
import os
cwd = os.getcwd()  # Get the current working directory (cwd)
print(cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print(files)

# One Method of Read the file
f = open('random.txt', 'r')
print(f.read())
f.close()


# with open('random.txt', 'r') as f:
#      for line in f:
#           print(line)