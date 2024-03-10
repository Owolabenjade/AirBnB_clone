#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ TestBaseModel class to run tests against BaseModel class """

    def test_init(self):
        """ Test instantiation of BaseModel class """
        model = BaseModel()
        self.assertIs(type(model), BaseModel)
        self.assertIs(type(model.id), str)
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))

    def test_str(self):
        """ Test that the str method has the correct output """
        model = BaseModel()
        string = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), string)

    def test_save(self):
        """ Test the save method """
        model = BaseModel()
        update_before = model.updated_at
        model.save()
        update_after = model.updated_at
        self.assertNotEqual(update_before, update_after)

    def test_to_dict(self):
        """ Test conversion of model to dictionary """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIs(type(model_dict), dict)
        self.assertTrue('to_dict' not in model_dict)

    def test_kwargs_init(self):
        """ Test initialization of BaseModel with kwargs """
        model = BaseModel()
        model_dict = model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertFalse(model is new_model)
        self.assertEqual(model.id, new_model.id)
        self.assertEqual(model.created_at, new_model.created_at)
        self.assertEqual(model.updated_at, new_model.updated_at)
        self.assertEqual(model.to_dict(), new_model.to_dict())

    def test_kwargs_none(self):
        """ Test that passing kwargs as None doesn't throw error """
        with self.assertRaises(TypeError):
            BaseModel(None)

    def test_created_updated_iso(self):
        """ Test that created_at, updated_at are in ISO format in dict """
        model = BaseModel()
        model_dict = model.to_dict()

        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
