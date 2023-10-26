#!/usr/python3
"""Rectangle module unit tests"""
import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Rectangle unit tests"""

    def test_rectangle_expect(self):
        """Test - width/height/x/y/id is an int"""
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)
        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r4.width, 1)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 3)
        self.assertEqual(r4.y, 4)
        self.assertEqual(r4.id, 5)

    def test_rectangle_area(self):
        """Test - area of the rectangle"""
        r = Rectangle(1, 2)
        expect = 2
        self.assertEqual(r.area(), expect)

    def test_rectangle_string(self):
        """Test - an arg is a string"""
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "4")

    def test_rectangle_neg(self):
        """Test - an arg is neg"""
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4)

    def test_rectangle_zero(self):
        """Test - an arg is zero"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

    def test_rectangle_str(self):
        """Test - prints the str specified"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_rectangle_display_missing(self):
        """Test - display as expected without x or y"""
        output = StringIO()
        sys.stdout = output
        r = Rectangle(1, 1)
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "#\n")

    def test_rectangle_display_x_y(self):
        """Test - display as expected with x and y"""
        output = StringIO()
        sys.stdout = output
        r = Rectangle(1, 1, 1, 1)
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n #\n")

    def test_rectangle_display_x(self):
        """Test - display as expected with x and no y"""
        output = StringIO()
        sys.stdout = output
        r = Rectangle(1, 1, 1)
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), " #\n")

    def test_rectangle_update(self):
        """Test - update as expected"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(89)
        self.assertEqual(r.id, 89)
        r2 = Rectangle(1, 2, 3, 4, 5)
        r2.update(89, 1)
        self.assertEqual(r2.id, 89, 1)
        r3 = Rectangle(1, 2, 3, 4, 5)
        r3.update(89, 1, 2)
        self.assertEqual(r3.id, 89, 1)
        r4 = Rectangle(1, 2, 3, 4, 5)
        r4.update(89, 1, 2, 3)
        self.assertEqual(r4.id, 89, 1)

if __name__ == '__main__':
    unittest.main()
