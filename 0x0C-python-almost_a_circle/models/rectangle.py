#!/usr/bin/python3
"""Defines a class Rectangle that inherits from Base."""


from models.base import Base


class Rectangle(Base):
    """A class that inherits from Base. It contains private instance
    attributes ech with its on getter and setter."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """The init method initializes the Rectangle."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.
        
        Args:
            value: The new width value.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If the value is not positive.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.
    
        Args:
            value: The new height value.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If the value is not positive.
        """
        if not isinstance(value, int):
            raise TypeError(" height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    
    @property
    def x(self):
        """Get the value x of the rectangle."""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Set the value x of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x  must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the value y of the rectangle."""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Set the value y of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area method returns the area of the rectangle using
        height and width."""
        return (self.__width * self.__height)

    def display(self):
        """Print the rectangle using #.
        Position the rectangle using x and y coordinates."""
        for y_coord in range(self.__y):
            print()

        for h in range(self.__height):
            for x_coord in range(self.__x):
                print(" ", end='')
            for w in range (self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """Return formatted string."""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """Update method assigns an argument to each attribute.

        Args:
            *args: Positional argument, it allows a user to pass
                    variable number of arguments.
        """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
