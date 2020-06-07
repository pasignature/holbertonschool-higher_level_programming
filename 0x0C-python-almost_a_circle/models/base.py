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
