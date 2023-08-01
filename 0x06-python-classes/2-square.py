#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a class Square"""

    def __init__(self, size):
        """Instantiation with a new size Square."""

        """size (int): The size of a new Square."""
        self.__size = size

        def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
