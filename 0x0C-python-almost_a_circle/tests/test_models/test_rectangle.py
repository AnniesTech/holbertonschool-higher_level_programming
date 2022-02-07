#!/usr/bin/python3
"""Tests for Class Rectangle"""


import unittest
import pep8
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ Imports class Rectangle """
    def test_pep8_base(self):
        """ Test that checks for PEP8 """
        syntax = pep8.StyleGuide(quit=True)
        result = syntax.check_files(['models/rectangle.py'])
        self.assertEqual(
            result.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def set_up(self):
        """set to 0 the number of objects"""
        Base._Base__nb_objects = 0

    def test_rectangle_is_base(self):
        """Test for base in rec"""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        """Test with no arguments"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """Test with one argument"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        """Test with 2 arguments"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        """Test with 3 arguments"""
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        """Test with 4 arguments"""
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        """Test with 5 arguments"""
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        """Test with more than 5 arguments"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        """Test with private attribute width"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        """Test with private attribute height"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        """Test with private attribute x"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        """Test with private attribute y"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        """Test with width getter"""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        """Test with width getter"""
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        """Test with height getter"""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        """Test with height setter"""
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        """Test with x getter"""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        """Test with x setter"""
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        """Test with y getter"""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        """Test with y getter"""
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)
