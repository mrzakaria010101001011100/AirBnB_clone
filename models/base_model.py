from datetime import datetime
from uuid import uuid4

class BaseModel:
    """
    BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """Initialization of the BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Return the string representation of BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy

class User(BaseModel):
    """
    User class extending BaseModel
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add specific attributes for User
        self.username = kwargs.get('username', '')
        self.email = kwargs.get('email', '')

    def __str__(self):
        return "[{}] ({}) {}: {}".format(self.__class__.__name__, self.id, self.username, self.email)

# Example usage
if __name__ == "__main__":
    user_data = {
            'id': '1',
            'username': 'john_doe',
            'email': 'john.doe@example.com',
            'created_at': '2024-03-12T12:00:00.000000',
            'updated_at': '2024-03-12T12:00:00.000000'
            }
    user = User(**user_data)
    print(user)
    user.save()
    print(user.to_dict())

