#!/usr/bin/python3
"""
Unit tests for the FileStorage class.
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    @classmethod
    def setUpClass(cls):
        """Set up for the test cases."""
        cls.storage = FileStorage()
        cls.storage_file = FileStorage._FileStorage__file_path

    def tearDown(self):
        """Clean up files (if any) created by the test cases."""
        try:
            os.remove(self.storage_file)
        except FileNotFoundError:
            pass

    def test_all_returns_dict(self):
        """Test that all returns a dictionary."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test that new adds an object to the storage dictionary."""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn(f"BaseModel.{obj.id}", self.storage.all())

    def test_save(self):
        """Test that save correctly saves objects to file storage."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage_file))

    def test_reload(self):
        """Test that reload correctly loads objects from file storage."""
        obj = BaseModel()
        obj_id = obj.id
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        objects = self.storage.all()
        self.assertIn(f"BaseModel.{obj_id}", objects)

if __name__ == '__main__':
    unittest.main()

