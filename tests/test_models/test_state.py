#1/usr/bin/python3
'''unittests for state class

unittest classes:
    TestInstantiation
    TestSave
    Test_to_dict
'''
import unittest
import models
from models.state import State
import os
from datetime import datetime
from time import sleep


class TestInstantiation(unittest.TestCase):
    ''' Tests for Instantiation for the state class'''

    def test_no_args(self):
        self.assertEqual(State, type(State()))
    
    def test_instance_in_objects(self):
        self.assertIn(State(), models.storage.all().values())
    
    def test_id(self):
        self.assertEqual(str, type(State().id))
    
    def test_created_at(self):
        self.assertEqual(datetime, type(State().created_at))
    
    def test_updated_at(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_name(self):
        staTe = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(staTe))
        self.assertNotIn("name", staTe.__dict__)
    
    def test_unique_ids(self):
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)


class TestSave(unittest.TestCase):
    '''unittests for the save method in State Class'''

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tempo")
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
        state_ = State()
        sleep(0.1)
        f_updated_at = state_.updated_at
        state_.save()
        self.assertLess(f_updated_at, state_.updated_at)

    def test_double_saves(self):
        state_ = State()
        sleep(0.1)
        f_updated_at = state_.updated_at
        state_.save()
        s_updated_at = state_.updated_at
        self.assertLess(f_updated_at, s_updated_at)
        sleep(0.1)
        state_.save()
        self.assertLess(s_updated_at, state_.updated_at)
    
    def test_save_withargs(self):
        state_ = State()
        with self.assertRaises(TypeError):
            state_.save(None)

    def test_saveFileUpdates(self):
        state_ = State()
        state_.save()
        _state_id = "State." + state_.id
        with open("file.json", "r") as f:
            self.assertIn(_state_id, f.read())
    

class Test_to_dict(unittest.TestCase):
    '''unittests for to_dict method in State class'''

    def test_type_to_dict(self):
        self.assertTrue(dict, type(State().to_dict()))
    
    def test_correctKeys_to_dict(self):
        state_ = State()
        self.assertIn("id", state_.to_dict())
        self.assertIn("created_at", state_.to_dict())
        self.assertIn("updated_at", state_.to_dict())
        self.assertIn("__class__", state_.to_dict())

    def test_hasAddedAttributes_to_dict(self):
        state_ = State()
        state_.middle_name = "Africa"
        state_.my_number = 50
        self.assertEqual("Africa", state_.middle_name)
        self.assertIn("my_number", state_.to_dict())

    def test_datetimeAttributesAreStrings_to_dict(self):
        state_ = State()
        _stateDictionary= state_.to_dict()
        self.assertEqual(str, type(_stateDictionary["id"]))
        self.assertEqual(str, type(_stateDictionary["created_at"]))
        self.assertEqual(str, type(_stateDictionary["updated_at"]))

    def test_output_to_dict(self):
        _date = datetime.today()
        state_ = State()
        state_.id = "123456"
        state_.created_at = state_.updated_at = _date
        dictionary = {
            'id': '123456',
            '__class__': 'State',
            'created_at': _date.isoformat(),
            'updated_at': _date.isoformat(),
        }
        self.assertDictEqual(state_.to_dict(), dictionary)

    def test_contrast_to_dict(self):
        state_ = State()
        self.assertNotEqual(state_.to_dict(), state_.__dict__)

    def test_to_dict_with_arg(self):
        state_ = State()
        with self.assertRaises(TypeError):
            state_.to_dict(None)


if __name__ == "__main__":
    unittest.main()
