#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage


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


if __name__ == '__main__':
    unittest.main()
