import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        # If kwargs is not empty, set attributes from dictionary
        if kwargs:
            # Iterate through keys and values of kwargs dictionary
            for key, value in kwargs.items():
                # Convert created_at and updated_at strings to datetime objects
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                # Set attribute if key is not __class__
                if key != "__class__":
                    setattr(self, key, value)
            # Set id, created_at, and updated_at attributes from kwargs if they exist, otherwise set to new values
            self.id = kwargs.get('id', str(uuid.uuid4()))
            self.created_at = kwargs.get('created_at', datetime.now())
            self.updated_at = datetime.now()
        # If kwargs is empty, set id, created_at, and updated_at attributes to new values
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        # Return string representation of BaseModel instance
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        # Update updated_at attribute with current datetime
        self.updated_at = datetime.now()

    def to_dict(self):
        # Create copy of __dict__ attribute of BaseModel instance
        new_dict = self.__dict__.copy()
        # Add __class__ key with class name of object to dictionary
        new_dict['__class__'] = type(self).__name__
        # Convert created_at and updated_at attributes to string objects in ISO format
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        # Return dictionary representation of BaseModel instance
        return new_dict
