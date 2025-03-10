import unittest
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import more_lists as ml

class TestListFunctions(unittest.TestCase):
    def test_sum_list(self):
        # Call the function
        result = ml.sum_list()
        
        # Check if the result is as expected
        self.assertEqual(result, 17, "The sum of the list should be 17.")

    def test_add_to_list(self):
        # Test input list
        input_list = [2, 4, 3, 8]
        
        # Call the function
        result = ml.add_to_list(input_list)
        
        # Check if the result is as expected
        self.assertEqual(result, [3, 5, 4, 9], "The list should be [3, 5, 4, 9] after adding 1 to each element.")

if __name__ == "__main__":
    unittest.main()