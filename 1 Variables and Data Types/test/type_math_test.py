import unittest
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import types_and_math as tm

class TestVariablesAndMath(unittest.TestCase):

    def test_type_casting(self):
        self.assertEqual(tm.int_to_str, "5")
        self.assertEqual(tm.bool_to_int, 1)
        self.assertEqual(tm.int_to_float, 5.0)
        self.assertEqual(tm.float_to_int, 3)
        self.assertEqual(tm.str_to_bool, True)

    def test_math_operations(self):
        self.assertEqual(tm.sum_a_b, 3)
        self.assertEqual(tm.sub_d_c, -1)
        self.assertEqual(tm.mul_b_c, 6)
        self.assertEqual(tm.div_a_d, 0.25)

if __name__ == '__main__':
    unittest.main()