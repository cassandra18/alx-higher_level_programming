#!/usr/bin/python3
"""Defines a class Square."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class is a subclass if the Rectangle class."""
    def __init__(self, size, x=0, y=0, id=None):
        """The init method initializes the square.

        Args:
            self: Refer to the Square class object.
            size: Refer to the width and height of the square.
            x: Position the square horizontally in the x-y axis.
            y: Position the square vertically in the x-y axis
            id: Identity of each square instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size attribute of the square."""
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """The str method formats the string that is printed
        on the stdout."""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    def update(self, *args, **kwargs):
        """Update method assigns an argument to each attribute."""
        if args and len(args) > 0:
            attributes = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    
    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
