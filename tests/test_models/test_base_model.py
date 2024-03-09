#!/usr/bin/python3
"""
test_base_model.py: Unit test for BaseModel class
"""

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Defines test cases for the BaseModel class."""

    def setUp(self):
        """Method to set up test fixtures before exercising tests."""
        self.base_instance = BaseModel()

    def tearDown(self):
        """Method to clean up after test cases have run."""
        del self.base_instance

    def test_init(self):
        """Test initialization of base model instances."""
        self.assertIsInstance(self.base_instance, BaseModel)

    def test_id_creation(self):
        """Test if an ID is created for a new instance."""
        self.assertTrue(hasattr(self.base_instance, "id"))

    # More tests go here

if __name__ == '__main__':
    unittest.main()
