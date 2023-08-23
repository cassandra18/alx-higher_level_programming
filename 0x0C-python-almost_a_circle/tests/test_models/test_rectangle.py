#!/usr/bin/python3
import unittest
import sys
import io
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    
    def setUp(self):
        self.r1 = Rectangle(10, 9)
        self.r2 = Rectangle(2, 5, 1, 1, 2)
        self.r3 = Rectangle(7, 19, 2, 5, 90)
    
    def tearDown(self):
        pass

    def test_id(self):
        #self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 90)
    def test_width(self):
        self.assertEqual(self.r1.width, 10)
        with self.assertRaises(ValueError):
            self.r2.width = -1
        with self.assertRaises(TypeError):
            self.r1.width = "9"

    def test_height(self):
        self.assertEqual(self.r1.height, 9)
        with self.assertRaises(ValueError):
            self.r2.height = -1
        with self.assertRaises(TypeError):
            self.r1.height = "9"
        with self.assertRaises(TypeError):
            self.r1.height = {}

    def test_x(self):
        self.assertEqual(self.r3.x, 2)
        with self.assertRaises(ValueError):
            self.r2.x = -1
        with self.assertRaises(TypeError):
            self.r1.x = "9"
        with self.assertRaises(TypeError):
            self.r1.x = {}

    def test_y(self):
        self.assertEqual(self.r3.y, 5)
        with self.assertRaises(ValueError):
            self.r2.y = -1
        with self.assertRaises(TypeError):
            self.r1.y = None
        with self.assertRaises(TypeError):
            self.r1.y = {}

    def test_area(self):
        self.assertEqual(self.r1.area(), 90)

    def test_display(self):
        expected_output = "\n ##\n ##\n ##\n ##\n ##\n"
        saved_stdout = sys.stdout
        sys.stdout = io.StringIO()

        self.r2.display()
        output = sys.stdout.getvalue()
        
        sys.stdout = saved_stdout
        
        self.assertEqual(output, expected_output)

    def test_str(self):
        #expected_output_r1 = "[Rectangle] (1) 0/0 - 10/9"
        expected_output_r2 = "[Rectangle] (2) 1/1 - 2/5"

        #self.assertEqual(str(self.r1), expected_output_r1)
        self.assertEqual(str(self.r2), expected_output_r2)

    def test_update_with_args(self):
        self.r1.update(10, 7, 6, 1, 2)
        self.assertEqual(self.r1.id, 10)
        self.assertEqual(self.r1.width, 7)
        self.assertEqual(self.r1.height, 6)
        self.assertEqual(self.r1.x, 1)
        self.assertEqual(self.r1.y, 2)
    
    def test_update_with_kwargs(self):
        self.r2.update(id=42, width=8, y=5)
        self.assertEqual(self.r2.id, 42)
        self.assertEqual(self.r2.width, 8)
        self.assertEqual(self.r2.y, 5)

    def test_to_dictionary(self):
        self.assertEqual(self.r3.to_dictionary(), {'x': 2, 'y': 5, 'id': 90, 'height': 19, 'width': 7})
    
    def test_invalid_area(self):
        """Test the area() method with invalid attributes."""
        with self.assertRaises(ValueError):
            self.r3.width = -5
            self.r3.area()

    def test_invalid_display(self):
        """Test the display() method with invalid attributes."""
        with self.assertRaises(ValueError):
            self.r1.height = -3
            self.r1.display()

    def test_invalid_to_dictionary(self):
        """Test to_dictionary() with invalid attributes."""
        with self.assertRaises(TypeError):
            self.r2.width = "invalid"
            self.r2.to_dictionary()

if __name__ == "__main__":
    unittest.main()
