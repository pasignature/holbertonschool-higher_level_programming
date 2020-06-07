#!/usr/bin/python3
"""Class for Base"""

import json

class Base:
    '''Base Class with its private attributes'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Instantiation of Base Class constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Method returns the JSON string rep. of function'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
