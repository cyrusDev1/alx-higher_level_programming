#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function."""

    def test_list(self):
        """Test a list with a beginning max value."""
        lt = [7, 6, 10, 4, 9]
        self.assertEqual(max_integer(lt), 10)

    def test_max_at_beginning(self):
        """Test a list with a beginning max value."""
        lt = [7, 6, 5, 4, 2]
        self.assertEqual(max_integer(lt), 7)

    def test_max_at_end(self):
        """Test a list with a end max value."""
        lt = [0, 1, 5, 4, 8]
        self.assertEqual(max_integer(lt), 8)

    def test_one_element(self):
        """Test a string"""
        lt = [7]
        self.assertEqual(max_integer(lt), 7)

    def test_with_str_in_list(self):
        """Test a string"""
        lt = ["i", "am", "cyrus"]
        self.assertEqual(max_integer(lt), "i")

    def test_empty_list(self):
        """Test a string"""
        lt = []
        self.assertEqual(max_integer(lt), None)

    def test_string(self):
        """Test a string"""
        s = "Cyrus"
        self.assertEqual(max_integer(s), "y")

    def test_empty_string(self):
        """Test a string"""
        s = ""
        self.assertEqual(max_integer(s), None)

    def test_floats(self):
        """Test floats"""
        lt = [0.7, 0.8, 0.1]
        self.assertEqual(max_integer(lt), 0.8)

    def test_negative(self):
        """Test negative"""
        lt = [-1, -8, -9, -6]
        self.assertEqual(max_integer(lt), -1)

    def test_no_list(self):
        """Test no list"""
        self.assertRaises(TypeError, max_integer, 10)

    def test_with_none(self):
        """Test with none"""
        self.assertRaises(TypeError, max_integer, None)


if __name__ == "__main__":
    unittest.main()
