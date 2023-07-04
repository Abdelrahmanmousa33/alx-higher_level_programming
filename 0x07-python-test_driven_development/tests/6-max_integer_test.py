#!/usr/bin/python3
"""unittest for max_integer"""

import unittest
max_integer =  __import__('6-max_integer').max_integer

class TestMaxInt(unittest.TestCase):
    """unittest class for max_integer"""
    
    def test_orderd(self):
        """test orderd list"""

        test = [1, 2, 3, 4]
        self.assertEqual(max_integer(test), 4)

    def test_unorderd(self):
        """test unorderd list"""

        test = [1, 4, 3, 2]
        self.assertEqual(max_integer(test), 4)

    def test_empty_list(self):
        """Test an empty list."""

        test = []
        self.assertEqual(max_integer(test), None)
        
    def test_max_at_begining(self):
        """tests when max at begining"""

        test = [4, 2, 3, 1]
        self.assertEqual(max_integer(test), 4)

    def test_one_element_list(self):
        """Test with a single element."""

        test = [7]
        self.assertEqual(max_integer(test), 7)

    def test_floats(self):
        """Test a list of floats."""

        test = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(test), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""

        test = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(test), 15.5)

    def test_string(self):
        """Test a string."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
