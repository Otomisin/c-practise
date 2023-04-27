import json

with open("jsonsample.json", "r") as read_file:
     data = json.load(read_file)

print(data)
