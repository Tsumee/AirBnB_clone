#!/usr/bin/python3
"""Describes the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Presents the BaseModel of the AirBnB_clone project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Untouched arguments.
            **kwargs (dict): Pairs attributes for the key/value.
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        tm_format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for a, b in kwargs.items():
                if a == "created_at" or a == "updated_at":
                    self.__dict__[a] = datetime.strptime(b, tm_format)
                else:
                    self.__dict__[a] = b
        else:
            models.storage.new(self)

    def save(self):
        """Current datetime for updated_at."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Dictionary for Basemodel is being returned.
        Involes the key/value pairs __class__ repressenting
        the class name of the object are included."""
        arr_dictionary = self.__dict__.copy()
        arr_dictionary["created_at"] = self.created_at.isoformat()
        arr_dictionary["updated_at"] = self.updated_at.isoformat()
        arr_dictionary["__class__"] = self.__class__.__name__
        return arr_dictionary

    def __str__(self):
        """Return the print/str description of the BaseModel instance."""
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
