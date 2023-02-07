"""
Exam Resit for Software Metrics
implementation of test cases for the math function math.isfinite()
"""
import math
import unittest
from math_function import is_finite


class TestIsFiniteMethods(unittest.TestCase):
    """Test the is_finite method"""
    def test_right_result(self):
        """test if the result will be right with proper arguments"""
        self.assertEqual(is_finite(2000), True)
        self.assertEqual(is_finite(math.inf), False)

    def test_wrong_result(self):
        """test if the result will be wrong with proper arguments"""
        self.assertNotEqual(is_finite(0.0), False)
        self.assertNotEqual(is_finite(-math.inf), True)

    def test_without_arguments(self):
        """test without any given arguments to the method"""
        with self.assertRaises(TypeError):
            is_finite()

    def test_incorrect_arguments_string(self):
        """Test with invalid arguments, specifically with string"""
        input_string = "5"
        with self.assertRaises(TypeError):
            is_finite(input_string)

    def test_incorrect_arguments_array(self):
        """Test with invalid arguments, specifically with array"""
        input_array = [5, 2]
        with self.assertRaises(TypeError):
            is_finite(input_array)


if __name__ == "__main__":
    unittest.main(verbosity=2)
