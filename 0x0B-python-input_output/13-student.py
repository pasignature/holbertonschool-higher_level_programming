#!/usr/bin/python3
"""Student To Disk And Reload"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """Initialize"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves the dict repr of Student"""

        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        d = {}
        for k in attrs:
            if not isinstance(k, str):
                return self.__dict__
            if k in self.__dict__.keys():
                d[k] = self.__dict__[k]
        return d

    def reload_from_json(self, json):
        """Replaces all attributes of the instances"""

        for k in json.keys():
            self.__dict__[k] = json[k]
