#!/usr/bin/python3
'''Unit tests for review class

Unittest classes:
    Test_Instantiation
    Test_Save
    Test_to_dict
'''
import unittest
import models
from models.review import Review
import os
from datetime import datetime
from time import sleep


class Test_Instantiation(unittest.TestCase):
    '''Unit tests for review class Instantiation'''

    def test_zero_args(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id(self):
        review_ = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(review_))
        self.assertNotIn("place_id", review_.__dict__)

    def test_user_id(self):
        review_ = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(review_))
        self.assertNotIn("user_id", review_.__dict__)

    def test_text(self):
        review_ = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(review_))
        self.assertNotIn("text", review_.__dict__)

    def test_unique_ids(self):
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_double_created_at(self):
        review1= Review()
        sleep(0.1)
        review2 = Review()
        self.assertLess(review1.created_at, review2.created_at)

    def test_double_updated_at(self):
        review1 = Review()
        sleep(0.1)
        review2 = Review()
        self.assertLess(review1.updated_at, review2.updated_at)

    def test_unusedArgs(self):
        review_ = Review(None)
        self.assertNotIn(None, review_.__dict__.values())

    def test_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_kwargs(self):
        _date = datetime.today()
        _dateFormat = _date.isoformat()
        review_ = Review(id="10111", created_at=_dateFormat, updated_at=_dateFormat)
        self.assertEqual(review_.id, "10111")
        self.assertEqual(review_.created_at, _date)
        self.assertEqual(review_.updated_at, _date)


class Test_Save(unittest.TestCase):
    '''Unittests for save function for Review class.'''

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
        review_ = Review()
        sleep(0.1)
        f_updated_at = review_.updated_at
        review_.save()
        self.assertLess(f_updated_at, review_.updated_at)

    def test_double_save(self):
        review_ = Review()
        sleep(0.1)
        f_updated_at = review_.updated_at
        review_.save()
        s_updated_at = review_.updated_at
        self.assertLess(f_updated_at, s_updated_at)
        sleep(0.1)
        review_.save()
        self.assertLess(s_updated_at, review_.updated_at)

    def test_save_arg(self):
        review_ = Review()
        with self.assertRaises(TypeError):
            review_.save(None)

    def test_updatesFile(self):
        review_ = Review()
        review_.save()
        review_id = "Review." + review_.id
        with open("file.json", "r") as fl:
            self.assertIn(review_id, fl.read())


class Test_to_dict(unittest.TestCase):
    '''Unittests for to_dict function in Review class.'''

    def test_TypeOf_to_dict(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_Keys_to_dict(self):
        review_ = Review()
        self.assertIn("id", review_.to_dict())
        self.assertIn("created_at", review_.to_dict())
        self.assertIn("updated_at", review_.to_dict())
        self.assertIn("__class__", review_.to_dict())

    def test_extraAttributes_to_dict(self):
        review_ = Review()
        review_.middle_name = "Africa"
        review_.my_number = 10
        self.assertEqual("Africa", review_.middle_name)
        self.assertIn("my_number", review_.to_dict())

    def test_to_dict_datetime(self):
        review_ = Review()
        review__dict = review_.to_dict()
        self.assertEqual(str, type(review__dict["id"]))
        self.assertEqual(str, type(review__dict["created_at"]))
        self.assertEqual(str, type(review__dict["updated_at"]))

    def test_contrast_to_dict(self):
        review_ = Review()
        self.assertNotEqual(review_.to_dict(), review_.__dict__)

    def test_to_dict_arg(self):
        review_ = Review()
        with self.assertRaises(TypeError):
            review_.to_dict(None)


if __name__ == "__main__":
    unittest.main()
