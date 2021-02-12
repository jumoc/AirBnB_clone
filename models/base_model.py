#!/usr/bin/python3
import uuid
from datetime import datetime

"""base_model module"""

class BaseModel():
    """BaseModel parent class"""

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        # [<class name>] (<self.id>) <self.__dict__>
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
            )

    def save(self):
        """Updates the variable updated_at with the current time"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Returns a dictionary representation of an object"""
        n_dict = self.__dict__.copy()
        n_dict["__class__"] = self.__class__.__name__
        n_dict["created_at"] = n_dict.get("created_at").isoformat()
        n_dict["updated_at"] = n_dict.get("updated_at").isoformat()
        return n_dict
