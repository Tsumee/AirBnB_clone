#!/usr/bin/python3
"""Describes unittests for models/amenity.
Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Amenity class testing for instantiation Unittests."""

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        amnity = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amnity.__dict__)

    def test_two_amenities_unique_ids(self):
        amnity_1 = Amenity()
        amnity_2 = Amenity()
        self.assertNotEqual(amnity_1.id, amnity_2.id)

    def test_two_amenities_different_created_at(self):
        amnity_1 = Amenity()
        sleep(0.05)
        amnity_2 = Amenity()
        self.assertLess(amnity_1.created_at, amnity_2.created_at)

    def test_two_amenities_different_updated_at(self):
        amnity_1 = Amenity()
        sleep(0.05)
        amnity_2 = Amenity()
        self.assertLess(amnity_1.updated_at, amnity_2.updated_at)

    def test_str_representation(self):
        dayt = datetime.today()
        day-rrp = repr(dayt)
        amnity = Amenity()
        amnity.id = "123456"
        amnity.created_at = amnity.updated_at = dayt
        amnity_st = amnity.__str__()
        self.assertIn("[Amenity] (123456)", amnity_st)
        self.assertIn("'id': '123456'", amnity_st)
        self.assertIn("'created_at': " + day-rrp, amnity_st)
        self.assertIn("'updated_at': " + day-rrp, amnity_st)

    def test_args_unused(self):
        amnity = Amenity(None)
        self.assertNotIn(None, amnity.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        dayt = datetime.today()
        day_ssi = dayt.isoformat()
        amnity = Amenity(id="345", created_at=day_ssi, updated_at=day_ssi)
        self.assertEqual(amnity.id, "345")
        self.assertEqual(amnity.created_at, dayt)
        self.assertEqual(amnity.updated_at, dayt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """Save method for Unittest with Amenity class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

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
        amnity = Amenity()
        sleep(0.05)
        first_updated_at = amnity.updated_at
        amnity.save()
        self.assertLess(first_updated_at, amnity.updated_at)

    def test_two_saves(self):
        amnity = Amenity()
        sleep(0.05)
        first_updated_at = amnity.updated_at
        amnity.save()
        second_updated_at = amnity.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amnity.save()
        self.assertLess(second_updated_at, amnity.updated_at)

    def test_save_with_arg(self):
        amnity = Amenity()
        with self.assertRaises(TypeError):
            amnity.save(None)

    def test_save_updates_file(self):
        amnity = Amenity()
        amnity.save()
        amnity_mod = "Amenity." + amnity.id
        with open("file.json", "r") as x:
            self.assertIn(amnity_mod, x.read())


class TestAmenity_to_dict(unittest.TestCase):
    """to_dict method for Unittest for Amenity class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        amnity = Amenity()
        self.assertIn("id", amnity.to_dict())
        self.assertIn("created_at", amnity.to_dict())
        self.assertIn("updated_at", amnity.to_dict())
        self.assertIn("__class__", amnity.to_dict())

    def test_to_dict_contains_added_attributes(self):
        amnity = Amenity()
        amnity.middle_name = "AirBnB"
        amnit.my_number = 90
        self.assertEqual("AirBnB", amnity.middle_name)
        self.assertIn("my_number", amnity.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        amnity = Amenity()
        amn_dct = amnity.to_dict()
        self.assertEqual(str, type(amn_dct["id"]))
        self.assertEqual(str, type(amn_dct["created_at"]))
        self.assertEqual(str, type(amn_dct["updated_at"]))

    def test_to_dict_output(self):
        dayt = datetime.today()
        amnity = Amenity()
        amnity.id = "123456"
        amnity.created_at = amnity.updated_at = dayt
        dict_tc = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dayt.isoformat(),
            'updated_at': dayt.isoformat(),
        }
        self.assertDictEqual(amnity.to_dict(), dict_tc)

    def test_contrast_to_dict_dunder_dict(self):
        amnity = Amenity()
        self.assertNotEqual(amnity.to_dict(), amnity.__dict__)

    def test_to_dict_with_arg(self):
        amnity = Amenity()
        with self.assertRaises(TypeError):
            amnity.to_dict(None)


if __name__ == "__main__":
    unittest.main()
