#!/usr/bin/python3
from datetime import datetime
from . import storage
import uuid
"""base_model module"""


class BaseModel():
    """BaseModel parent class"""

    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    kwargs[key] = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        # [<class name>] (<self.id>) <self.__dict__>
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
            )

    def save(self):
        """Updates the variable updated_at with the current time"""
        self.updated_at = datetime.today()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of an object"""
        n_dict = self.__dict__.copy()
        n_dict["__class__"] = type(self).__name__
        n_dict["created_at"] = n_dict.get("created_at").isoformat()
        n_dict["updated_at"] = n_dict.get("updated_at").isoformat()
        return n_dict
