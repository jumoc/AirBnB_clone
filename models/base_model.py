#!/usr/bin/python3
from datetime import datetime
import models
import uuid
"""base_model module"""


class BaseModel():
    """BaseModel parent class"""

    def __init__(self, *args, **kwargs):
        """Constructor for BaseModel"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """String representation of an object"""
        # [<class name>] (<self.id>) <self.__dict__>
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
            )

    def save(self):
        """Updates the variable updated_at with the current time"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of an object"""
        n_dict = self.__dict__.copy()
        n_dict["__class__"] = type(self).__name__
        if type(n_dict["created_at"]) is not str:
            n_dict["created_at"] = n_dict.get("created_at").isoformat()
        if type(n_dict["updated_at"]) is not str:
            n_dict["updated_at"] = n_dict.get("updated_at").isoformat()
        return n_dict
