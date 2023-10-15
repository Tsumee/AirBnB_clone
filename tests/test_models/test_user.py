#!/usr/bin/python3
'''Unit tests for User class

Unittest classes:
    Test_Instantiation
    Test_Save
    Test_to_dict
'''
import unittest
import models
from models.user import User
import os
from datetime import datetime
from time import sleep


class Test_Instantiation(unittest.TestCase):
    '''Unittests for user class instances'''

    def test_zero_Instantiation(self):
        self.assertEqual(User, type(User()))

    def test_new_instance(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(User().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is(self):
        self.assertEqual(str, type(User.email))

    def test_password(self):
        self.assertEqual(str, type(User.password))

    def test_first_name(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name(self):
        self.assertEqual(str, type(User.last_name))

    def test_unique_ids(self):
        1user = User()
        2user = User()
        self.assertNotEqual(1user.id, 2user.id)

    def test_created_at(self):
        1user = User()
        sleep(0.1)
        2user = User()
        self.assertLess(1user.created_at, 2user.created_at)

    def test_updated_at(self):
        1user = User()
        sleep(0.1)
        2user = User()
        self.assertLess(1user.updated_at, 2user.updated_at)

    def test_UnusedArgs(self):
        user_ = User(None)
        self.assertNotIn(None, user_.__dict__.values())

    def test_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_kwargs(self):
        date_ = datetime.today()
        _dateFormat = date_.isoformat()
        user_ = User(id="10111", created_at=_dateFormat, updated_at=_dateFormat)
        self.assertEqual(user_.id, "10111")
        self.assertEqual(user_.created_at, date_)
        self.assertEqual(user_.updated_at, date_)


class Test_Save(unittest.TestCase):
    '''Unittests for save function in User class.'''

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
        user_= User()
        sleep(0.1)
        f_updated_at = user_.updated_at
        user_.save()
        self.assertLess(f_updated_at, user_.updated_at)

    def test_double_save(self):
        user_ = User()
        sleep(0.1)
        f_updated_at = user_.updated_at
        user_.save()
        s_updated_at = user_.updated_at
        self.assertLess(f_updated_at, s_updated_at)
        sleep(0.1)
        user_.save()
        self.assertLess(s_updated_at, user_.updated_at)

    def test_args(self):
        user_ = User()
        with self.assertRaises(TypeError):
            user_.save(None)

    def test_saveFileUpdates(self):
        user_ = User()
        user_.save()
        user_rid = "User." + user_.id
        with open("file.json", "r") as fl:
            self.assertIn(user_rid, fl.read())


class Test_to_dict(unittest.TestCase):
    '''Unittests for to_dict function in User class.'''

    def test_TypeOf_to_dict(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_keys_to_dict(self):
        user_ = User()
        self.assertIn("id", user_.to_dict())
        self.assertIn("created_at", user_.to_dict())
        self.assertIn("updated_at", user_.to_dict())
        self.assertIn("__class__", user_.to_dict())

    def test_to_dict_contains_added_attributes(self):
        user_ = User()
        user_.middle_name = "Africa"
        user_.my_number = 23
        self.assertEqual("Africa", user_.middle_name)
        self.assertIn("my_number", user_.to_dict())

    def test_to_dict_datetime(self):
        user_ = User()
        _user_dict = user_.to_dict()
        self.assertEqual(str, type(_user_dict["id"]))
        self.assertEqual(str, type(_user_dict["created_at"]))
        self.assertEqual(str, type(_user_dict["updated_at"]))

    def test_contrast_to_dict_(self):
        user_ = User()
        self.assertNotEqual(user_.to_dict(), user_.__dict__)

    def test_args(self):
        user_ = User()
        with self.assertRaises(TypeError):
            user_.to_dict(None)


if __name__ == "__main__":
    unittest.main()
