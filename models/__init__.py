# Importing the FileStorage class from models.engine.file_storage module
from models.engine.file_storage import FileStorage

# Creating an instance of FileStorage
storage = FileStorage()

# Loading data from the JSON file into the storage instance
storage.reload()
