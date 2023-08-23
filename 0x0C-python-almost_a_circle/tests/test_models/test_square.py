import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    
    def setUp(self):
        self.s1 = Square(3, 1, 1, 20)
        self.s2 = Square(2, 2, 2, 19)

    def tearDown(self):
        pass

    def test_init(self):
        """Test initialization of the Square class."""
        self.assertEqual(self.s1.id, 20)
        self.assertEqual(self.s1.size, 3)
        self.assertEqual(self.s1.x, 1)
        self.assertEqual(self.s1.y, 1)

    def test_size_setter(self):
        """Test size setter."""
        self.assertEqual(self.s1.size, 3)
        self.assertEqual(self.s2.width, 2)
        self.assertEqual(self.s2.height, 2)

    def test_size_setter_invalid(self):
        """Test size setter with invalid size values."""
        with self.assertRaises(ValueError):
            self.s1.size = -10
        with self.assertRaises(TypeError):
            self.s2.size = "invalid"

    def test_str(self):
        """Test the __str__() method."""
        self.assertEqual(str(self.s1), "[Square] (20) 1/1 - 3")

    def test_update(self):
        """Test the update() method."""
        self.s2.update(1, 8, 4, 5)
        self.assertEqual(self.s2.id, 1)
        self.assertEqual(self.s2.size, 8)
        self.assertEqual(self.s2.x, 4)
        self.assertEqual(self.s2.y, 5)

    def test_update_with_args(self):
        """Test the update() method with *args."""
        self.s1.update(1, 8, 4, 5)
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s1.size, 8)
        self.assertEqual(self.s1.x, 4)
        self.assertEqual(self.s1.y, 5)

    def test_update_with_kwargs(self):
        """Test the update() method with **kwargs."""
        self.s2.update(size=10, y=6)
        self.assertEqual(self.s2.size, 10)
        self.assertEqual(self.s2.y, 6)

    def test_to_dictionary(self):
        """Test the to_dictionary() method."""
        expected_dict = {'id': 19, 'size': 2, 'x': 2, 'y': 2}
        self.assertEqual(self.s2.to_dictionary(), expected_dict)

    def test_invalid_coordinates(self):
        """Test initialization with invalid coordinates."""
        with self.assertRaises(ValueError):
            self.s1.y = -2
        with self.assertRaises(TypeError):
            self.s2.x = "x"

    def test_invalid_to_dictionary(self):
        """Test to_dictionary() with invalid attributes."""
        with self.assertRaises(TypeError):
            self.s2.width = "invalid"
            self.s2.to_dictionary()


if __name__ == "__main__":
    unittest.main()
