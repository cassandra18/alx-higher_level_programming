#!/usr/bin/python3
"""Student class module"""


class Student():
    """
    Student Class
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation with first_name, last_name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        A function that retrieves a dictionary representation of a Student
        instance.

        Args:
            attrs (list or None): A list of attribute names to retrieve.
            If None, retrieve all attributes.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        dictionary = {}
        if attrs is None:
            attrs = dir(self)
        for attr_name in attrs:
            if not attr_name.startswith("__") and hasattr(self, attr_name):
                attr_value = getattr(self, attr_name)
                if isinstance(attr_value, (list, dict, str, int, bool)):
                    dictionary[attr_name] = attr_value
        return dictionary

    def reload_from_json(self, json_data):
        """
        Replaces all attributes of the Student instance as JSON representation

        Args:
            json_data (dict): A dict with attribute names and values.
        """
        for attr_name, attr_value in json_data.items():
            setattr(self, attr_name, attr_value)
