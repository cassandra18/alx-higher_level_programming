import unittest
import io
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(10, 9)
        self.r2 = Rectangle(2, 5, 1, 1, 2)
        self.r3 = Rectangle(7, 19, 2, 5, 90)
    def tearDown(self):
        pass

    def test_id(self):
        self.assertEqual(self.r1.id, 1)
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

if __name__ == "__main__":
    unittest.main()
