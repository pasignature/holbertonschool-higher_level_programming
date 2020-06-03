#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """Rectangle Class"""

    def __init__(self, width, height):
        """inits the class"""

        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
