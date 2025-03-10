import unittest
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import loop_intro as loop
class TestLoopSum(unittest.TestCase):
    def test_loop_sum(self):
        # Call the function
        result_1 = loop.loop_sum()
        
        # Check if the result is as expected
        self.assertEqual(result_1, 5, "The sum should be 5 after 5 iterations.")

        # Call the function
        result_2 = loop.while_loop()
        
        # Check if the result is as expected
        self.assertEqual(result_2, 10, "The sum should be 10 when count reaches 5.")

if __name__ == "__main__":
    unittest.main()