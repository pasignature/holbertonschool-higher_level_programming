#!/usr/bin/python3
"""Student To JSON"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """Initialize"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves the dict repr of Student"""

        return self.__dict__
