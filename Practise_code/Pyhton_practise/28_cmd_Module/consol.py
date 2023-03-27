from models.base_model import BaseModel

# Create an instance of the BaseModel class
base_model = BaseModel()

# Print the string representation of the instance
print(base_model)

# Update the instance and call the save method
base_model.name = "My BaseModel"
base_model.save()

# Print the dictionary representation of the instance
print(base_model.to_dict())
