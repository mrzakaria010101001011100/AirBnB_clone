#!/usr/bin/python3
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Clean file"""

    def setUp(self):
        self.file_storage = FileStorage()
        setattr(FileStorage, "_FileStorage__objects", {})

    def tearDown(self):
        """Clean file"""
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_reload(self):
        try:
            self.file_storage.reload()
        except Exception as e:
            self.fail(f"reload() raised an unexpected exception: {e}")

    def test_create_object(self):
        """Test create_object method"""
        objec = BaseModel()
        self.storage.create_object(objec)
        all_objcs = self.storage.get_all()
        self.assertIn("BaseModel." + objec.id, all_objcs)

    def test_reload_empty_file(self):
        """Test reload empty file"""
        open(FileStorage._FileStorage__file_path, "w").close()
        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.get_all()
        self.assertEqual(len(all_objs), 0)


if __name__ == '__main__':
    unittest.main()
