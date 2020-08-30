#!/usr/bin/python3
from json import dump

"""Save Object To A File"""


def save_to_json_file(my_obj, filename):
    """Writes an object to text file using JSON repr"""

    with open(filename, "w", encoding="UTF-8") as f:
        dump(my_obj, f)
