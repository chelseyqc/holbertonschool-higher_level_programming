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

    def test_id_input(self):
        """Test - id inputted as arg"""
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
