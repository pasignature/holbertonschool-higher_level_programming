#!/usr/bin/python3
from json import load

"""Create Object From A JSON File"""


def load_from_json_file(filename):
    """creates an object from a JSON file"""

    with open(filename, "r", encoding="UTF-8") as f:
        return load(f)
