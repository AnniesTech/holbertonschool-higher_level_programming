#!/usr/bin/python3
""" Tests for Base class """


import unittest
import pep8
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ Imports class Base """
    def test_pep8_base(self):
        """ Test that checks for PEP8 """
        syntax = pep8.StyleGuide(quit=True)
        result = syntax.check_files(['models/base.py'])
        self.assertEqual(
            result.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_id_as_positive(self):
        """ Test for positive id """
        base_instance = Base(10)
        self.assertEqual(base_instance.id, 10)
        base_instance = Base(20)
        self.assertEqual(base_instance.id, 20)

    def test_id_as_negative(self):
        """ Test for negative id """
        base_instance = Base(-20)
        self.assertEqual(base_instance.id, -20)
        base_instance = Base(-10)
        self.assertEqual(base_instance.id, -10)

    def test_tuple_id(self):
        """Test for tuple on id"""
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_id_as_none(self):
        """ Test for None id """
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)
        base_instance = Base(None)
        self.assertEqual(base_instance.id, 2)

    def test_string_id(self):
        """ Test id as a string """
        base_instance = Base("Hello world")
        self.assertEqual(base_instance.id, "Hello world")
        base_instance = Base("Lorem Ipsum")
        self.assertEqual(base_instance.id, "Lorem Ipsum")

    def test_instance(self):
        """ Test class Base  instance """
        base_instance = Base()
        self.assertEqual(type(base_instance), Base)
        self.assertTrue(isinstance(base_instance, Base))

    def test_to_json_string(self):
        """ Test to_json_string method """
        rectangle_instance = Rectangle(9, 10, 2, 8, 70)
        rectangle_data = re1.to_dictionary()
        json_data = Base.to_json_string([rect_data])
        self.assertEqual(type(json_data), str)

    def test_empty_to_json_string(self):
        """ Test for a empty data on to_json_string method """
        empty_data = []
        json_data = Base.to_json_string(empty_data)
        self.assertEqual(json_data, "[]")

        empty_data = None
        json_data = Base.to_json_string(empty_data)
        self.assertEqual(json_data, "[]")
