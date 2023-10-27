#!/usr/python3
"""Square module unit tests"""
import unittest
import sys
import os
from io import StringIO
from models.square import Square

class TestSquare(unittest.TestCase):
    """Square unit tests"""

    def test_square_expect(self):
        """Test - size/x/y/id is an int"""
        s =  Square(1)
        self.assertEqual(s.size, 1)
        s2 = Square(1, 2)
        self.assertEqual(s2.x, 2)
        s3 = Square(1, 2, 3)
        self.assertEqual(s3.y, 3)
        s4 = Square(1, 2, 3, 4)
        self.assertEqual(s4.id, 4)

    def test_square_area(self):
        """Test - area of the square"""
        s = Square(1)
        expect = 1
        self.assertEqual(s.area(), expect)

    def test_square_string(self):
        """Test - an arg is a string"""
        with self.assertRaises(TypeError):
            s = Square("1")
        with self.assertRaises(TypeError):
            s = Square(1, "2")
        with self.assertRaises(TypeError):
            s = Square(1, 2, "3")

    def test_square_neg(self):
        """Test - an arg is neg"""
        with self.assertRaises(ValueError):
            s = Square(-1)
        with self.assertRaises(ValueError):
            s = Square(1, -2)
        with self.assertRaises(ValueError):
            s = Square(1, 2, -3)

    def test_square_zero(self):
        """Test - an arg is zero"""
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_square_display_str(self):
        """Test - prints the str specified"""
        s = Square(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 1")

    def test_square_display_missing(self):
        """Test - display as expected without x or y"""
        output = StringIO()
        sys.stdout = output
        s = Square(1)
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "#\n")

    def test_square_display_x_y(self):
        """Test - display as expected with x and y"""
        output = StringIO()
        sys.stdout = output
        s = Square(1, 2, 3)
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n\n\n  #\n")

    def test_square_display_x(self):
        """Test - display as expected with x and no y"""
        output = StringIO()
        sys.stdout = output
        s = Square(1, 2)
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "  #\n")

    def test_square_update(self):
        """Test - update as expected"""
        s = Square(1, 1, 1, 1)
        s.update(89)
        self.assertEqual(s.id, 89)
        s2 = Square(1, 1, 1, 1)
        s2.update(89, 1)
        self.assertEqual(s2.x, 1)
        s3 = Square(1, 1, 1, 1)
        s3.update(89, 1, 2)
        self.assertEqual(s3.x, 2)
        s4 = Square(1, 1, 1, 1)
        s4.update(89, 1, 2, 3)
        self.assertEqual(s4.y, 3)

    def test_square_create(self):
        """Test - creates new instance of square"""
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)
        s2 = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s2.size, 1)
        s3 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s3.x, 2)
        s4 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s4.y, 3)

    def test_square_save_to_file(self):
        """Test - save square to file"""
        Square.save_to_file([Square(1, 2)])
        with open("Square.json", 'r', encoding="utf-8") as file:
            s = file.read()
        self.assertEqual(
            s, '[{"id": 44, "x": 2, "size": 1, "y": 0}]')

    def test_square_save_to_file_empty(self):
        """Test - saves empty square to file"""
        Square.save_to_file([])
        with open("Square.json", 'r', encoding="utf-8") as file:
            s = file.read()
        self.assertEqual(s, '[]')

    def test_square_save_to_file_none(self):
        """Test - saves none square to file"""
        Square.save_to_file(None)
        with open("Square.json", 'r', encoding="utf-8") as file:
            s = file.read()
        self.assertEqual(s, '[]')

    def test_rectangle_to_dictionary(self):
        """Test - square becomes dictionary"""
        s = Square(1, 2, 3, 4)
        s_dictionary =  s.to_dictionary()
        self.assertEqual(s_dictionary,
                         {'id': 4, 'size': 1, 'x': 2, 'y': 3})

    def test_square_load_from_file(self):
        """Test - square lods file"""
        s = Square(1, 2, 3, 4)
        Square.save_to_file([s])
        output = Square.load_from_file()
        self.assertEqual(str(output[0]), '[Square] (4) 2/3 - 1')

if __name__ == '__main__':
    unittest.main()
