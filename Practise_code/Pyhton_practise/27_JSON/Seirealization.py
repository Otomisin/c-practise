import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

print(type(data)) # Print type

## Create a Json file from the dict file

with open("data_file.json", "w") as write_file:
     json.dump(data, write_file, indent=4) # Use indent 4 to format it to readable formart
