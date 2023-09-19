#!/usr/bin/python3
"""A moduke that defines a class-Base."""


import json


class Base:
    """
    A class that defines a method used to reeturn the an instance
    id.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        A method that initializes the class, Base.

        Args:
            id = public instance attribute. Default value is None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None:
            return "[]"
        if not isinstance(list_dictionaries, list):
            raise TypeError("Input must be a list.")

        for item in list_dictionaries:
            if not isinstance(item, dict):
                raise TypeError("Each item in the list must be a dictionary.")

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)
        with open(filename, "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string

        Args:
            json_string: the string representing dictionaries

        Returns:
            list of the JSON string representation json_string
        """
        if json_string is None or json_string == "":
            return []

        try:
            output = json.loads(json_string)
            if not isinstance(output, list):
                raise TypeError("JSON string does not represent a list.")
            for item in output:
                if not isinstance(item, dict):
                    raise TypeError(
                            "Each item in the list must be a dictionary.")
            return output
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON string.")

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                list_dicts = json.loads(json_string)
                list_inst = [cls.create(**dict_obj) for dict_obj in list_dicts]
                return list_inst
        except FileNotFoundError:
            return []
