#!/usr/bin/python3
'''Unit tests for Place Class

Unittest classes:
    Test_Instantiation
    Test_Save
    Test_to_dict

'''
import unittest
from models.place import Place
import os
import models
from datetime import datetime
from time import sleep


class Test_Instantiation(unittest.TestCase):
    '''Unit tests for Place class instantiation '''

    def test_zero_args(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_TypeOf_id(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_cityid(self):
        place_ = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(place_))
        self.assertNotIn("city_id", place_.__dict__)

    def test_name(self):
        place_ = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(place_))
        self.assertNotIn("name", place_.__dict__)

    def test_description(self):
        place_ = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(place_))
        self.assertNotIn("desctiption", place_.__dict__)

    def test_numberOfRooms(self):
        place_ = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(place_))
        self.assertNotIn("number_rooms", place_.__dict__)

    def test_numberOfBathrooms(self):
        place_ = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(place_))
        self.assertNotIn("number_bathrooms", place_.__dict__)

    def test_maxGuests(self):
        place_ = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(place_))
        self.assertNotIn("max_guest", place_.__dict__)

    def test_price_by_night(self):
        place_ = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(place_))
        self.assertNotIn("price_by_night", place_.__dict__)

    def test_latitude(self):
        place_ = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(place_))
        self.assertNotIn("latitude", place_.__dict__)

    def test_longitude(self):
        place_ = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(place_))
        self.assertNotIn("longitude", place_.__dict__)

    def test_amenity_ids(self):
        place_ = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(place_))
        self.assertNotIn("amenity_ids", place_.__dict__)

    def test_unique_ids(self):
        1place = Place()
        2place = Place()
        self.assertNotEqual(1place.id, 2place.id)

    def test_created_at(self):
        1place = Place()
        sleep(0.1)
        2place = Place()
        self.assertLess(1place.created_at, 2place.created_at)

    def test_updated_at(self):
        1place = Place()
        sleep(0.05)
        2place = Place()
        self.assertLess(1place.updated_at, 2place.updated_at)

    def test_unusedArgs(self):
        place_ = Place(None)
        self.assertNotIn(None, place_.__dict__.values())

    def test_Zero_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_kwargs(self):
        date_ = datetime.today()
        date_Format = date_.isoformat()
        place_ = Place(id="10111", created_at=date_Format, updated_at=date_Format)
        self.assertEqual(place_.id, "10111")
        self.assertEqual(place_.created_at, date_)
        self.assertEqual(place_.updated_at, date_)

class Test_Save(unittest.TestCase):
    '''Unit tests for save function in Place class'''

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_single_save(self):
        place_ = Place()
        sleep(0.1)
        first_updated_at = place_.updated_at
        place_.save()
        self.assertLess(first_updated_at, place_.updated_at)

    def test_double_save(self):
        place_ = Place()
        sleep(0.1)
        f_updated_at = place_.updated_at
        place_.save()
        s_updated_at = place_.updated_at
        self.assertLess(f_updated_at, s_updated_at)
        sleep(0.1)
        place_.save()
        self.assertLess(s_updated_at, place_.updated_at)

    def test_saveArg(self):
        place_ = Place()
        with self.assertRaises(TypeError):
            place_.save(None)

    def test_updatesFile_save(self):
        place_ = Place()
        place_.save()
        place_id = "Place." + place_.id
        with open("file.json", "r") as fl:
            self.assertIn(place_id, fl.read())


class Test_to_dict(unittest.TestCase):
    '''Unittests for Place class to_dict function'''

    def test_TypeOf_to_dict(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_Keys_to_dict(self):
        place_ = Place()
        self.assertIn("id", place_.to_dict())
        self.assertIn("created_at", place_.to_dict())
        self.assertIn("updated_at", place_.to_dict())
        self.assertIn("__class__", place_.to_dict())

    def test_extra_to_dict(self):
        place_ = Place()
        place_.middle_name = "Africa"
        place_.my_number = 123
        self.assertEqual("Africa", place_.middle_name)
        self.assertIn("my_number", place_.to_dict())

    def testdate_time_to_dict(self):
        place_ = Place()
        place__dict = place_.to_dict()
        self.assertEqual(str, type(place__dict["id"]))
        self.assertEqual(str, type(place__dict["created_at"]))
        self.assertEqual(str, type(place__dict["updated_at"]))

    def contract_to_dict(self):
        place_ = Place()
        self.assertNotEqual(place_.to_dict(), place_.__dict__)

    def test_arg_to_dict(self):
        place_ = Place()
        with self.assertRaises(TypeError):
            place_.to_dict(None)


if __name__ == "__main__":
    unittest.main()
