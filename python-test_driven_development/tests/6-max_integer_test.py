#!/usr/bin/python3
"""unit testing for max_integer function"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer"""

    def test_empty_list(self):
        """Empty list"""
        self.assertEqual(max_integer(), None)

    def test_one_element(self):
        """List contains only one element"""
        self.assertEqual(max_integer([1]), 1)

    def test_multiple_max(self):
        """List contains multiple elements with the same max value"""
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_negative(self):
        """List contains negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_int_float(self):
        """List contains both integers and floats"""
        self.assertEqual(max_integer([1.5, 2, 3, 3.5]), 3.5)

    def test_middle_max(self):
        """List contains the max in the middle"""
        self.assertEqual(max_integer([1, 3, 2]), 3)


if __name__ == '__main__':
    unittest.main()
