#!/usr/python3
"""Rectangle module unit tests"""
import unittest
import sys
import os
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

    def test_rectangle_create(self):
        """Test - creates new instance of rectangle"""
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)
        r2 = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r2.id, 89)
        r3 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r3.id, 89)
        r4 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r4.id, 89)
        r5 = Rectangle.create(**{
            'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4
        })
        self.assertEqual(r5.id, 89)

    def test_rectangle_save_to_file(self):
        """Test - saves rectangle to file"""
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", 'r', encoding="utf-8") as file:
            r = file.read()
        self.assertEqual(
            r, '[{"id": 21, "width": 1, "height": 2, "x": 0, "y": 0}]')
        os.remove("Rectangle.json")

    def test_rectangle_save_to_file_empty(self):
        """Test - saves empty rectangle to file"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", 'r', encoding="utf-8") as file:
            r = file.read()
        self.assertEqual(r, '[]')

    def test_rectangle_save_to_file_none(self):
        """Test - saves None rectangle to file"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", 'r', encoding="utf-8") as file:
            r = file.read()
        self.assertEqual(r, '[]')

if __name__ == '__main__':
    unittest.main()
