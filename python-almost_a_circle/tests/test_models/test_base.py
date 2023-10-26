#!/usr/bin/python3
"""Base module unit tests"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Base unit tests"""

    def test_baseid(self):
        """Test - if id is not None"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
