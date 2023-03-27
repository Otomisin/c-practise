import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel class for other classes to inherit from
    """

    def __init__(self):
        """
        Initialize public instance attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Return string representation of instance
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Update updated_at attribute with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return dictionary representation of instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
