#!/usr/bin/python3
"""Sqaure #2 Module"""


class Square(__import__('9-rectangle').Rectangle):
    """Square Class"""

    def __init__(self, size):
        """Initializes the square"""

        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        """Calculates the area"""

        return self.__size * self.__size

    def __str__(self):
        """Return a formatted string to be printed"""

        return '[Square] {0}/{0}'.format(self.__size)
