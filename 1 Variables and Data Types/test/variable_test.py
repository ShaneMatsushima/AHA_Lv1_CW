import unittest
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import variables

class TestVariables(unittest.TestCase):
    def test_int_var(self):
        """Test if int_var is an integer."""
        self.assertIsInstance(variables.int_var, int)

    def test_str_var(self):
        """Test if str_var is a string."""
        self.assertIsInstance(variables.str_var, str)

    def test_bool_var(self):
        """Test if bool_var is a boolean."""
        self.assertIsInstance(variables.bool_var, bool)

    def test_float_var(self):
        """Test if float_var is a float."""
        self.assertIsInstance(variables.float_var, float)

    def test_temperature_data(self):
        """Test if temperature_data is a float."""
        self.assertIsInstance(variables.temperature_data, float)

    def test_moisture_data(self):
        """Test if moisture_data is a float."""
        self.assertIsInstance(variables.moisture_data, float)

    def test_temperature_pin(self):
        """Test if temperature_pin is an integer."""
        self.assertIsInstance(variables.temperature_pin, int)

if __name__ == "__main__":
    unittest.main()