#!/usr/bin/python3
'''Unit tests for the City Class

Unittest classes:
    Test_Instantiation
    Test_Save
    Test_to_dict

'''
import unittest
from models.city import City
import os
import models
from datetime import datetime
from time import sleep


class Test_Instantiation(unittest.TestCase):
    '''Unit tests for the instantation of City class'''

    def test_no_args(self):
        self.assertEqual(City, type(City()))

    def test_new_instance(self):
        self.assertIn(City(), models.storage.all().values())

    def test_TypeOf_id(self):
        self.assertEqual(str, type(City().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_stateid(self):
        city_ = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(city_))
        self.assertNotIn("state_id", city_.__dict__)

    def test_name(self):
        city_ = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(city_))
        self.assertNotIn("name", city_.__dict__)

    def test_uniqueIds(self):
        1city = City()
        2city = City()
        self.assertNotEqual(1city.id, 2city.id)

    def test_different_created_at(self):
        1city = City()
        sleep(0.1)
        2city = City()
        self.assertLess(1city.created_at, 2city.created_at)

    def test_different_updated_at(self):
        1city = City()
        sleep(0.1)
        2city = City()
        self.assertLess(1city.updated_at, 2city.updated_at)

    def test_args(self):
        city_ = City(None)
        self.assertNotIn(None, city_.__dict__.values())

    def test_nokwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_kwargs(self):
        date_ = datetime.today()
        _dateFormat = date_.isoformat()
        city_ = City(id="10111", created_at=_dateFormat, updated_at=_dateFormat)
        self.assertEqual(city_.id, "10111")
        self.assertEqual(city_.created_at, date_)
        self.assertEqual(city_.updated_at, date_)


class Test_Save(unittest.TestCase):
    '''Unit tests for save function in the City class'''

    @classmethod
    def setUp(self):
        try:
            os.rename("filename.json", "tempo")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tempo", "file.json")
        except IOError:
            pass

    def test_single_save(self):
        city_ = City()
        sleep(0.1)
        f_updated_at = city_.updated_at
        city_.save()
        self.assertLess(f_updated_at, city_.updated_at)

    def test_double_save(self):
        city_ = City()
        sleep(0.1)
        f_updated_at = city_.updated_at
        city_.save()
        s_updated_at = city_.updated_at
        self.assertLess(f_updated_at, s_updated_at)
        sleep(0.1)
        city_.save()
        self.assertLess(s_updated_at, city_.updated_at)

    def test_args_save(self):
        city_ = City()
        with self.assertRaises(TypeError):
            city_.save(None)

    def test_save_updatedFiles(self):
        city_ = City()
        city_.save()
        _cityid = "City." + city_.id
        with open("file.json", "r") as fl:
            self.assertIn(_cityid, fl.read())


class Test_to_dict(unittest.TestCase):
    '''Unit tests for to_dict function in City class'''

    def test_TypeOf_to_dict(self):
        self.assertTrue(dict, type(City().to_dict))

    def test_Keys_to_dict(self):
        city_ = City()
        self.assertIn("id", city_.to_dict())
        self.assertIn("created_at", city_.to_dict())
        self.assertIn("updated_at", city_.to_dict())
        self.assertIn("__class__", city_.to_dict())

    def test_extraAttributes_to_dict(self):
        city_ = City()
        _cityDict = city_.to_dict()
        self.assertEqual(str, type(_cityDict["id"]))
        self.assertEqual(str, type(_cityDict["created_at"]))
        self.assertEqual(str, type(_cityDict["updated_at"]))

    def test_contrast_to_dict(self):
        city_ = City()
        self.assertNotEqual(city_.to_dict(), city_.__dict__)

    def test_args_to_dict(self):
        city_ = City()
        with self.assertRaises(TypeError):
            city_.to_dict(None)


if __name__ == "__main__":
    unittest.main()
