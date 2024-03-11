#!/usr/bin/python3
import datetime
import uuid
import models


class BaseModel:
    """
    BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """Initialization of the BaseModel"""
        if kwargs:
            for key, valu in kwargs.items():
                if key != "__class__":
                    if key in ['created_at', 'updated_at']:
                        valu = datetime.datetime.strptime(valu, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, valu)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Return the string representation of BaseModel"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.save()
        # Ensure the object is added to storage after saving to file

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        dict_copy = self.__dict__.copy()
        dict_copy['id'] = self.id
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
