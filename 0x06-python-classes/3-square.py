#!/usr/bin/python3

"""Define a new Square."""

class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area od the square."""
        return (self.__size * self.__size)
