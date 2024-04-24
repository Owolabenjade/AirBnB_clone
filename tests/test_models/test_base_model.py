#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """
    Defines test cases for the BaseModel class functionalities.
    """

    def test_init(self):
        """
        Test normal instantiation and attribute types.
        """
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_str(self):
        """
        Test the __str__ method for correct format.
        """
        instance = BaseModel()
        expected = f"[BaseModel] ({instance.id}) {instance.__dict__}"
        self.assertEqual(str(instance), expected)

    def test_save(self):
        """
        Test the save method updates `updated_at`.
        """
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(old_updated_at, instance.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method includes correct keys and value types.
        """
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertIsInstance(instance_dict['created_at'], str)
        self.assertIsInstance(instance_dict['updated_at'], str)
        self.assertEqual(instance_dict['id'], instance.id)

    def test_init_kwargs(self):
        """
        Test instantiation with kwargs recreates the same instance.
        """
        instance1 = BaseModel()
        instance1_dict = instance1.to_dict()
        instance2 = BaseModel(**instance1_dict)
        self.assertEqual(instance1.id, instance2.id)
        self.assertEqual(instance1.created_at, instance2.created_at)
        self.assertEqual(instance1.updated_at, instance2.updated_at)
        self.assertNotEqual(instance1, instance2)

    def test_kwargs_none(self):
        """
        Test instantiation with kwargs as None does not fail.
        """
        with self.assertRaises(TypeError):
            instance = BaseModel(**None)

if __name__ == "__main__":
    unittest.main()

