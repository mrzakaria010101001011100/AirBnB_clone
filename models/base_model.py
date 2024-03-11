#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage

class BaseModel:
<<<<<<< HEAD
"""BaseModel class"""
    def __init__(self, *args, **kwargs):
         # Initialize instance attributes from kwargs if provided
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    setattr(self, k, v)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
        else:
        """String representation of object"""
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
=======
    """
    Defines the BaseModel class
    """

    id_generator = uuid.uuid4

    def __init__(self):
        """
        Initializes a new instance of BaseModel
        """
        self.id = str(BaseModel.id_generator())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of BaseModel instance
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)
>>>>>>> d40fdfb86fa1ccf9557a1268e3e2cbef038bf4b6

    def save(self):
    """Save method to update updated_at and save instance to storage"""        self.updated_at = datetime.now()
      storage.save()

    def to_dict(self):
    """Convert object to dictionary"""
        obj_dict = self.__dict__.copy()
<<<<<<< HEAD
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
=======
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        obj_dict['updated_at'] = self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        return obj_dict
>>>>>>> d40fdfb86fa1ccf9557a1268e3e2cbef038bf4b6

# Test the BaseModel class
if __name__ == "__main__":
    # Creating an instance of BaseModel
    model = BaseModel()

    # Generating a dictionary representation of the instance
    model_dict = model.to_dict()

    # Re-creating an instance from the dictionary representation
    new_model = BaseModel(**model_dict)

    # Verifying the attributes of the new instance
    print(new_model.__dict__)
