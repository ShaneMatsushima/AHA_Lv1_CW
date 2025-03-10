import sys
import os
import unittest

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from add import add  # Import the add function from add.py in the parent directory

class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)  # Test adding two positive numbers

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)  # Test adding two negative numbers

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 1), 0)  # Test adding a negative and a positive number

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)  # Test adding zeros
        self.assertEqual(add(5, 0), 5)  # Test adding zero to a positive number