#!/usr/bin/env python3
"""
test module for testing place models
"""

import datetime
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlaceModel(unittest.TestCase):
    """test class for testing place models
    """
    def setUp(self):
        self.temp_b = Place()

    def tearDown(self):
        self.temp_b = None

    def test_type(self):
        """test method for type testing of place model
        """
        self.assertIsInstance(self.temp_b, Place)
        self.assertEqual(type(self.temp_b), Place)
        self.assertEqual(issubclass(self.temp_b.__class__, BaseModel), True)

    def test_basic_attribute_set(self):
        """test method for basic attribute assignment
        """
        self.temp_b.name = "bennett"
        self.temp_b.xyz = 400
        self.assertEqual(self.temp_b.name, "bennett")
        self.assertEqual(self.temp_b.xyz, 400)

    def test_string_return(self):
        """tests the string method to make sure it returns
            the proper string
        """
        my_str = str(self.temp_b)
        id_test = "[{}] ({})".format(self.temp_b.__class__.__name__,
                                     self.temp_b.id)
        boolean = id_test in my_str
        self.assertEqual(True, boolean)
        boolean = "updated_at" in my_str
        self.assertEqual(True, boolean)
        boolean = "created_at" in my_str
        self.assertEqual(True, boolean)
        boolean = "datetime.datetime" in my_str
        self.assertEqual(True, boolean)

    def test_to_dict(self):
        """tests the to_dict method to make sure properly working
        """
        my_dict = self.temp_b.to_dict()
        self.assertEqual(str, type(my_dict['created_at']))
        self.assertEqual(my_dict['created_at'],
                         self.temp_b.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.temp_b.created_at))
        self.assertEqual(my_dict['__class__'],
                         self.temp_b.__class__.__name__)
        self.assertEqual(my_dict['id'], self.temp_b.id)

    def test_to_dict_more(self):
        """tests more things with to_dict method
        """
        my_dict = self.temp_b.to_dict()
        created_at = my_dict['created_at']
        time = datetime.datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(self.temp_b.created_at, time)

    def test_from_dict_basic(self):
        """tests the from_dict method
        """
        my_dict = self.temp_b.to_dict()
        my_base = self.temp_b.__class__(**my_dict)
        self.assertEqual(my_base.id, self.temp_b.id)
        self.assertEqual(my_base.updated_at, self.temp_b.updated_at)
        self.assertEqual(my_base.created_at, self.temp_b.created_at)
        self.assertEqual(my_base.__class__.__name__,
                         self.temp_b.__class__.__name__)

    def test_from_dict_hard(self):
        """test for the from_dict method for class objects
        """
        self.temp_b.random = "hello!"
        self.temp_b.z = 55
        self.temp_b.amenity_ids = ['90870987907', '0897909', '987907']
        my_dict = self.temp_b.to_dict()
        self.assertEqual(my_dict['z'], 55)
        my_base = self.temp_b.__class__(**my_dict)
        self.assertEqual(my_base.z, self.temp_b.z)
        self.assertEqual(my_base.random, self.temp_b.random)
        self.assertEqual(my_base.created_at, self.temp_b.created_at)
        self.assertEqual(type(my_base.number_rooms), int)
        self.assertEqual(type(my_base.number_bathrooms), int)
        self.assertEqual(type(my_base.max_guest), int)
        self.assertEqual(type(my_base.price_by_night), int)
        self.assertEqual(type(my_base.latitude), float)
        self.assertEqual(type(my_base.longitude), float)
        self.assertEqual(type(my_base.amenity_ids), list)
        self.assertEqual(self.temp_b.number_rooms, my_base.number_rooms)
        self.assertEqual(self.temp_b.number_bathrooms,
                         my_base.number_bathrooms)
        self.assertEqual(self.temp_b.max_guest, my_base.max_guest)
        self.assertEqual(self.temp_b.price_by_night, my_base.price_by_night)
        self.assertEqual(self.temp_b.latitude, my_base.latitude)
        self.assertEqual(self.temp_b.longitude, my_base.longitude)
        self.assertEqual(self.temp_b.amenity_ids, my_base.amenity_ids)

    def test_unique_id(self):
        """test for unique ids for class objects
        """
        another = self.temp_b.__class__()
        another2 = self.temp_b.__class__()
        self.assertNotEqual(self.temp_b.id, another.id)
        self.assertNotEqual(self.temp_b.id, another2.id)

    def test_id_type_string(self):
        """test id of the class is a string
        """
        self.assertEqual(type(self.temp_b.id), str)

    def test_updated_time(self):
        """test that updated time gets updated
        """
        time1 = self.temp_b.updated_at
        self.temp_b.save()
        time2 = self.temp_b.updated_at
        self.assertNotEqual(time1, time2)
        self.assertEqual(type(time1), datetime.datetime)