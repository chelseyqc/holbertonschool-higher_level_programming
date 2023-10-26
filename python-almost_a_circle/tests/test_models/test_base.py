#!/usr/bin/python3
"""Base module unit tests"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Base unit tests"""

    def test_id(self):
        """Test - generated id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        a = Base()
        b = Base()
        self.assertEqual(b.id, a.id + 1)

    def test_id_input(self):
        """Test - id inputted as arg"""
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_base_to_json_string(self):
        """Test - to_json_string list_dictionaries is not empty"""
        json_dictionary = Base.to_json_string([{'id': 10}])
        self.assertEqual(json_dictionary, "[{\"id\": 10}]")

    def test_base_to_json_string_none(self):
        """Test - to_json_string list_dictionaries is None"""
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")

    def test_base_to_json_string_empty(self):
        """Test - to_json_string list_dictionaries is empty"""
        input = []
        self.assertEqual(Base.to_json_string(input), "[]")

    def test_from_json_string(self):
        """Test - from_json_string converts correctly"""
        input = "[{\"id\": 89}]"
        expected = [{"id": 89}]
        self.assertEqual(Base.from_json_string(input), expected)

    def test_from_json_string_none(self):
        """Test - from_json_string is None"""
        input = None
        expected = []
        self.assertEqual(Base.from_json_string(input), expected)

    def test_from_json_string_empty(self):
        """Test - from_json_string is empty"""
        input = "[]"
        self.assertEqual(Base.from_json_string(input), [])

    def test_from_json_string_type(self):
        """Test - from_json_string creates correct type"""
        input = Base.from_json_string("[{\"id\": 89}]")
        self.assertEqual(type(input).__name__, "list")

if __name__ == '__main__':
    unittest.main()