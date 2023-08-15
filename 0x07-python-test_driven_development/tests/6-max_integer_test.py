#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer function."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [12, 13, 14]
        self.assertEqual(max_integer(ordered), 14)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [12, 14, 13]
        self.assertEqual(max_integer(unordered), 14)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [14, 13, 12]
        self.assertEqual(max_integer(max_at_beginning), 14)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [15]
        self.assertEqual(max_integer(one_element), 15)

    def test_floats(self):
        """Test a list of floats and finds max."""
        floats = [11.1, 12.2, 13.3, 14.4]
        self.assertEqual(max_integer(floats), 14.4)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [11.1, 12, 13.3, 14.4]
        self.assertEqual(max_integer(ints_and_floats), 14.4)

    def test_string(self):
        """Test a string."""
        string = "Lekei"
        self.assertEqual(max_integer(string), 'k')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Did", "call", "you", "Lelei"]
        self.assertEqual(max_integer(strings), "Lelei")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
