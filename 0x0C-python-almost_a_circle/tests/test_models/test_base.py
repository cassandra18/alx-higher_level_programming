#!/usr/bin/python3
import unittest
import json
import os
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestBaseClass(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        pass

    def test_instance_creation(self):
        first_instance = Base()
        self.assertEqual(first_instance.id, 1, "Instance 1 ID mismatch")

        second_instance = Base()
        self.assertEqual(second_instance.id, 2, "Instance 2 ID mismatch")

        specified_id = 100
        third_inst = Base(id=specified_id)
        self.assertEqual(third_inst.id, specified_id, "Instance 3 ID mismatch")

    def test_instance_id_assignment(self):
        """
        Test the correct assignment of IDs to instances.
        """
        first_instance = Base()
        second_instance = Base()
        third_inst = Base(id=10)
        self.assertEqual(first_instance, 1, "Instance 1 ID assignment mismatch")
        self.assertEqual(second_instance.id, 2, "Instance 2 ID assignment mismatch")
        self.assertEqual(third_inst.id, 10, "Instance 3 ID assignment mismatch")

    def test_to_json_string_empty_list(self):
        """
        Test to_json_string method with an empty list.
        """
        dictionary = []
        json_string = Base.to_json_string(dictionary)
        self.assertEqual(json_string, "[]")

    def test_to_json_string_list(self):
        """
        Test to_json_string method with a non-empty list of dictionaries.
        """
        dictionary = [{'key': 'value'}, {'one': 'two'}]
        json_string = Base.to_json_string(dictionary)
        expected_json = json.dumps(dictionary)
        self.assertEqual(json_string, expected_json)

    def test_to_json_string_invalid_dicts(self):
        """
        Test to_json_string method with a non-empty list containing
        non-dictionaries.
        """
        non_dict_list = ['one', 2, None]
        with self.assertRaises(TypeError):
            Base.to_json_string(non_dict_list)

    def test_save_to_file_empty_list(self):
        """
        Test save_to_file method with an empty list of instances.
        """
        empty_list = []
        f = "Base.json"
        Base.save_to_file(empty_list)
        self.assertTrue(
            os.path.exists(f), f"File '{f}' not found")
        with open(f, "r") as f_ile:
            content = f_ile.read()
            self.assertEqual(content, "[]")

    def test_save_to_file_list(self):
        """
        Test save_to_file method with a non-empty list of instances.
        """
        first_instance = Rectangle(10, 20)
        second_instance = Square(5)
        instance_list = [first_instance, second_instance]
        f_ile = f"{Base.__name__}.json"
        Base.save_to_file(instance_list)
        self.assertTrue(
            os.path.exists(f_ile), f"File '{f_ile}' not found")
        with open(f_ile, "r") as f:
            content = f.read()
            expected_content = Base.to_json_string(
                [first_instance.to_dictionary(), second_instance.to_dictionary()])
            self.assertEqual(content, expected_content)

    def test_from_json_string_valid_input(self):
        json_string = '[{"key": "value"}, {"one": "two"}]'
        output = Base.from_json_string(json_string)
        self.assertIsInstance(output, list)
        self.assertListEqual(output, [{"key": "value"},
                                      {"one": "two"}])

    def test_from_json_string_invalid_input(self):
        invalid_json_string = "invalid json"
        with self.assertRaises(ValueError):
            Base.from_json_string(invalid_json_string)

    def test_from_json_string_empty_input(self):
        empty_json_string = ""
        output = Base.from_json_string(empty_json_string)
        self.assertIsInstance(output, list)
        self.assertListEqual(output, [])

    def test_from_json_string_non_string_input(self):
        non_string_input = 123
        with self.assertRaises(TypeError):
            Base.from_json_string(non_string_input)

    def test_load_from_file_rectangle(self):
        """
        Test loading instances of Rectangle from file.
        """
        f_name = "Rectangle.json"
        try:
            os.remove(f_name)
        except FileNotFoundError:
            pass

        r1 = Rectangle(10, 20)
        r2 = Rectangle(5, 10)
        rect_list = [r1, r2]
        Rectangle.save_to_file(rect_list)

        loaded_rectangles = Rectangle.load_from_file()

        self.assertIsInstance(loaded_rectangles, list)
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertIsInstance(loaded_rectangles[0], Rectangle)
        self.assertIsInstance(loaded_rectangles[1], Rectangle)
        self.assertEqual(loaded_rectangles[0].width, r1.width)
        self.assertEqual(loaded_rectangles[0].height, r1.height)
        self.assertEqual(loaded_rectangles[1].width, r2.width)
        self.assertEqual(loaded_rectangles[1].height, r2.height)

    def test_load_from_file_square(self):
        """
        Test loading instances of Square from file.
        """
        f_ile = "Square.json"
        try:
            os.remove(f_ile)
        except FileNotFoundError:
            pass

        s1 = Square(5)
        s2 = Square(10)
        square_list = [s1, s2]
        Square.save_to_file(square_list)

        loaded_squares = Square.load_from_file()

        self.assertIsInstance(loaded_squares, list)
        self.assertEqual(len(loaded_squares), 2)
        self.assertIsInstance(loaded_squares[0], Square)
        self.assertIsInstance(loaded_squares[1], Square)
        self.assertEqual(loaded_squares[0].size, s1.size)
        self.assertEqual(loaded_squares[1].size, s2.size)

    def test_create_rectangle(self):
        """Test create method for Rectangle class."""
        rect_dict = {'id': 51, 'width': 9, 'height': 67, 'x': 0, 'y': 8}
        rect_instance = Rectangle.create(**rect_dict)

        self.assertIsInstance(rect_instance, Rectangle)
        self.assertEqual(rect_instance.id, 51)
        self.assertEqual(rect_instance.width, 9)
        self.assertEqual(rect_instance.height, 67)
        self.assertEqual(rect_instance.x, 0)
        self.assertEqual(rect_instance.y, 8)

    def test_create_square(self):
        """Test create method for Square class."""
        square_dict = {'id': 12, 'size': 55, 'x': 9, 'y': 8}
        square_instance = Square.create(**square_dict)

        self.assertIsInstance(square_instance, Square)
        self.assertEqual(square_instance.id, 12)
        self.assertEqual(square_instance.size, 55)
        self.assertEqual(square_instance.x, 9)
        self.assertEqual(square_instance.y, 8)


if __name__ == '__main__':
    unittest.main()
