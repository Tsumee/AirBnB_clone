#!/usr/bin/python3
"""Describes unittests for models/m_baseodel.
Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.m_baseodel import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Testing instantiation for Unittest with BaseModel class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        m1_base = BaseModel()
        m2_base = BaseModel()
        self.assertNotEqual(m1_base.id, m2_base.id)

    def test_two_models_different_created_at(self):
        m1_base = BaseModel()
        sleep(0.05)
        m2_base = BaseModel()
        self.assertLess(m1_base.created_at, m2_base.created_at)

    def test_two_models_different_updated_at(self):
        m1_base = BaseModel()
        sleep(0.05)
        m2_base = BaseModel()
        self.assertLess(m1_base.updated_at, m2_base.updated_at)

    def test_str_representation(self):
        dayt = datetime.today()
        day_ssi = repr(dayt)
        m_base = BaseModel()
        m_base.id = "123456"
        m_base.created_at = m_base.updated_at = dayt
        m_base_str = m_base.__str__()
        self.assertIn("[BaseModel] (123456)", m_base_str)
        self.assertIn("'id': '123456'", m_base_str)
        self.assertIn("'created_at': " + day_ssi, m_base_str)
        self.assertIn("'updated_at': " + day_ssi, m_base_str)

    def test_args_unused(self):
        m_base = BaseModel(None)
        self.assertNotIn(None, m_base.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dayt = datetime.today()
        day_iss = dayt.isoformat()
        m_base = BaseModel(id="345", created_at=day_iss, updated_at=day_iss)
        self.assertEqual(m_base.id, "345")
        self.assertEqual(m_base.created_at, dayt)
        self.assertEqual(m_base.updated_at, dayt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dayt = datetime.today()
        day_iss = dayt.isoformat()
        m_base = BaseModel("12", id="345", created_at=day_iss, updated_at=day_iss)
        self.assertEqual(m_base.id, "345")
        self.assertEqual(m_base.created_at, dayt)
        self.assertEqual(m_base.updated_at, dayt)


class TestBaseModel_save(unittest.TestCase):
    """Save method for Unittest with BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        m_base = BaseModel()
        sleep(0.05)
        first_updated_at = m_base.updated_at
        m_base.save()
        self.assertLess(first_updated_at, m_base.updated_at)

    def test_two_saves(self):
        m_base = BaseModel()
        sleep(0.05)
        first_updated_at = m_base.updated_at
        m_base.save()
        second_updated_at = m_base.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        m_base.save()
        self.assertLess(second_updated_at, m_base.updated_at)

    def test_save_with_arg(self):
        m_base = BaseModel()
        with self.assertRaises(TypeError):
            m_base.save(None)

    def test_save_updates_file(self):
        m_base = BaseModel()
        m_base.save()
        m_base_id = "BaseModel." + m_base.id
        with open("file.json", "r") as x:
            self.assertIn(m_base_id, x.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """to_dict method for Unittest eith BaseModdel class."""

    def test_to_dict_type(self):
        m_base = BaseModel()
        self.assertTrue(dict, type(m_base.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        m_base = BaseModel()
        self.assertIn("id", m_base.to_dict())
        self.assertIn("created_at", m_base.to_dict())
        self.assertIn("updated_at", m_base.to_dict())
        self.assertIn("__class__", m_base.to_dict())

    def test_to_dict_contains_added_attributes(self):
        m_base = BaseModel()
        m_base.name = "AirBnB"
        m_base.my_number = 90
        self.assertIn("name", m_base.to_dict())
        self.assertIn("my_number", m_base.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        m_base = BaseModel()
        dict_bm = m_base.to_dict()
        self.assertEqual(str, type(dict_bm["created_at"]))
        self.assertEqual(str, type(dict_bm["updated_at"]))

    def test_to_dict_output(self):
        dayt = datetime.today()
        m_base = BaseModel()
        m_base.id = "123456"
        m_base.created_at = m_base.updated_at = dayt
        tt_dict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dayt.isoformat(),
            'updated_at': dayt.isoformat()
        }
        self.assertDictEqual(m_base.to_dict(), tt_dict)

    def test_contrast_to_dict_dunder_dict(self):
        m_base = BaseModel()
        self.assertNotEqual(m_base.to_dict(), m_base.__dict__)

    def test_to_dict_with_arg(self):
        m_base = BaseModel()
        with self.assertRaises(TypeError):
            m_base.to_dict(None)


if __name__ == "__main__":
    unittest.main()

