#!/usr/bin/python3
"""Defines unittests for models/rectangle.py.
"""

import unittest
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestRectangle(unittest.TestCase):
    """Test rectangle class"""

    def test_2_0(self):
        """Test ID"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        r4 = Rectangle(10, 2, 0, 0, -7)
        self.assertEqual(r4.id, -7)
        r5 = Rectangle(10, 2, 4, 5, 8)
        self.assertEqual(r5.id, 8)
    
    def test_2_1(self):
        """Test attribute value"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(10, 2, 4, 5, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 5)
    
    def test_2_2(self):
        """Test attribute value"""
        with self.assertRaises(TypeError):
            r = Rectangle(8)

if __name__ == "__main__":
    unittest.main()