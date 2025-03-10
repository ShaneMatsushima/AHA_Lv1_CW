import unittest
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import more_functions as f

class TestFunctions(unittest.TestCase):
    def test_add_func(self):
        """Test add_func which should sum two integers"""
        self.assertEqual(f.add_func(1, 2), 3)
    
    def test_multiply_func(self):
        """Test multiply_func which should multiply two integers"""
        self.assertEqual(f.multiply_func(2, 3), 6)
    
    def test_divide_func(self):
        """Test divide_func which should divide two integers"""
        self.assertEqual(f.divide_func(6, 2), 3)

    def test_sum_list(self):
        """Test sum_list which should sum a list of integers"""
        self.assertEqual(f.sum_list([1, 2, 3]), 6)
    
    def test_multiply_lists(self):
        """Test multiply_lists which should multiply two lists of integers"""
        self.assertEqual(f.multiply_lists([1, 2], [3, 4]), [3, 8])
        self.assertEqual(f.multiply_lists([1, 2, 3], [4, 5, 6]), [4, 10, 18])
    
if __name__ == "__main__":
    unittest.main()

    
