import unittest
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import func_hello_world as f

class TestHelloFunction(unittest.TestCase):
    def test_hello(self):
        # Call the function
        result = f.hello()
        
        # Check if the result is as expected
        self.assertEqual(result, "Hello World", 'The function should return "Hello World".')

if __name__ == "__main__":
    unittest.main()