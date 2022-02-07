#!/usr/bin/python3
""" Test cases for class Square """


import unittest
import io
import json
from models import square
from models.base import Base
from models.rectangle import Rectangle


class testcases(unittest.TestCase):
    """testing class square"""
    @classmethod
    def setUpClass(cls):
        Base._Base_objects = 0
        cls.c1 = Square(1)
        cls.c2 = Square(1, 2)
        cls.c3 = Square(2, 3, 4)
        cls.c4 = Square(4, 5, 6)
        cls.c5 = Square(6, 7, 8, 9)
        cls.c1.id = 1
        cls.c2.id = 2
        cls.c3.id = 3
        cls.c4.id = 4
        cls.c5.id = 5

    def test_square_instance(self):
        """Tests if Square is instance of Rectangle and Base"""
        ss = Square(5, 2, 1, 20)
        self.assertEqual(type(ss), Square)
        self.assertTrue(type(ss) == Square)
        self.assertFalse(type(ss) == Rectangle)
        self.assertFalse(type(ss) == Base)
        self.assertTrue(isinstance(ss, Base))
        self.assertTrue(isinstance(ss, Rectangle))
        self.assertTrue(isinstance(ss, Square))

    def test_id(self):
        self.assertEqual(self.c1.id, 1)
        self.assertEqual(self.c2.id, 2)
        self.assertEqual(self.c3.id, 3)
        self.assertEqual(self.c4.id, 4)
        self.assertEqual(self.c5.id, 5)

    def test_size(self):
        self.assertEqual(self.c1.size, 1)
        self.assertEqual(self.c2.size, 2)
        self.assertEqual(self.c3.size, 3)
        self.assertEqual(self.c4.size, 4)
        self.assertEqual(self.c5.size, 5)

    def test_width(self):
        self.assertEqual(self.c1.width, 1)
        self.assertEqual(self.c2.width, 2)
        self.assertEqual(self.c3.width, 3)
        self.assertEqual(self.c4.width, 4)
        self.assertEqual(self.c5.width, 5)

    def test_height(self):
        self.assertEqual(self.c1.height, 1)
        self.assertEqual(self.c2.height, 2)
        self.assertEqual(self.c3.height, 3)
        self.assertEqual(self.c4.height, 4)
        self.assertEqual(self.c5.height, 5)

    def test_x(self):
        self.assertEqual(self.c1.x, 1)
        self.assertEqual(self.c2.x, 2)
        self.assertEqual(self.c3.x, 3)
        self.assertEqual(self.c4.x, 4)
        self.assertEqual(self.c5.x, 5)

    def test_y(self):
        self.assertEqual(self.c1.y, 1)
        self.assertEqual(self.c2.y, 2)
        self.assertEqual(self.c3.y, 3)
        self.assertEqual(self.c4.y, 4)
        self.assertEqual(self.c5.y, 5)
