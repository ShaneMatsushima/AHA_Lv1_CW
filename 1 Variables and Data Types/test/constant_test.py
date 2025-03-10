import unittest
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import constants_vs_variables as cv

class TestCirclePhysics(unittest.TestCase):
    def test_pi_constant(self):
        """Test if the PI constant is correctly defined."""
        self.assertEqual(cv.PI, 3.14159)

    def test_gravity_constant(self):
        """Test if the GRAVITY constant is correctly defined."""
        self.assertEqual(cv.GRAVITY, 9.81)

    def test_area_1_calculation(self):
        """Test the first area calculation with the initial radius."""
        expected_area_1 = cv.PI * (24.38 ** 2)
        self.assertAlmostEqual(cv.area_1, expected_area_1, places=5)

    def test_force_calculation(self):
        """Test the force calculation using mass and GRAVITY."""
        # Assuming you set the mass to 5.0
        mass = 5.0
        expected_force = mass * cv.GRAVITY
        self.assertAlmostEqual(cv.force, expected_force, places=5)

if __name__ == "__main__":
    unittest.main()